"""
Your Name
Project 4 - Tries
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

from __future__ import annotations
from typing import Tuple, Dict, List


class TrieNode:
    """
    Implementation of a trie node.
    """

    # DO NOT MODIFY

    __slots__ = "children", "is_end"

    def __init__(self, arr_size: int = 26) -> None:
        """
        Constructs a TrieNode with arr_size slots for child nodes.
        :param arr_size: Number of slots to allocate for child nodes.
        :return: None
        """
        self.children = [None] * arr_size
        self.is_end = 0

    def __str__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        if self.empty():
            return "..."
        children = self.children  # to shorten proceeding line
        return str({chr(i + ord("a")) + "*"*min(children[i].is_end, 1): children[i] for i in range(26) if children[i]})

    def __repr__(self) -> str:
        """
        Represents a TrieNode as a string.
        :return: String representation of a TrieNode.
        """
        return self.__str__()

    def __eq__(self, other: TrieNode) -> bool:
        """
        Compares two TrieNodes for equality.
        :return: True if two TrieNodes are equal, else False
        """
        if not other or self.is_end != other.is_end:
            return False
        return self.children == other.children

    # Implement Below

    def empty(self) -> bool:
        """
        Checks if a trienode is empty
        :return: True if trienode is empty
        """
        for i in range(26):
            if self.children[i] is not None:
                return False
        return True

    @staticmethod
    def _get_index(char: str) -> int:
        """
        gets the index in int from char
        :param char: char whose int index is needed
        :return: int that is the char in int (ASCII)
        """
        return ord(char.lower()) - 97


    def get_child(self, char: str) -> TrieNode:
        """
        gets the child of a Trie node from the index of char
        :param char: char whose index is selected from child
        :return: Trienode if index is not None
        """
        if self.empty():
            return None

        return self.children[self._get_index(char)]

    def set_child(self, char: str) -> None:
        """
        sets the child of a Trie node from the index of char
        :param char: char whose index is to be set from child
        :return: None
        """

        self.children[self._get_index(char)] = TrieNode()

    def delete_child(self, char: str) -> None:
        """
        deletes the child of a Trie node from the index of char
        :param char: char whose index is to be deleted from child if not None
        :return: None
        """
        self.children[self._get_index(char)] = None


class Trie:
    """
    Implementation of a trie.
    """

    # DO NOT MODIFY

    __slots__ = "root", "unique", "size"

    def __init__(self) -> None:
        """
        Constructs an empty Trie.
        :return: None.
        """
        self.root = TrieNode()
        self.unique = 0
        self.size = 0

    def __str__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return "Trie Visual:\n" + str(self.root)

    def __repr__(self) -> str:
        """
        Represents a Trie as a string.
        :return: String representation of a Trie.
        """
        return self.__str__()

    def __eq__(self, other: Trie) -> bool:
        """
        Compares two Tries for equality.
        :return: True if two Tries are equal, else False
        """
        return self.root == other.root

    # Implement Below

    def add(self, word: str) -> int:
        """
        Adds a word to the Trie
        :param word: string word to be added
        :return: total count of that word int the trie
        """

        def add_inner(node: TrieNode, index: int) -> int:
            if node.get_child(word[index]) is None:
                node.set_child(word[index])

            if index == len(word) - 1:
                if node.get_child(word[index]).is_end == 0:
                    self.unique += 1

                node.get_child(word[index]).is_end += 1
                return node.get_child(word[index]).is_end
            return add_inner(node.get_child(word[index]), index + 1)

        curr_node = self.root
        self.size += 1

        count = add_inner(curr_node, 0)

        return count

    def search(self, word: str) -> int:
        """
        search for word in the trie
        :param word: word to be searched
        :return: count of word in Trie if Found else 0
        """
        if word == "":
            return True

        def search_inner(node: TrieNode, index: int) -> int:
            if node.get_child(word[index]) is None:
                return 0

            if index == len(word) - 1:
                return node.get_child(word[index]).is_end
            return search_inner(node.get_child(word[index]), index + 1)

        curr_node = self.root
        return search_inner(curr_node, 0)

    def delete(self, word: str) -> int:
        """
        deletes word from trie if found
        :param word: word to be seleted
        :return: count of words deleted
        """
        def delete_inner(node: TrieNode, index: int) -> Tuple[int, bool]:
            if node.get_child(word[index]) is None:
                return 0, False

            if index == len(word) - 1:
                is_end = node.get_child(word[index]).is_end
                if is_end > 0:
                    self.unique -= 1
                    self.size -= is_end
                node.get_child(word[index]).is_end = 0

                if node.get_child(word[index]).empty():
                    node.delete_child(word[index])
                return is_end, node.empty() and node.is_end == 0

            if node.get_child(word[index]).empty():
                node.get_child(word[index]).delete_child(word[index])

            is_end1, bool1 = delete_inner(node.get_child(word[index]), index + 1)

            if bool1:
                node.delete_child(word[index])
            return is_end1, node.empty()



        curr_node = self.root
        is_end, bool1 = delete_inner(curr_node, 0)
        return is_end

    def __len__(self) -> int:
        """
        gets the number of words of trie
        :return: int of number of words in Trie
        """
        return self.size

    def __contains__(self, word: str) -> bool:
        """
        if a word is present in Trie
        :param word: word to be searched in trie
        :return: returns bool if the word is present
        """
        return self.search(word) > 0

    def empty(self) -> bool:
        """
        checks if a trie is empty or not
        :return: bool if trie is empty
        """
        if self.size > 0:
            return False
        return True

    def get_vocabulary(self, prefix: str = "") -> Dict[str, int]:
        """
        gets the words form trie that start with prefix in the trie
        :param prefix: prefix of the word
        :return: returns a dict of the words with prefix and their count
        """
        main_dict = {}
        def get_vocabulary_inner(node, suffix):

            if node.is_end > 0:
                main_dict[prefix + suffix] = node.is_end

            for i in range(26):
                if node.get_child(chr(i + 97)) is not None:
                    get_vocabulary_inner(node.get_child(chr(i + 97)), suffix + chr(i + 97))

        node = self.root
        if self.empty():
            return main_dict
        for i in prefix:
            if node.get_child(i) is None:
                return main_dict
            node = node.get_child(i)

        get_vocabulary_inner(node, "")
        return main_dict

    def autocomplete(self, word: str) -> Dict[str, int]:
        """
        gets the words form trie that match word in the trie
        :param word: template of word with . or letters
        :return: returns a dict of the words with prefix and their count
        """
        main_dict = {}

        def autocomplete_inner(node, prefix, index):
            if node.is_end > 0 and len(prefix) == len(word):
                main_dict[prefix] = node.is_end
                return
            if index > len(word):
                return
            for i in range(26):
                if node.get_child(chr(i + 97)) is not None and index < len(word) and word[index] == '.':
                    autocomplete_inner(node.get_child(chr(i + 97)), prefix + chr(i + 97), index+1)
                elif index < len(word) and word[index] != '.' and node.get_child(word[index]) is not None:
                    autocomplete_inner(node.get_child(word[index]), prefix + word[index], index+1)


        node = self.root
        if self.empty():
            return main_dict
        temp_word = ""
        index = 0
        for i in word:
            if i == '.':
                break
            if node.get_child(i) is None:
                return main_dict
            node = node.get_child(i)
            temp_word += i
            index += 1

        autocomplete_inner(node, temp_word, index)
        return main_dict


class TrieClassifier:
    """
    Implementation of a trie-based text classifier.
    """

    # DO NOT MODIFY

    __slots__ = "tries"

    def __init__(self, classes: List[str]) -> None:
        """
        Constructs a TrieClassifier with specified classes.
        :param classes: List of possible class labels of training and testing data.
        :return: None.
        """
        self.tries = {}
        for cls in classes:
            self.tries[cls] = Trie()

    @staticmethod
    def accuracy(labels: List[str], predictions: List[str]) -> float:
        """
        Computes the proportion of predictions that match labels.
        :param labels: List of strings corresponding to correct class labels.
        :param predictions: List of strings corresponding to predicted class labels.
        :return: Float proportion of correct labels.
        """
        correct = sum([1 if label == prediction else 0 for label, prediction in zip(labels, predictions)])
        return correct / len(labels)

    # Implement Below

    def fit(self, class_strings: Dict[str, List[str]]) -> None:
        """
        adds the data from class_strings for the fit in self.tries
        :param class_strings: dict for the fit
        :return: void (none)
        """
        trie = Trie()
        for k in class_strings.keys():
            for i in class_strings[k]:
                for j in i.split():
                    trie.add(j)
            self.tries[k] = trie
            trie = Trie()


    def predict(self, strings: List[str]) -> List[str]:
        """
        Predicts the class for a tweet from the data in self.tries
        :param strings: list of strings to classify
        :return: list of class in order with the sentences
        """
        list1 = []
        dict1 = {}
        for k in self.tries.keys():
            dict1[k] = 0

        for i in strings:
            for j in i.split():
                for k in self.tries.keys():
                    dict1[k] += self.tries[k].search(j)

            max1 = -1
            str_class = ""
            for k in dict1:
                if dict1[k]/len(self.tries[k]) > max1:
                    max1 = dict1[k]/len(self.tries[k])
                    str_class = k
                dict1[k] = 0
            list1.append(str_class)

        return list1
