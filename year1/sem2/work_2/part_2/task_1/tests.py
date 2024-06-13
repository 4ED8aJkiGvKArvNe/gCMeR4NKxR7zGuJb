from unittest.mock import MagicMock, patch
import unittest

from main import *

class TestSolution(unittest.TestCase):
    def test_find_average(self):
        self.assertEqual(find_average([(1, 1), (2, 2), (3, 3), (4, 4)]), 2.5)

    def test_find_average_deviation(self):
        self.assertEqual(find_average_deviation([(1, 1), (2, 2), (3, 3), (4, 4)], 4), 1.5)

    def test_calculate_range(self):
        # mock the real implementation of the calculate_value function
        mock_calculate_value = MagicMock()
        mock_calculate_value.side_effect = calculate_value

        with patch('main.calculate_value', mock_calculate_value):
            calculate_range(1, 1, 1, 0, 2, 0.5)

            # check if `calculate_value` was called 30 times
            self.assertEqual(mock_calculate_value.call_count, 5)

    def test_calculate_value(self):
        # mock the real implementation of the func_1, func_2, func_3 functions
        mock_func_1 = MagicMock()
        mock_func_2 = MagicMock()
        mock_func_3 = MagicMock()
        
        with patch('main.func_1', mock_func_1), \
             patch('main.func_2', mock_func_2), \
             patch('main.func_3', mock_func_3):
        
            # case 1
        
            calculate_value(1, 1, 1, -2)
        
            # check if `func_1` was called once but the `func_2` and `func_3` were not called
            self.assertEqual(mock_func_1.call_count, 1)
            self.assertEqual(mock_func_2.call_count, 0)
            self.assertEqual(mock_func_3.call_count, 0)

            mock_func_1.reset_mock()
        
            # case 2
            
            calculate_value(0, 1, 1, 2)
            
            # check if `func_2` was called once but the `func_1` and `func_3` were not called
            self.assertEqual(mock_func_1.call_count, 0)
            self.assertEqual(mock_func_2.call_count, 1)
            self.assertEqual(mock_func_3.call_count, 0)
            
            mock_func_2.reset_mock()

            # case 3
            
            calculate_value(1, 0, 1, 2)
            
            # check if `func_3` was called once but the `func_1` and `func_2` were not called
            self.assertEqual(mock_func_1.call_count, 0)
            self.assertEqual(mock_func_2.call_count, 0)
            self.assertEqual(mock_func_3.call_count, 1)
        
        
        
