from karmaid.redisio import get_redis


def get_iplimitation_key(ipaddr):
    return 'iplimitation__{}'.format(ipaddr)


def count_ip(ipaddr, max_count, expire_time):
    redis = get_redis()
    key = get_iplimitation_key(ipaddr)
    ret = redis.get(key)
    if ret is not None and int(ret) >= max_count:
        return False
    get_redis().incr(key)
    if ret is None:
        redis.expire(key, expire_time)
    return True
