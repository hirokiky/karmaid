import unittest

from pyramid import testing


class TestKarmaResource(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from karmaid.resources import StuffResource
        return StuffResource(*args, **kwargs)

    def test__invalid_resource(self):
        request = testing.DummyRequest(params={})
        target = self._makeOne(request)
        from karmaid.stuffs import InvalidStuff
        with self.assertRaises(InvalidStuff):
            target.stuff

    def test__valid_resource(self):
        request = testing.DummyRequest(params={'stuff': 'Ritsu'})
        target = self._makeOne(request)
        self.assertEqual('Ritsu', target.stuff)
