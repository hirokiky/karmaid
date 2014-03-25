import unittest

from pyramid import testing


class TestKarmaResource(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from karmaid.resources import KarmaResource
        return KarmaResource(*args, **kwargs)

    def test__invalid_resource(self):
        request = testing.DummyRequest(params={})
        target = self._makeOne(request)
        from pyramid.httpexceptions import HTTPBadRequest
        with self.assertRaises(HTTPBadRequest):
            target.resource

    def test__valid_resource(self):
        request = testing.DummyRequest(params={'resource': 'Ritsu'})
        target = self._makeOne(request)
        self.assertEqual('Ritsu', target.resource)
