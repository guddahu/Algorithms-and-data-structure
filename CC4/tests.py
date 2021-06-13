"""
Zosha Korzecke
CC4 - Unit Tests
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

import unittest
from solution import Books
from random import sample, seed


class CC4Tests(unittest.TestCase):

    def test_basic(self):
        # Test on a basic group of books
        pile = Books()

        # Tests insert and remove
        pile.insert(3)
        actual = pile.remove()
        expected = 3
        self.assertEqual(actual, expected)

        # Basic test for shortest_book with multiple books
        pile.insert(4)
        pile.insert(6)
        pile.insert(3)
        pile.insert(8)
        actual = pile.shortest_book()
        expected = 3
        self.assertEqual(actual, expected)

        # Tests that shortest_book updates when previous shortest book in pile is removed
        pile.remove()
        pile.remove()
        actual = pile.shortest_book()
        expected = 4
        self.assertEqual(actual, expected)

    def test_empty(self):
        pile = Books()

        # Testing remove on an empty pile
        actual = pile.remove()
        expected = None
        self.assertEqual(actual, expected)

        # Testing shortest_book on an empty pile
        actual = pile.shortest_book()
        expected = None
        self.assertEqual(actual, expected)

    def test_duplicates(self):
        pile = Books()

        # Inserts books of the same size
        pile.insert(4)
        pile.insert(4)
        pile.insert(4)
        pile.insert(3)
        pile.insert(3)
        pile.insert(3)
        pile.insert(2)
        pile.insert(2)
        pile.insert(3)
        pile.insert(1)

        actual = pile.shortest_book()
        expected = 1
        self.assertEqual(actual, expected)

        actual = pile.remove()
        expected = 1
        self.assertEqual(actual, expected)
        actual = pile.shortest_book()
        expected = 2
        self.assertEqual(actual, expected)

        actual = pile.remove()
        expected = 3
        self.assertEqual(actual, expected)
        actual = pile.shortest_book()
        expected = 2
        self.assertEqual(actual, expected)

        pile.remove()
        pile.remove()
        actual = pile.remove()
        expected = 3
        self.assertEqual(actual, expected)
        actual = pile.shortest_book()
        expected = 3
        self.assertEqual(actual, expected)

        pile.remove()
        pile.remove()
        pile.remove()
        pile.remove()
        actual = pile.shortest_book()
        expected = 4
        self.assertEqual(actual, expected)

        pile.remove()
        actual = pile.shortest_book()
        expected = None
        self.assertEqual(actual, expected)

    def test_small_random(self):
        pile = Books()
        seed(331)
        # Tests a small set of randomly generated books
        books = sample(range(0, 10000), 10)

        for i in books:
            pile.insert(i)

        actual = pile.shortest_book()
        expected = min(books)
        self.assertEqual(actual, expected)

        pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:9])
        self.assertEqual(actual, expected)

        pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:8])
        self.assertEqual(actual, expected)

        pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:7])
        self.assertEqual(actual, expected)

        pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:8])
        self.assertEqual(actual, expected)

    def test_large_random(self):
        pile = Books()
        seed(331)
        # Tests a large set of randomly generated books
        books = sample(range(0, 10000), 1000)

        for i in books:
            pile.insert(i)

        actual = pile.shortest_book()
        expected = min(books)
        self.assertEqual(actual, expected)

        for i in range(100):
            pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:900])
        self.assertEqual(actual, expected)

        for i in range(100):
            pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:800])
        self.assertEqual(actual, expected)

        for i in range(100):
            pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:700])
        self.assertEqual(actual, expected)

        for i in range(100):
            pile.remove()

        actual = pile.shortest_book()
        expected = min(books[0:600])
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
