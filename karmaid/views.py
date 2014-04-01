from functools import wraps

from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config, notfound_view_config

from karmaid.iplimitation import count_ip
from karmaid.karma import get_karma, inc_karma, dec_karma, get_best_stuffs, get_worst_stuffs
from karmaid.stuffs import InvalidStuff


class APIAccessReachedLimitation(Exception):
    pass


def ip_limitation(view_callable):
    @wraps(view_callable)
    def wrapped(context, request, *args, **kwargs):
        if not count_ip(request.client_addr,
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
    try:
        stuff = request.context.stuff
    except InvalidStuff:
        raise HTTPNotFound
    return {'stuff': stuff,
            'stuff_url': request.route_url('top', _query={'stuff': stuff})}


@view_config(route_name='api_karma', request_method='GET', renderer='json')
def api_karma(request):
    stuff = request.context.stuff
    karma = get_karma(stuff)
    return {'stuff': stuff,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=inc',
             renderer='json', decorator='karmaid.views.ip_limitation')
def api_inc(request):
    stuff = request.context.stuff
    karma = inc_karma(stuff)
    return {'stuff': stuff,
            'karma': karma}


@view_config(route_name='api_karma', request_method='POST', request_param='action=dec',
             renderer='json', decorator='karmaid.views.ip_limitation')
def api_dec(request):
    stuff = request.context.stuff
    karma = dec_karma(stuff)
    return {'stuff': stuff,
            'karma': karma}


@notfound_view_config(route_name='api_karma', request_method='POST', renderer='json')
@view_config(route_name='api_karma', context=InvalidStuff, renderer='json')
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
            'stuffs': get_worst_stuffs()}


@view_config(route_name='api_ranking', renderer='json')
def api_best(request):
    return {'ranking': 'best',
            'stuffs': get_best_stuffs()}


@view_config(route_name='js_widget', renderer='widget.js.mako')
def js_widget(request):
    request.response.content_type = 'application/javascript'
    return {}
