import unittest

from main import *

class TestSolution(unittest.TestCase):
    def test_list_of_unique_values(self):
        list = [1, 2, 3, "qwer", "asdf", "zxcv"]
        shift = 2
        self.assertCountEqual(shift_list(list, shift), shift_list_with_slices(list, shift))
