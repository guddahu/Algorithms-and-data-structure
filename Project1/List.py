"""
PROJECT 1 - Doubly Linked List + Recursion
Name:
"""

from __future__ import annotations  # allow self-reference
from typing import TypeVar, Generic, Callable  # function type
from Project1.Node import DoublyLinkedListNode as Node

T = TypeVar("T")


class List:
    """
    Adaptation of the C++ List implementation where its underlying
    structure is a cyclic Doubly Linked List
    """

    def __init__(self, num: int = None, val: Generic[T] = None, container: list = None) -> None:
        """
        Creates root node and sets its prev and next member variable to itself
        Assigns list with param values given
        :param num: count of val occurrences
        :param val: value to be stored in Node
        :param container: contains elements used in assign
        """
        self.node = Node(None)
        self.node.prev = self.node.next = self.node

        if num or container:
            self.assign(num, val, container)

    def __repr__(self) -> str:
        """
        :return: Represents the list as a string utilizing __str__
        """
        return self.__str__()

    def __eq__(self, other: List) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        """
        def is_equal(node1: Node, node2: Node) -> bool:
            if node1 is self.node and node2 is other.node:
                return True
            if node1 is self.node or node2 is other.node or node1 != node2\
                    or node1.prev != node2.prev:
                return False
            return is_equal(node1.next, node2.next)
        return is_equal(self.node.next, other.node.next)

    def assign(self, num: int = None, val: Generic[T] = None, container: list = None):
        """
        Populates self with nodes using the given parameters
        :param num: represents the number of occurrences of val to assign to list
        :param val: value to have n occurrences
        :param container: used to generate nodes with its contents
        """
        self.clear()
        node = self.node

        if container:
            for item in container:
                node.next = Node(item, prev=node)
                node = node.next
        elif num:
            for _ in range(num):
                node.next = Node(val, prev=node)
                node = node.next

        node.next, self.node.prev = self.node, node

    def clear(self) -> None:
        """
        Resets list by reassigning root nodes' references to itself
        """
        self.node.prev = self.node.next = self.node

    # Implement below - Do not modify function signatures

    def empty(self) -> bool:
        """
        :return: if List contains any additional nodes other than the root node, False else True
        """

        if self.node.prev is self.node and self.node.next is self.node:  # checks if list is empty
            return True

        return False

    def front(self) -> Node:
        """
        :return: first node in the list or root node if empty
        """
        if self.empty():                        # checks if empty
            return self.node

        return self.node.next                   # returns front node

    def back(self) -> Node:
        """
        :return: last node in the list or root node if empty
        """
        if self.empty():                        # checks if empty
            return self.node

        return self.node.prev                   # returns back node

    def swap(self, other: List) -> None:
        """
        :param other: List to swap contents
        """
        temp = self.node                     #swaps two nodes
        self.node = other.node
        other.node = temp

    def __str__(self) -> str:
        """
        RECURSIVE
        :return: string representation of linked list
        """

        def to_string(node, final=" "):                   # recursive function to print the list
            if node.next.val is None:
                return ""

            if node.next.next.val is not None:
                final = str(final) + str(node.next.val) + str(" <->" + to_string(node.next))
            else:
                final = str(final) + str(node.next.val) + str(to_string(node.next))
            return final

        str1 = to_string(self.node, "")
        return str1

    def size(self) -> int:
        """
        RECURSIVE
        :return: size of list or number of nodes not including the root node
        """
        def size_list(node, count=0) -> int: #recursive function to return the size
            if node.next is self.node:
                return 0
            count = count + 1 + size_list(node.next)

            return count

        count = size_list(self.node)
        return count

    def insert(self, position: Node, val: Generic[T], num: int = 1) -> Node:
        """
        RECURSIVE
        Places node before given position with a value of val
        When num is given, insert num occurrences of node
        :param position: Node index to insert new node before
        :param val: value to insert
        :param num: number of insertions of val at position index
        :return: node that points to the first of the newly inserted nodes
        """
        def insert_node(position, num, val):          #recursive function to insert nodes of value val
            if num == 0:
                return
            node1 = Node(val)
            temp = position.prev
            node1.next = position
            position.prev = node1

            temp.next = node1
            node1.prev = temp
            insert_node(node1, num-1, val)


        return insert_node(position, num, val)


    def erase(self, first: Node, last: Node = None) -> Node:
        """
        Erases node or nodes in list from first to, but not including last: [first, last)
        When last is not given, erase only first node
        :param first: position to start erasing (inclusive)
        :param last: position to end erasing (exclusive)
        :return: node that followed the last node erased
        """
        if first is self.node or first is None: #checks for empty
            return first
        if last is self.node:                   #checks if last is base node
            prev_node = first.prev
            prev_node.next = last
            last.prev = prev_node
            return last
        if last is None:                        #checks if last is None
            next_node = first.next
            prev_node = first.prev

            prev_node.next = next_node
            next_node.prev = prev_node
            return next_node
        else:                             #otherwise remove nodes til last
            prev_node = first.prev
            prev_node.next = last
            last.prev = prev_node
            return last


    def push_front(self, val: Generic[T]) -> None:
        """
        Inserts new Node with value of val in the front of the list
        :param val: value of new Node
        """
        first_node = self.node.next

        self.node.next = Node(val)
        latest_first = self.node.next

        latest_first.prev = self.node         #pushes the node to the front
        latest_first.next = first_node
        first_node.prev = latest_first        #rearranges the list

    def push_back(self, val: Generic[T]) -> None:
        """
        Inserts new Node with value of val in the back of the list
        :param val: value of new Node
        """
        last_node = self.node.prev
        self.node.prev = Node(val)             #pushes the node to the back
        latest_first = self.node.prev

        latest_first.next = self.node           #rearranges the list
        latest_first.prev = last_node
        last_node.next = latest_first

    def pop_front(self) -> None:
        """
        Erases Node in the front of the list
        """
        erased = self.node.next
        self.node.next = erased.next
        erased.next.prev = self.node                 #pops the front node

    def pop_back(self) -> None:
        """
        Erases Node in the back of the list
        """
        erased = self.node.prev
        self.node.prev = erased.prev
        erased.prev.next = self.node                 #pops the back node

    def remove(self, val: Generic[T]) -> None:
        """
        RECURSIVE
        Removes all nodes containing a value of val
        :param val: value to remove
        """
        def remove_node(node: Node) -> Node:           #recursive function
            if node is self.node:
                return node
            if node.val == val:                        #removes all nodes with value val
                next_node = node.next
                prev_node = node.prev

                prev_node.next = next_node
                next_node.prev = prev_node
            remove_node(node.next)

        remove_node(self.node.next)

    def remove_if(self, pred: Callable[[T], bool]) -> None:
        """
        RECURSIVE
        Removes all Nodes with pred returning True
        :param pred: predicate function that returns a boolean
        """
        def remove_node_if(node: Node) -> Node:      #recursive func to remove nodes

            if node is self.node:
                return node
            if pred(node.val):                       #checks if the prediction is true
                next_node = node.next
                prev_node = node.prev

                prev_node.next = next_node
                next_node.prev = prev_node

            remove_node_if(node.next)
        remove_node_if(self.node.next)

    def reverse(self) -> None:
        """
        RECURSIVE
        Reverses linked list in place
        """
        def reverse_list(node: Node) -> None: #recursive function to reverse the list
            temp = node.prev
            node.prev = node.next
            node.next = temp
            if node.prev is self.node:
                return None
            reverse_list(node.prev)

        reverse_list(self.node)
    def unique(self) -> None:
        """
        RECURSIVE
        Removes all but one element from every consecutive group of equal elements in the container
        """
        def unique_list(node: Node) -> Node:        #recursive function to remove common elements
            """unique helper"""
            if node is self.node:
                return node
            if node.next.val == node.val:
                temp = node.prev
                temp.next = node.next
                node.next.prev = temp
            unique_list(node.next)
        unique_list(self.node.next)
# Application Problem

def fix_playlist(lst: List) -> bool:
    """
    Checks if the given lst is proper, broken, or improper
    It is broken when there is no cycle
    It is improper when lst forms a cycle with a node other than the root node
    Fixes lst if broken in place
    :param lst: List to check and fix cycle
    :return: True if proper or fixed broken cycle else False
    """
    if lst.empty():
        return True

    def fix_playlist_helper(slow: Node, fast: Node) -> bool:
        slow1 = slow.next
        if slow1 is None and slow1 is not lst.node or fast.next is None and fast.next is not lst.node or fast.next.next\
                is None and fast.next.next is not lst.node:
            if slow1 is None:                                #fixes the broken list
                node1 = slow
            elif fast.next is None:
                node1 = fast
            else:
                node1 = fast.next
            node1.next = lst.node
            lst.node.prev = node1
            return True
        if lst.node.prev is lst.back() and lst.node.prev is not None:     # for proper list
            return True
        slow = slow.next

        fast = fast.next.next

        if slow is fast:          # checks if the list is improper
            return False

        return fix_playlist_helper(slow, fast)

    result = fix_playlist_helper(lst.node, lst.node)

    return result
