import unittest

from main import *

class TestSolution(unittest.TestCase):
    def test_contains(self):
        self.assertTrue(contains((0, 0, 2, 2), (0, 0, 1, 1)))
        self.assertTrue(contains((0, 0, 2, 2), (0, 0, 2, 2)))
        self.assertTrue(contains((0, 0, 2, 2), (1, 1, 1, 1)))
        self.assertFalse(contains((0, 0, 2, 2), (1, 1, 2, 2)))
        self.assertFalse(contains((0, 0, 2, 2), (0, 0, 3, 3)))

    def test_intersects(self):
        self.assertTrue(intersects((0, 0, 2, 2), (0, 0, 1, 1)))
        self.assertTrue(intersects((0, 0, 2, 2), (1, 1, 1, 1)))
        self.assertTrue(intersects((0, 0, 2, 2), (1, 1, 2, 2)))
        self.assertTrue(intersects((0, 0, 2, 2), (0, 0, 2, 2)))
        self.assertTrue(intersects((0, 0, 2, 2), (0, 0, 3, 3)))
        self.assertFalse(intersects((0, 0, 2, 2), (2, 2, 1, 1)))
        self.assertFalse(intersects((0, 0, 2, 2), (3, 3, 1, 1)))
