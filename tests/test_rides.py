import unittest
import sys  # fix import errors
import os
from tests.base import ConfigTestCase
import json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RideTests(ConfigTestCase):
    """This class contains RideTests """


if __name__ == '__main__':
    unittest.main()
