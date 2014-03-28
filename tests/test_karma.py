import unittest

from karmaid.karma import KARMA_KEY_NAME
from karmaid.redisio import get_redis


def setUpModule():
    from karmaid.redisio import init_fake_redis
    init_fake_redis()


class _RedisTestCase(unittest.TestCase):
    def tearDown(self):
        get_redis().flushall()


class TestGetKarma(_RedisTestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.karma import get_karma
        return get_karma(*args, **kwargs)

    def test__karma_existed(self):
        get_redis().zadd(KARMA_KEY_NAME, 3, 'RitsuTainaka')
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(3, actual)

    def test__no_karma(self):
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(0, actual)


class TestIncKarma(_RedisTestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.karma import inc_karma
        return inc_karma(*args, **kwargs)

    def test__karma_existed(self):
        get_redis().zadd(KARMA_KEY_NAME, 3, 'RitsuTainaka')
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(4, actual)

    def test__no_karma(self):
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(1, actual)


class TestDecKarma(_RedisTestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.karma import dec_karma
        return dec_karma(*args, **kwargs)

    def test__karma_existed(self):
        get_redis().zadd(KARMA_KEY_NAME, 3, 'RitsuTainaka')
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(2, actual)

    def test__no_karma(self):
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(-1, actual)


class TestGetBestStuffs(_RedisTestCase):
    def _callFUT(self):
        from karmaid.karma import get_best_stuffs
        return get_best_stuffs()

    def test__not_enough_stuffs(self):
        redis = get_redis()
        redis.zadd(KARMA_KEY_NAME, 10000, 'cureblack')
        redis.zadd(KARMA_KEY_NAME, 9999, 'curesunny')
        redis.zadd(KARMA_KEY_NAME, 1, 'curemarine')
        actual = self._callFUT()
        self.assertEqual(['cureblack', 'curesunny', 'curemarine'], actual)

    def test__enough_stuffs(self):
        redis = get_redis()
        redis.zadd(KARMA_KEY_NAME, 6, 'ritsu')
        redis.zadd(KARMA_KEY_NAME, 5, 'jun')
        redis.zadd(KARMA_KEY_NAME, 4, 'ui')
        redis.zadd(KARMA_KEY_NAME, 3, 'nodoka')
        redis.zadd(KARMA_KEY_NAME, 2, 'ichigo')
        redis.zadd(KARMA_KEY_NAME, 1, 'sawa-chan')
        redis.zadd(KARMA_KEY_NAME, 0, 'ton-chan')
        redis.zadd(KARMA_KEY_NAME, -1, 'azunyan')
        redis.zadd(KARMA_KEY_NAME, -2, 'mugi')
        redis.zadd(KARMA_KEY_NAME, -3, 'mio')
        redis.zadd(KARMA_KEY_NAME, -4, 'yui')
        actual = self._callFUT()
        self.assertEqual(['ritsu', 'jun', 'ui', 'nodoka', 'ichigo',
                          'sawa-chan', 'ton-chan', 'azunyan', 'mugi',
                          'mio'], actual)


class TestGetWorstStuffs(_RedisTestCase):
    def _callFUT(self):
        from karmaid.karma import get_worst_stuffs
        return get_worst_stuffs()

    def test__not_enough_stuffs(self):
        redis = get_redis()
        redis.zadd(KARMA_KEY_NAME, 10000, 'darkprettycure')
        redis.zadd(KARMA_KEY_NAME, 9999, 'regine')
        redis.zadd(KARMA_KEY_NAME, -100, 'akao-ni')
        actual = self._callFUT()
        self.assertEqual(['akao-ni', 'regine', 'darkprettycure'], actual)

    def test__enough_stuffs(self):
        redis = get_redis()
        redis.zadd(KARMA_KEY_NAME, 100, 'beer')
        redis.zadd(KARMA_KEY_NAME, 99, 'sake')
        redis.zadd(KARMA_KEY_NAME, 98, 'chu-hai')
        redis.zadd(KARMA_KEY_NAME, 97, 'shochu')
        redis.zadd(KARMA_KEY_NAME, 96, 'whiskey')
        redis.zadd(KARMA_KEY_NAME, 95, 'gin')
        redis.zadd(KARMA_KEY_NAME, 94, 'rum')
        redis.zadd(KARMA_KEY_NAME, 93, 'tequila')
        redis.zadd(KARMA_KEY_NAME, 92, 'brandy')
        redis.zadd(KARMA_KEY_NAME, 91, 'wine')
        redis.zadd(KARMA_KEY_NAME, 90, 'grappa')
        actual = self._callFUT()
        self.assertEqual(['grappa', 'wine', 'brandy', 'tequila',
                          'rum', 'gin', 'whiskey', 'shochu', 'chu-hai',
                          'sake'], actual)
