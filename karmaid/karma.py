from karmaid.redisio import get_redis


def get_karma_key(resource):
    return 'karma__{}'.format(resource)


def get_karma(resource):
    karma = get_redis().get(get_karma_key(resource))
    return int(karma) if karma else 0


def inc_karma(resource):
    return get_redis().incr(get_karma_key(resource))


def dec_karma(resource):
    return get_redis().decr(get_karma_key(resource))
