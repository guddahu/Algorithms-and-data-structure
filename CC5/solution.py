"""
CC5- Trie
Name: Aditya Raj
"""

from __future__ import annotations  # allow self-reference
MAXVALUE = -99999999
class TreeNode:
    """Tree Node that contains a value as well as left and right pointers"""
    def __init__(self, val: int = 0, left: TreeNode = None, right: TreeNode = None):
        self.val = val
        self.left = left
        self.right = right


class Track:
    """
    Class to keep track of last subtree and last sum
    """
    def __init__(self, maximum=0, minimum=0, bst_=True, sum_=0, max_sum=0):
        self.max = maximum          #max value
        self.maxsum = max_sum       #max_sum

        self.min = minimum          #min val in subtree

        self.bst = bst_             #is it a bst

        self.sum = sum_             #current sum

def postorder(node: TreeNode):
    """
    helper function for game master to compute the largest sum
    starts from the bottom and keeps track of the last values of sum, min and max
    :param node:
    :return: track object with sum
    """
    global MAXVALUE         #keeps track of max value
    if node is None:
        return Track(-999999999, 9999999999, True, 0, 0)
    if node.left is None and node.right is None:
        MAXVALUE = max(MAXVALUE, node.val)
        return Track(node.val, node.val, True, node.val, MAXVALUE)

    left = postorder(node.left)
    right = postorder(node.right)

    tracker = Track()

    if right.bst and left.bst and left.max < node.val < right.min:   #checks if a BST

        tracker.min = min(node.val, right.min, left.min)
        tracker.max = max(node.val, left.max, right.max)

        MAXVALUE = max(MAXVALUE, right.sum + node.val + left.sum)
        tracker.sum = left.sum + right.sum + node.val

        tracker.maxsum = MAXVALUE
        tracker.bst = True
        return tracker
    tracker.bst = False
    tracker.maxsum = MAXVALUE
    tracker.sum = left.sum + right.sum + node.val
    return tracker

def game_master(root: TreeNode) -> int:
    """
    finds the largest sum if bst subtree
    :param root: root node of tree
    :return: int ie the largest sum of a BST in tree
    """
    global MAXVALUE
    MAXVALUE = -99999999
    tracker1 = postorder(root)
    return tracker1.maxsum
