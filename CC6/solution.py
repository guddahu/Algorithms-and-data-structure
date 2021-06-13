"""
CC6 - It's As Easy As 01-10-11
Name: Aditya Raj
"""

from typing import Generator, Any


class Node:
    """
    Node Class
    :value: stored value
    :next: reference to next node
    """

    def __init__(self, value) -> None:
        """
        Initializes the Node class
        """
        self.value: str = value
        self.next: Node = None

    def __str__(self) -> str:
        """
        Returns string representation of a Node
        """

        return self.value


class Queue:
    """
    Queue Class
    :first: reference to first node in the queue
    :last: reference to last node in the queue
    """

    def __init__(self) -> None:
        """
        Initializes the Queue class
        """
        self.first: Node = None
        self.last: Node = None

    def __str__(self) -> str:
        final = 'front - '
        current = self.first
        while current is not None:
            final += str(current) + ' - '
            current = current.next
        final += "last"
        return final

    def insert(self, value: str) -> None:
        """
        inserts the string val into queue
        :param value: String to be inserted
        :return: NOne
        """
        newest = Node(value)  # node will be new tail node
        if self.first is None:
            self.first = newest  # special case: previously empty
        else:
            self.last.next = newest
        self.last = newest  # update reference to tail node

    def pop(self) -> str:
        """
        pop the last element inserted
        :return: the string that was popped
        """
        if self.first is None:
            return
        answer = self.first.value
        self.first = self.first.next

        if self.first is None:  # special case as queue is empty
            self.last = None  # removed head had been the tail
        return answer


def alien_communicator(n: Any) -> Generator[str, None, None]:
    """
    returns a generator type with binary number starting from 0
    :param n: range of binary numbers
    :return: string for each binary number
    """
    if not isinstance(n, int) or isinstance(n, bool):
        return

    if n < 0:
        return
    if n == 0:
        yield '0'
        return

    queue = Queue()
    queue.insert('1')

    yield '0'

    while n > 0:
        string1 = queue.pop()
        yield string1
        string2 = string1

        queue.insert(string1 + "0")

        queue.insert(string2 + "1")

        n -= 1
