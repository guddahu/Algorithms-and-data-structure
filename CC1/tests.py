"""
Andrew McDonald
Coding Challenge 1 - Sort of Sorted - Unit Tests
CSE 331 Fall 2020
Professor Sebnem Onsay
"""

import unittest
import string
from CC1.solution import sort_of_sorted


class CC1Tests(unittest.TestCase):

    def test_basic(self):
        """
        Test algorithm on basic, short lists
        """
        subject = ["bravo", "golf", "charlie", "echo", "foxtrot", "alpha", "delta"]
        expected = 3, ["charlie", "echo", "foxtrot"]
        result = sort_of_sorted(subject)
        assert result == expected

        subject = ["let's", "go", "state"]
        expected = 2, ["go", "state"]
        result = sort_of_sorted(subject)
        assert result == expected

        subject = ["on", "the", "banks", "of", "the", "red", "cedar"]
        expected = 3, ["banks", "of", "the"]
        result = sort_of_sorted(subject)
        assert result == expected

        subject = []
        expected = 0, []
        result = sort_of_sorted(subject)
        assert result == expected

    def test_whole(self):
        """
        Test algorithm when entire list should be returned
        """
        subject = ["michigan", "state", "university"]
        expected = 3, ["michigan", "state", "university"]
        result = sort_of_sorted(subject)
        assert result == expected

        subject = list(string.ascii_lowercase)
        expected = 26, list(string.ascii_lowercase)
        result = sort_of_sorted(subject)
        assert result == expected

    def test_multiple(self):
        """
        Test algorithm when multiple sublists of maximal length exist
        """
        subject = ["go", "green", "go", "white"]
        expected = [(2, ["go", "green"]), (2, ["go", "white"])]
        result = sort_of_sorted(subject)
        assert result in expected

        subject = ["michigan", "state", "university", "is", "the", "best", "in", "the", "midwest"]
        expected = [(3, ["michigan", "state", "university"]), (3, ["best", "in", "the"])]
        result = sort_of_sorted(subject)
        assert result in expected

    def test_single(self):
        """
        Test algorithm when maximal length sublist is one string
        """
        subject = ["watch", "the", "points", "keep", "growing"]
        expected = [(1, ["watch"]), (1, ["the"]), (1, ["points"]), (1, ["keep"]), (1, ["growing"])]
        result = sort_of_sorted(subject)
        assert result in expected

        subject = list(reversed(string.ascii_lowercase))
        expected = [(1, [letter]) for letter in string.ascii_lowercase]
        result = sort_of_sorted(subject)
        assert result in expected

    def test_duplicates(self):
        """
        Test algorithm when multiple identical strings are next to one another
        """
        subject = ["let's", "go", "go", "state"]
        expected = 3, ["go", "go", "state"]
        result = sort_of_sorted(subject)
        assert result == expected

        subject = ["msu"] * 10
        expected = 10, ["msu"] * 10
        result = sort_of_sorted(subject)
        assert result == expected

    def test_long(self):
        """
        Test algorithm with long strings as final sanity check
        """
        source = """
                    on the banks of the red cedar
                    theres a school thats known to all
                    its specialty is winning
                    and those spartans play good ball
                    spartan teams are never beaten
                    all through the game theyll fight
                    fight for the only colors
                    green and white
                    go right through for msu
                    watch the points keep growing
                    spartan teams are bound to win
                    theyre fighting with a vim
                    rah rah rah
                    see their team is weakening
                    were going to win this game
                    fight fight rah team fight
                    victory for msu
                    """
        subject = source.split()
        expected = 5, ["rah", "rah", "rah", "see", "their"]
        result = sort_of_sorted(subject)
        assert result == expected

        source = """
                    msu we love thy shadows
                    when twilight silence falls
                    flushing deep and softly paling
                    oer ivy covered halls
                    beneath the pines well gather
                    to give our faith so true
                    sing our love for alma mater
                    and thy praises msu
                    when from these scenes we wander
                    and twilight shadows fade
                    our memory still will linger
                    where light and shadows played
                    in the evening oft well gather
                    and pledge our faith anew
                    sing our love for alma mater
                    and thy praises msu.
                    """
        subject = source.split()
        expected = [(3, ['faith', 'so', 'true']), (3, ['memory', 'still', 'will']), (3, ['evening', 'oft', 'well'])]
        result = sort_of_sorted(subject)
        assert result in expected

        source = """
                    alfa bravo charlie delta echo foxtrot golf hotel india juliett kilo lima mike november
                    oscar papa quebec romeo sierra tango uniform victor whiskey x-ray yankee zulu
                    """
        subject = source.split() * 10
        expected = 26, source.split()
        result = sort_of_sorted(subject)
        assert result == expected

        source = string.ascii_lowercase * 10
        subject = list(source)
        expected = 26, list(string.ascii_lowercase)
        result = sort_of_sorted(subject)
        assert result == expected

        subject = [letter for letter in string.ascii_lowercase * 10 for i in range(10)]
        expected = 260, [letter for letter in string.ascii_lowercase for i in range(10)]
        result = sort_of_sorted(subject)
        assert result == expected


if __name__ == '__main__':
    unittest.main()
