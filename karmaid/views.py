from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config, notfound_view_config

from karmaid.karma import get_karma, inc_karma, dec_karma


@view_config(route_name='top', renderer='top.mako')
def top(request):
    return {}


@view_config(route_name='api_karma', request_method='GET', renderer='json')
def api_karma(request):
    resource = request.context.resource
    karma = get_karma(resource)
    return {'resource': resource,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=inc',
             renderer='json')
def api_inc(request):
    resource = request.context.resource
    karma = inc_karma(resource)
    return {'resource': resource,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=dec',
             renderer='json')
def api_dec(request):
    resource = request.context.resource
    karma = dec_karma(resource)
    return {'resource': resource,
            'karma': karma}


@notfound_view_config(route_name='api_karma', request_method='POST', renderer='json')
@view_config(route_name='api_karma', context=HTTPBadRequest, renderer='json')
def api_bad_request(request):
    request.response.status_int = 400
    return {'status': 400,
            'message': 'BadRequest'}
