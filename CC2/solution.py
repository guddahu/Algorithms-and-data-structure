"""
Aditya raj
Coding Challenge 2 - Drop It Liae It's Hot - Solution
CSE 331 Fall 2020
Professor Sebnem Onsay
"""


def firefighter(grid, sq_size):
    """
    Given an n x n 2D list of 0's and 1's and an integer a, determine the greatest number of 1's
    that can be covered by a square of size a x a. Return a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    :param grid: [list[list[int]]] a square 2D list of 0, 1 integers
    :param k: [int] the size of the square placed to cover 1's
    :return: [tuple[int, int, int]] a tuple (a, b, c) where
        a = number of 1's this optimal k x k square covers
        b = the row of the top left corner of this square
        c = the col of the top left corner of this square
    """
    if grid == [[]]:
        return 0, 0, 0
    len_grid = len(grid)
    sum_grid = 0
    max_sum_grid = 0
    final_tuple = 0, 0, 0
    for i in range(len_grid):
        for j in range(len_grid):
            for k in range(sq_size):
                if i+sq_size-1 >= len_grid or j+sq_size-1 >= len_grid:
                    break
                for last in range(sq_size):
                    if i+last >= len_grid or j+k >= len_grid:
                        break
                    sum_grid = sum_grid + grid[i+last][j+k]

            if max_sum_grid < sum_grid:
                if sum_grid == sq_size*sq_size:
                    return (sum_grid, i, j)
                max_sum_grid = sum_grid
                final_tuple = (max_sum_grid, i, j)
            sum_grid = 0

    return final_tuple
