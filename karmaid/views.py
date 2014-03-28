from functools import wraps

from pyramid.httpexceptions import HTTPBadRequest
from pyramid.view import view_config, notfound_view_config

from karmaid.iplimitation import count_ip
from karmaid.karma import get_karma, inc_karma, dec_karma, get_best_resources, get_worst_resources


class APIAccessReachedLimitation(Exception):
    pass


def ip_limitation(view_callable):
    @wraps(view_callable)
    def wrapped(context, request, *args, **kwargs):
        if not count_ip(request.remote_addr,
                        int(request.registry.settings['iplimitation.max_count']),
                        int(request.registry.settings['iplimitation.expire_time'])):
            raise APIAccessReachedLimitation
        return view_callable(context, request, *args, **kwargs)
    return wrapped


@view_config(route_name='top', renderer='top.mako')
def top(request):
    return {}


@view_config(route_name='button', renderer='button1.mako')
def button(request):
    return {}


@view_config(route_name='api_karma', request_method='GET', renderer='json')
def api_karma(request):
    resource = request.context.resource
    karma = get_karma(resource)
    return {'resource': resource,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=inc',
             renderer='json', decorator='karmaid.views.ip_limitation')
def api_inc(request):
    resource = request.context.resource
    karma = inc_karma(resource)
    return {'resource': resource,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=dec',
             renderer='json', decorator='karmaid.views.ip_limitation')
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


@view_config(context=APIAccessReachedLimitation, renderer='json')
def api_reached_limitation(request):
    request.response.status_int = 403
    return {'status': 403,
            'message': 'APIAccessReachedLimitation'}


@view_config(route_name='api_ranking', renderer='json', request_param='desc')
def api_worst(request):
    return {'ranking': 'worst',
            'resources': get_worst_resources()}


@view_config(route_name='api_ranking', renderer='json')
def api_best(request):
    return {'ranking': 'best',
            'resources': get_best_resources()}
