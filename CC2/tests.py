"""
Andrew McDonald
Coding Challenge 2 - Drop It Like It's Hot - Unit Tests
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

import unittest
from solution import firefighter


class CC2Tests(unittest.TestCase):

    def test_basic(self):
        """
        Test algorithm on basic cases
        """
        grid = [[0, 0, 0],
                [0, 1, 1],
                [0, 1, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (3, 1, 1)
        assert result == expected

        grid = [[0, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 0, 2)
        assert result == expected

        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 1, 1]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 2, 2)
        assert result == expected

        grid = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [1, 1, 0, 0],
                [1, 1, 0, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 2, 0)
        assert result == expected

        grid = [[1, 1, 0, 0],
                [1, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 0, 0)
        assert result == expected

        grid = [[0, 0, 0, 0, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0]]
        k = 3
        result = firefighter(grid, k)
        expected = (9, 1, 1)
        assert result == expected

    def test_all_none(self):
        """
        Test algorithm on cases where optimal square covers entire grid or no spaces
        """
        grid = [[0, 1, 0],
                [1, 0, 1],
                [1, 1, 0]]
        k = 3
        result = firefighter(grid, k)
        expected = (5, 0, 0)
        assert result == expected

        grid = [[0, 1, 0],
                [1, 0, 1],
                [1, 1, 0]]
        k = 0
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

        grid = [[]]
        k = 1
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

    def test_multiple(self):
        """
        Test algorithm on cases where multiple optimal placements exist
        """
        grid = [[0, 0, 0],
                [0, 1, 1],
                [0, 1, 0]]
        k = 1
        result = firefighter(grid, k)
        expected = (1, 1, 1)
        assert result == expected

        grid = [[1, 0, 0],
                [0, 1, 0],
                [0, 0, 1]]
        k = 2
        result = firefighter(grid, k)
        expected = (2, 0, 0)
        assert result == expected

        grid = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

        grid = [[0, 0, 0],
                [0, 1, 0],
                [0, 0, 0]]
        k = 2
        result = firefighter(grid, k)
        expected = (1, 0, 0)
        assert result == expected

        grid = [[0, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 2, 0)
        assert result == expected

        grid = [[0, 0, 0, 0],
                [1, 0, 0, 1],
                [1, 1, 1, 1],
                [1, 1, 1, 1]]
        k = 3
        result = firefighter(grid, k)
        expected = (7, 1, 0)
        assert result == expected

        grid = [[0, 1, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 1, 1, 1]]
        k = 2
        result = firefighter(grid, k)
        expected = (4, 0, 2)
        assert result == expected

        grid = [[0, 1, 1, 1],
                [0, 0, 1, 1],
                [0, 0, 1, 1],
                [0, 1, 1, 1]]
        k = 3
        result = firefighter(grid, k)
        expected = (7, 0, 1)
        assert result == expected

    def test_long(self):
        """
        Test algorithm on large inputs
        """
        size = 100

        # empty grid
        grid = [[0 for i in range(size)] for j in range(size)]

        k = 2
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

        k = 10
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

        k = size
        result = firefighter(grid, k)
        expected = (0, 0, 0)
        assert result == expected

        # single point in grid
        grid[size // 2][size // 2] = 1

        k = 2
        result = firefighter(grid, k)
        expected = (1, size // 2 - 1, size // 2 - 1)
        assert result == expected

        k = 10
        result = firefighter(grid, k)
        expected = (1, size // 2 - 9, size // 2 - 9)
        assert result == expected

        k = size
        result = firefighter(grid, k)
        expected = (1, 0, 0)
        assert result == expected

        # four points in grid
        grid[size // 2][size // 2] = 1
        grid[size // 2 + 1][size // 2] = 1
        grid[size // 2][size // 2 + 1] = 1
        grid[size // 2 + 1][size // 2 + 1] = 1

        k = 2
        result = firefighter(grid, k)
        expected = (4, size // 2, size // 2)
        assert result == expected

        k = 10
        result = firefighter(grid, k)
        expected = (4, size // 2 - 8, size // 2 - 8)
        assert result == expected

        k = size
        result = firefighter(grid, k)
        expected = (4, 0, 0)
        assert result == expected


if __name__ == '__main__':
    unittest.main()
