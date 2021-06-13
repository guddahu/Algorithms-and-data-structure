"""
Name:
CC3 - Unit Tests
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

import unittest
from solution import find_missing_value

class CC3Tests(unittest.TestCase):

    def test_basic(self):
        # Test on even size list
        sequence = [0, 1, 3, 4, 5, 6]
        assert find_missing_value(sequence) == 2

        # Test on odd size list
        sequence = [0, 1, 3, 4, 5]
        assert find_missing_value(sequence) == 2


    def test_missing_last(self):
        # Test on even size list missing last
        sequence = [0, 1, 2, 3]
        assert find_missing_value(sequence) == 4

        # Test on odd size list missing last
        sequence = [0, 1, 2, 3, 4]
        assert find_missing_value(sequence) == 5

    def test_small_sequence(self):
        # Test on an empty list
        assert find_missing_value([]) == 0

        # Test on size one
        sequence = [0]
        assert find_missing_value(sequence) == 1

        sequence = [1]
        assert find_missing_value(sequence) == 0

        # Test on size two
        sequence = [0, 1]
        assert find_missing_value(sequence) == 2

        sequence = [0, 2]
        assert find_missing_value(sequence) == 1

        sequence = [1, 2]
        assert find_missing_value(sequence) == 0

    def test_large_sequence(self):
        # Test large sequence
        sequence = [x for x in range(1001)]
        for i in range(1001):
            temp_sequence = sequence.copy()
            temp_sequence.remove(i)
            assert find_missing_value(temp_sequence) == i

if __name__ == '__main__':
    unittest.main()
