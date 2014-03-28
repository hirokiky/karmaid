from pyramid.config import Configurator

from karmaid.redisio import init_redis
from karmaid.resources import StuffResource


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    init_redis(settings, 'redis.')

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('top', '/')
    config.add_route('button', '/button/1/', factory=StuffResource)
    config.add_route('api_karma', '/api/karma', factory=StuffResource)
    config.add_route('api_ranking', '/api/ranking')
    config.add_route('js_widget', 'widget.js', factory=StuffResource)
    config.scan('.views')

    return config.make_wsgi_app()
