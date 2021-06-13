from List import List
from typing import TypeVar, Generic, Callable  # function type
from Node import DoublyLinkedListNode as Node
def fix_playlist(lst: List) -> bool:
    """
    Checks if the given lst is proper, broken, or improper
    It is broken when there is no cycle
    It is improper when lst forms a cycle with a node other than the root node
    Fixes lst if broken in place
    :param lst: List to check and fix cycle
    :return: True if proper or fixed broken cycle else False
    """

    def fix_playlist_helper(slow: Node, fast: Node) -> bool:
        """fix_playlist helper"""
        if slow is lst.node:
            return True
        if slow == fast:
            return False
        fix_playlist(slow.next,fast.next.next)
    return fix_playlist_helper(lst.next,lst.next.next)
lst =List()
# one item - improper
lst.assign(container=[1])
lst.node.prev.next = lst.node.next  # bug
lst.node.prev = None  # bug
print(fix_playlist(lst))