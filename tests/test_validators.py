import unittest


class TestValidateResource(unittest.TestCase):
    def _callFUT(self, *args, **kwargs):
        from karmaid.validators import validate_resource
        return validate_resource(*args, **kwargs)

    def test__not_str(self):
        self.assertFalse(self._callFUT(100))

    def test__too_short(self):
        self.assertFalse(self._callFUT(''))

    def test__too_long(self):
        self.assertFalse(self._callFUT('a' * 5001))

    def test__non_ascii(self):
        self.assertFalse(self._callFUT('あ' * 5000))

    def test__valid_short(self):
        self.assertTrue(self._callFUT('a'))

    def test__valid_long(self):
        self.assertTrue(self._callFUT('a' * 5000))

    def test__valid_all_candidates(self):
        import string
        self.assertTrue(self._callFUT(string.punctuation +
                                      string.ascii_letters +
                                      string.digits))
