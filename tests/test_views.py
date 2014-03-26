import unittest
from unittest import mock

from pyramid import testing


def _createRequest(resource):
        context = testing.DummyResource()
        context.resource = resource
        request = testing.DummyRequest()
        request.context = context
        return request


class TestTop(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import top
        return top(*args, **kwargs)

    def test__it(self):
        self.assertEqual({}, self._callFUT('dummy'))


@mock.patch('karmaid.views.get_karma', autospec=True, return_value=3)
class TestAPIKarma(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_karma
        return api_karma(*args, **kwargs)

    def test__it(self, get_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'resource': 'Ritsu', 'karma': 3}, actual)
        get_karma_mock.assert_called_with('Ritsu')


@mock.patch('karmaid.views.inc_karma', autospec=True, return_value=3)
class TestAPIInc(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_inc
        return api_inc(*args, **kwargs)

    def test__it(self, inc_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'resource': 'Ritsu', 'karma': 3}, actual)
        inc_karma_mock.assert_called_with('Ritsu')


@mock.patch('karmaid.views.dec_karma', autospec=True, return_value=3)
class TestAPIDec(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_dec
        return api_dec(*args, **kwargs)

    def test__it(self, dec_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'resource': 'Ritsu', 'karma': 3}, actual)
        dec_karma_mock.assert_called_with('Ritsu')


class TestAPIBadRequest(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_bad_request
        return api_bad_request(*args, **kwargs)

    def test__it(self):
        self.assertEqual({'status': 400, 'message': 'BadRequest'},
                         self._callFUT(testing.DummyRequest()))


@mock.patch('karmaid.views.get_worst_resources', autospec=True, return_value=['worst', 'best'])
class TestAPIWorst(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_worst
        return api_worst(*args, **kwargs)

    def test__it(self, m):
        actual = self._callFUT('dummyrequest')
        self.assertEqual({'ranking': 'worst', 'resources': ['worst', 'best']},
                         actual)


@mock.patch('karmaid.views.get_best_resources', autospec=True, return_value=['best', 'worst'])
class TestAPIBest(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_best
        return api_best(*args, **kwargs)

    def test__it(self, m):
        actual = self._callFUT('dummyrequest')
        self.assertEqual({'ranking': 'best', 'resources': ['best', 'worst']},
                         actual)
