"""
Name: Aditya Raj
CC3 - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List


def find_missing_value(sequence):
    """
    Given a List of sorted integers from range 0 to n where there is an
    integer missing in between or at the end . Return the missing integer
    form the sorted list

    :param sequence: List[int] list sorted integers in the range 0 to n
    :return: int result where result is the missing integer from the list

    """
    start = 0
    end = len(sequence) - 1
    if sequence == []:
        return 0

    if sequence[start] != 0:
        return 0

    def find_missing_value_recursive(start, end):
        if start > end:
            return -1

        middle_check = (start + end) // 2
        if sequence[middle_check] != middle_check and sequence[middle_check -1] == middle_check - 1:
            return middle_check
        elif sequence[middle_check] != middle_check:
            return find_missing_value_recursive(start, middle_check - 1)
        else:
            return find_missing_value_recursive(middle_check + 1, end)
    result = find_missing_value_recursive(start, end)
    if result is -1:
        return len(sequence)
    return result
