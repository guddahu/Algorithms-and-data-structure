"""
Name:
CC4 - Starter Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

from __future__ import annotations  # allow self-reference

class Books:
    """
    Storing book pages in terms of page length in Stacks
    The underlying structure is List
    """
    def __init__(self):
        """
        Creates empty list and a min integer to store the minimum element
        """
        self.List = []
        self.min = None

    def insert(self, num: int):
        """
        Inserts the element at the top of the element with appropriate
        error checks
        :param num: The number to be inserted
        :return: None
        """
        if len(self.List) == 0:
            self.min = num
            self.List.append(num)              #inserting the first element
        elif num > self.min:
            self.List.append(num)                #append the element if not minimum
        else:
            self.List.append(2*num - self.min)   # 'encode' used from piazza the element to find the min element
            self.min = num                        # when popping.

    def remove(self):
        """
        Remove the element from the stack. And also decoding the element
        :return: the elemented popped ,if empty then None
        """
        init_element = None
        if len(self.List) != 0:
            init_element = self.List.pop()                  #pop if not empty
            if init_element < self.min:
                self.min = 2 * self.min - init_element       #if an encoded element is encountered
                init_element = (init_element + self.min)/2                # removing the encoding
        if len(self.List) == 0:
            self.min = None
        return init_element
    def shortest_book(self):
        """
        return the shortest element in the stack that is already stored in min
        :return: the minimum element
        """
        return self.min                          #return min element
