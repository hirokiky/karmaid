from karmaid.redisio import get_redis


KARMA_KEY_NAME = 'karma'


def get_karma(stuff):
    karma = get_redis().zscore(KARMA_KEY_NAME, stuff)
    return int(karma) if karma else 0


def inc_karma(stuff):
    return int(get_redis().zincrby(KARMA_KEY_NAME, stuff))


def dec_karma(stuff):
    return int(get_redis().zincrby(KARMA_KEY_NAME, stuff, amount=-1))


def get_best_stuffs():
    return [r.decode() for r in get_redis().zrevrange(KARMA_KEY_NAME, 0, 9)]


def get_worst_stuffs():
    return [r.decode() for r in reversed(get_redis().zrevrange(KARMA_KEY_NAME, -10, -1))]
