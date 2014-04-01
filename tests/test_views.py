import unittest
from unittest import mock

from pyramid import testing


def _createRequest(stuff):
        context = testing.DummyResource()
        context.stuff = stuff
        request = testing.DummyRequest()
        request.context = context
        return request


class TestIPLimitation(unittest.TestCase):
    def _makeOne(self, *args, **kwargs):
        from karmaid.views import ip_limitation
        return ip_limitation(*args, **kwargs)

    def setUp(self):
        testing.setUp(settings={'iplimitation.max_count': '300',
                                'iplimitation.expire_time': '3600'})

    @mock.patch('karmaid.views.count_ip', autospec=True, return_value=False)
    def test__reached_the_limit(self, m):
        from karmaid.views import APIAccessReachedLimitation
        target = self._makeOne(lambda: None)
        request = testing.DummyRequest()
        request.client_addr = 'dummy ipaddr'
        self.assertRaises(APIAccessReachedLimitation, target, 'dummy context', request)
        m.assert_called_with('dummy ipaddr', 300, 3600)

    @mock.patch('karmaid.views.count_ip', autospec=True, return_value=True)
    def test__under_the_limit(self, m):
        wrapped_view = mock.Mock(spec=['__call__'], return_value='dummy response')
        target = self._makeOne(wrapped_view)
        request = testing.DummyRequest()
        request.client_addr = 'dummy ipaddr'
        actual = target('dummy context', request)
        self.assertEqual('dummy response', actual)
        m.assert_called_with('dummy ipaddr', 300, 3600)
        wrapped_view.assert_called_with('dummy context', request)


class TestTop(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import top
        return top(*args, **kwargs)

    def test__it(self):
        self.assertEqual({}, self._callFUT('request'))


@mock.patch('karmaid.views.get_karma', autospec=True, return_value=3)
class TestAPIKarma(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_karma
        return api_karma(*args, **kwargs)

    def test__it(self, get_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'stuff': 'Ritsu', 'karma': 3}, actual)
        get_karma_mock.assert_called_with('Ritsu')


@mock.patch('karmaid.views.inc_karma', autospec=True, return_value=3)
class TestAPIInc(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_inc
        return api_inc(*args, **kwargs)

    def test__it(self, inc_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'stuff': 'Ritsu', 'karma': 3}, actual)
        inc_karma_mock.assert_called_with('Ritsu')


@mock.patch('karmaid.views.dec_karma', autospec=True, return_value=3)
class TestAPIDec(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_dec
        return api_dec(*args, **kwargs)

    def test__it(self, dec_karma_mock):
        actual = self._callFUT(_createRequest('Ritsu'))

        self.assertEqual({'stuff': 'Ritsu', 'karma': 3}, actual)
        dec_karma_mock.assert_called_with('Ritsu')


class TestAPIBadRequest(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_bad_request
        return api_bad_request(*args, **kwargs)

    def test__it(self):
        self.assertEqual({'status': 400, 'message': 'BadRequest'},
                         self._callFUT(testing.DummyRequest()))


class TestAPIReachedLimitation(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_reached_limitation
        return api_reached_limitation(*args, **kwargs)

    def test__it(self):
        self.assertEqual({'status': 403, 'message': 'APIAccessReachedLimitation'},
                         self._callFUT(testing.DummyRequest()))


@mock.patch('karmaid.views.get_worst_stuffs', autospec=True, return_value=['worst', 'best'])
class TestAPIWorst(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_worst
        return api_worst(*args, **kwargs)

    def test__it(self, m):
        actual = self._callFUT('dummyrequest')
        self.assertEqual({'ranking': 'worst', 'stuffs': ['worst', 'best']},
                         actual)


@mock.patch('karmaid.views.get_best_stuffs', autospec=True, return_value=['best', 'worst'])
class TestAPIBest(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.views import api_best
        return api_best(*args, **kwargs)

    def test__it(self, m):
        actual = self._callFUT('dummyrequest')
        self.assertEqual({'ranking': 'best', 'stuffs': ['best', 'worst']},
                         actual)
