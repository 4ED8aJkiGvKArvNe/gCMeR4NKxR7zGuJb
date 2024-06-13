import unittest

from main import *

class TestSolution(unittest.TestCase):
    def test_list_of_unique_values(self):
        list = [1, 1, 2, 3, "qwer", "qwer", "asdf", "zxcv"]
        self.assertCountEqual(find_unique(list), find_unique_with_set(list))
