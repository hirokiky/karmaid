_pool = None
_client = None


def init_redis(settings, prefix='redis.'):
    from importlib import import_module
    import redis
    options = dict((key[len(prefix):], settings[key])
                   for key in settings
                   if key.startswith(prefix))
    global _pool
    if _pool is None:
        _pool = redis.ConnectionPool(
            host=options['host'],
            port=int(options['port']),
            db=int(options['db']),
            password=options['password'] or None,
            socket_timeout=float(options['timeout']) if options['timeout'] else None,
        )
    global _client
    module, attr = options['client'].rsplit('.', 1)
    _client = getattr(import_module(module), attr)


def init_fake_redis():
    from fakeredis import FakeStrictRedis
    global _client
    _client = FakeStrictRedis


def get_redis():
    return _client(connection_pool=_pool)
