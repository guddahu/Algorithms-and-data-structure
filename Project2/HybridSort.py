"""
Name: Aditya Raj
Project 2 - Hybrid Sorting - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Any, Dict


def hybrid_sort(data: List[Any], threshold: int) -> None:
    """
    This function is called for doing merge sort with
    provided threshold.The provided threshold will then switch to the
    insertion sort
    :param data : holds the list to be sorted
    :param threshold : list length for toggle the insertion sort
    :returns : None
    """
    merge_sort(data, threshold)


def inversions_count(data: List[Any]) -> int:
    """
    Calls mergesort with threshold 0 and counts the
    number of inversions in the sort.
    :param data : holds the list to be sorted
    :returns int : the number of inversions
    """
    return merge_sort(data, 0)


def merge(list1, list2, final_list, threshold, toggle):
    """
    Helper function for merge Sort to merge two
    arrays into one and sort simultaneously

    :param list1: first half of the list
    :param list2: second half of the list
    :param final_list: the main list to merge it in
    :param threshold: count the number of inversions
    :param toggle: check if threshold is not zero
    :return: returns the innversion count
    """
    i = j = 0
    while i + j < len(final_list):
        if j == len(list2) or (i < len(list1) and list1[i] <= list2[j]):
            final_list[i + j] = list1[i]
            i += 1

        else:
            final_list[i + j] = list2[j]
            if toggle == 0:
                threshold += (len(list1) - i)
            j += 1

    return threshold


def merge_sort(data: List[Any], threshold: int = 0) -> int:
    """
    This function uses the Merge Sort algorithm to sort a list
    and also uses a toggle value to use insertion sort at a particular
    list length
    :param data: the list to be sorted
    :param threshold: threshold for using insertion sort
    :return: the number of inversions if required or 0
    """
    count1 = count2 = count3 = 0
    length = len(data)
    if length < 2:
        return 0
    if len(data) <= threshold and threshold != 0:
        insertion_sort(data)

    else:

        mid = length // 2
        list1 = data[0:mid]
        list2 = data[mid:length]

        count1 = merge_sort(list1, count3)
        count2 = merge_sort(list2, count3)

        count3 = merge(list1, list2, data, count3, threshold)
        if threshold == 0:
            return count3 + count1 + count2  # Adds the number of inversions
    return 0


def insertion_sort(data: List[Any]) -> None:
    """
    This function uses the insertion sort algorithm to
    sort a list
    :param data: the list to be sorted
    :returns : none
    """
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = key


def find_match(user_interests: List[str], candidate_interests: Dict[str, List]) -> str:
    """
    This function matches two users interest based on the ranking
    of their interests provided in a list. And uses the inversion count to
    deduce it.
    :param user_interests: list ranked for user interests
    :param candidate_interests: dict of different candidates with list of their interests
    :return: name of the person with highest matched preferences
    """
    maximum = 10000
    dict1 = {}
    dict2 = {}
    key1 = ""
    for i in range(len(user_interests)):
        dict1[user_interests[i]] = i + 1

    for keys, values in candidate_interests.items():
        list2 = []
        for i in values:
            list2.append(dict1[i])
        dict2[keys] = list2

    for key, value in dict2.items():
        count = inversions_count(value)
        if count < maximum:
            maximum = count
            key1 = key
    return key1
