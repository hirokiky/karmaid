import unittest

from karmaid.redisio import get_redis


def setUpModule():
    from karmaid.redisio import init_fake_redis
    init_fake_redis()


class TestCountIP(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.iplimitation import count_ip
        return count_ip(*args, **kwargs)

    def tearDown(self):
        get_redis().flushall()

    def test__first_visitor(self):
        actual = self._callFUT('192.168.1.1', 100, -1)
        self.assertTrue(actual)
        self.assertIsNone(get_redis().get('iplimitation__192.168.1.1'))

    def test__regular_visitor(self):
        get_redis().set('iplimitation__192.168.1.1', 99)
        actual = self._callFUT('192.168.1.1', 100, -1)
        self.assertTrue(actual)
        self.assertEqual(b'100', get_redis().get('iplimitation__192.168.1.1'))

    def test__spam(self):
        get_redis().set('iplimitation__192.168.1.1', 100)
        actual = self._callFUT('192.168.1.1', 100, -1)
        self.assertFalse(actual)
        self.assertEqual(b'100', get_redis().get('iplimitation__192.168.1.1'))
