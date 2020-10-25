from unittest import TestCase
from funny_package.command_line import main

class TestConsole(TestCase):
    def test_basic(self):
        main()