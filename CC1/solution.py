"""
Your Name
Coding Challenge 1 - Sort of Sorted - Solution Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
import copy


def sort_of_sorted(subject):
    '''
    This function returns the longest sublist
    in an unsorted list that is already sorted
    '''
    list_sort_check = []
    list_longest = []
    count = 0
    i = 0
    master_list = []
    while i < len(subject):
        list_sort_check.append(subject[i])

        if list_sort_check == sorted(list_sort_check):
            if len(list_longest) <= len(list_sort_check):
                list_longest = copy.deepcopy(list_sort_check)
                master_list.append(list_longest)
        else:
            list_sort_check = []
            count = count + 1
            i = copy.deepcopy(count)
            continue
        i = i + 1

    return len(list_longest), list_longest
