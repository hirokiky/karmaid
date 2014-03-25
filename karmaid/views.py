from pyramid.view import view_config

from karmaid.karma import get_karma, inc_karma, dec_karma
from karmaid.resources import KarmaResource


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
