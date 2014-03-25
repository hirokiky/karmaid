import unittest

from paste.deploy.loadwsgi import loadapp
from testfixtures import tempdir
import webtest

config = b"""\
[app:main]
paste.app_factory = karmaid:main
mako.directories = karmaid:templates
redis.client = fakeredis.FakeStrictRedis
"""


def create_app(d):
    path = d.write('ftest.ini', config)
    app = loadapp("config:" + path)
    return webtest.TestApp(app)


class TestAPIKarma(unittest.TestCase):
    @tempdir()
    def test__it(self, d):
        app = create_app(d)

        res = app.get('/api/karma', params={'resource': 'Ritsu'})
        self.assertEqual({'karma': 0, 'resource': 'Ritsu'}, res.json)

        res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'inc'})
        self.assertEqual({'karma': 1, 'resource': 'Ritsu'}, res.json)

        res = app.post('/api/karma', params={'resource': 'Ritsu', 'action': 'dec'})
        self.assertEqual({'karma': 0, 'resource': 'Ritsu'}, res.json)
