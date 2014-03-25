from karmaid.redisio import get_redis


def get_karma(resource):
    karma = get_redis().get(resource)
    return int(karma) if karma else 0


def inc_karma(resource):
    return get_redis().incr(resource)


def dec_karma(resource):
    return get_redis().decr(resource)
