import unittest

from paste.deploy.loadwsgi import loadapp
from testfixtures import tempdir
import webtest

config = b"""\
[app:main]
paste.app_factory = karmaid:main
mako.directories = karmaid:templates
redis.client = fakeredis.FakeStrictRedis
iplimitation.max_count = 10
iplimitation.expire_time = 86400
"""


def create_app(d):
    path = d.write('ftest.ini', config)
    app = loadapp("config:" + path)
    return webtest.TestApp(app)


class TestAPIKarma(unittest.TestCase):
    def tearDown(self):
        from karmaid.redisio import get_redis
        get_redis().flushall()

    @tempdir()
    def test__it(self, d):
        app = create_app(d)

        res = app.get('/api/karma', params={'resource': 'Ritsu'})
        self.assertEqual({'karma': 0, 'resource': 'Ritsu'}, res.json)

        res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'inc'})
        self.assertEqual({'karma': 1, 'resource': 'Ritsu'}, res.json)

        res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'dec'})
        self.assertEqual({'karma': 0, 'resource': 'Ritsu'}, res.json)

    @tempdir()
    def test__spam(self, d):
        app = create_app(d)

        for i in range(10):
            res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'inc'})
            self.assertEqual({'karma': i+1, 'resource': 'Ritsu'}, res.json)

        res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'inc'},
                       expect_errors=True)
        self.assertEqual(403, res.status_int)
        self.assertEqual({'status': 403, 'message': 'APIAccessReachedLimitation'}, res.json)
