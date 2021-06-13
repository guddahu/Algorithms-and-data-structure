"""
Name:
Coding Challenge 7 - Lonely Rolling Star - Solution Code
CSE 331 Fall 2020
Professor Sebnem Onsay
"""
from typing import List, Tuple


class Item:
    """
    A class that will store an item's name and category
    """

    def __init__(self, item_name: str, item_category: str):
        self.name = item_name
        self.category = item_category

    def __repr__(self):
        return "Item('" + self.name + "','" + self.category + "')"

    def get_name(self) -> str:
        """
        returns the strng representing the item's name
        :return: Item name string
        """
        return self.name

    def get_category(self) -> str:
        """
        Returns the string representation of the item's category
        :return: Item category string
        """
        return self.category


class RoboKingOfAllCosmos:

    def __init__(self):
        self.mem = {}
        self.categories = {}
        # put your scoring container here

    def construct_score_book(self, items_and_size: List[Tuple[str, float]]) -> None:
        """
        constructs the memory for RoboKing
        :param items_and_size: the list from which memory will be stored
        :return: None
        """
        for i in items_and_size:
            self.mem[i[0]] = i[1]

    def get_score_book(self) -> List[Tuple[str, float]]:
        """
        returns the memories of Roboking stored in mem
        :return: the score book of RoboKing
        """
        final = []

        for keys in self.mem:
            final.append((keys, self.mem[keys]))
        return final

    def judge_katamari(self, katamari_contents: List[Item]) -> Tuple[float, List[Tuple[str, int]], List[str]]:
        """
        Judges the katamari and keeps track of cousins ans categories and ranks to 3
        :param katamari_contents: contents to analyze on
        :return:
        """
        cousins = []

        size = 0.0
        for i in katamari_contents:
            if i.get_category() == "cousins":
                cousins.append(i.get_name())

            else:
                size += self.mem[i.get_name()]

            if i.get_category() in self.categories:
                self.categories[i.get_category()] += 1
            else:
                self.categories[i.get_category()] = 1

        sorted_cat = sorted(self.categories.items(), key=
        lambda kv: (kv[1], kv[0]), reverse=True)

        return round(size, 2), sorted_cat[0:3], cousins
