import unittest


def setUpModule():
    from karmaid.redisio import init_fake_redis
    init_fake_redis()


class TestGetKarma(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.karma import get_karma
        return get_karma(*args, **kwargs)

    def tearDown(self):
        from karmaid.redisio import get_redis
        get_redis().flushall()

    def test__karma_existed(self):
        from karmaid.redisio import get_redis
        get_redis().set('RitsuTainaka', 3)
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(3, actual)

    def test__no_karma(self):
        actual = self._callFUT('RitsuTainaka')
        self.assertEqual(0, actual)
