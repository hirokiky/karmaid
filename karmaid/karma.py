from karmaid.redisio import get_redis


KARMA_KEY_NAME = 'karma'


def get_karma(resource):
    karma = get_redis().zscore(KARMA_KEY_NAME, resource)
    return int(karma) if karma else 0


def inc_karma(resource):
    return int(get_redis().zincrby(KARMA_KEY_NAME, resource))


def dec_karma(resource):
    return int(get_redis().zincrby(KARMA_KEY_NAME, resource, amount=-1))


def get_best_resources():
    return [r.decode() for r in get_redis().zrevrange(KARMA_KEY_NAME, 0, 9)]


def get_worst_resources():
    return [r.decode() for r in reversed(get_redis().zrevrange(KARMA_KEY_NAME, -10, -1))]
