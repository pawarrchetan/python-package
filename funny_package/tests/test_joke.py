from unittest import TestCase
from six import string_types

import funny_package

class TestJoke(TestCase):
    def test_is_string(self):
        s = funny_package.joke()
        self.assertTrue(isinstance(s, string_types))