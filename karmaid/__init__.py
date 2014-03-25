from pyramid.config import Configurator

from karmaid.redisio import init_redis


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    init_redis(settings, 'redis.')

    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('top', '/')
    config.add_route('api', '/api')
    config.scan('.views')

    return config.make_wsgi_app()
