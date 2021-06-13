import unittest
import types
from CC6.solution import alien_communicator


class TestCodingChallenge6(unittest.TestCase):

    def test_zero(self):
        """
        Tests input 0, and checks value 0 on other inputs
        """
        # -- Test input 0 --
        # create generator
        binary = alien_communicator(0)
        self.assertIsInstance(binary, types.GeneratorType)

        # test #0
        expected_binary = bin(0)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
        self.assertEqual(expected_binary, next(binary, None))

        # test generator stops
        self.assertIsNone(next(binary, None))

        # -- Output 0, Input 5 --
        # create generator
        binary = alien_communicator(5)
        self.assertIsInstance(binary, types.GeneratorType)

        # test #0
        expected_binary = bin(0)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
        self.assertEqual(expected_binary, next(binary, None))

        # -- Output 0, Input 6 --
        # create generator
        binary = alien_communicator(6)
        self.assertIsInstance(binary, types.GeneratorType)

        # test #0
        expected_binary = bin(0)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
        self.assertEqual(expected_binary, next(binary, None))

    def test_invalid_input(self):
        """
        Tests inputs that should be ignored
        """
        # added a negative test
        n = -1
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = "5"
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = ""
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = "0"
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = "12"
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = "13"
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = "331 is fun"
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = True
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = False
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = []
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = ()
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = {}
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

        n = set()
        binary = alien_communicator(n)
        self.assertIsInstance(binary, types.GeneratorType)
        self.assertIsNone(next(binary, None))

    def test_basic(self):
        """
        Tests 0 to 10, then None
        """
        # create generator
        binary = alien_communicator(7)
        self.assertIsInstance(binary, types.GeneratorType)

        # test #0
        # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
        expected_binary = bin(0)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #1
        expected_binary = bin(1)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #2
        expected_binary = bin(2)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #3
        expected_binary = bin(3)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #4
        expected_binary = bin(4)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #5
        expected_binary = bin(5)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #6
        expected_binary = bin(6)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test #7
        expected_binary = bin(7)[2:]
        self.assertEqual(expected_binary, next(binary, None))

        # test to ensure does not continue past n
        self.assertIsNone(next(binary, None))

    def test_even_numbers_and_inputs(self):
        """
        Tests even numbers and even inputs
        """

        # -- Tests Even Numbers --
        # Create generator
        binary = alien_communicator(50)
        self.assertIsInstance(binary, types.GeneratorType)

        next(binary, None)  # skip 0
        next(binary, None)  # skip 1

        # Check only even numbers in range : 2, 4, 6..
        for i in range(2, 51, 2):  # n + 1 because generator generates up to n
            expected_binary = bin(i)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
            self.assertEqual(expected_binary, next(binary, None))
            next(binary, None)  # skip to next even

        # test to ensure does not continue past n
        self.assertIsNone(next(binary, None))

        # -- Tests Even Inputs --
        for n in range(2, 51, 2):  # EX: 2, 4, 6..
            binary = alien_communicator(n)
            self.assertIsInstance(binary, types.GeneratorType)

            # Check all numbers in range
            for i in range(n + 1):  # +1 because generator generates up to n
                expected_binary = bin(i)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
                self.assertEqual(expected_binary, next(binary, None))

            # test to ensure does not continue past n
            self.assertIsNone(next(binary, None))

    def test_odd_numbers_and_inputs(self):
        """
        Tests odd inputs
        """

        # -- Tests Odd Numbers --
        # Create generator
        binary = alien_communicator(50)
        self.assertIsInstance(binary, types.GeneratorType)

        next(binary, None)  # skip 0

        # Check only odd numbers in range: 1, 3, 5..
        for i in range(1, 51, 2):  # n + 1 because generator generates up to n
            expected_binary = bin(i)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
            self.assertEqual(expected_binary, next(binary, None))
            next(binary, None)  # skip to next odd

        # test to ensure does not continue past n
        self.assertIsNone(next(binary, None))

        # -- Tests Odd Inputs --
        for n in range(2, 51, 2):  # EX: 1, 3, 5..
            # Create generator
            binary = alien_communicator(n)
            self.assertIsInstance(binary, types.GeneratorType)

            # Check all numbers in range
            for i in range(n + 1):  # n + 1 because generator generates up to n
                expected_binary = bin(i)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
                self.assertEqual(expected_binary, next(binary, None))

            # test to ensure does not continue past n
            self.assertIsNone(next(binary, None))

    def test_large_input(self):
        """
        Tests large inputs and all values generated
        """
        for n in range(1, 1001):
            # Create generator
            binary = alien_communicator(n)
            self.assertIsInstance(binary, types.GeneratorType)

            for i in range(n + 1):  # n + 1 because generator generates up to n
                expected_binary = bin(i)[2:]  # Ex: bin(5)='0b101' -> bin(5)[2:]='101'
                self.assertEqual(expected_binary, next(binary, None))

            # test to ensure does not continue past n
            self.assertIsNone(next(binary, None))


if __name__ == '__main__':
    unittest.main()