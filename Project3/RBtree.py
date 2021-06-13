"""
Project 3 (Fall 2020) - Red/Black Trees
Name: Solution
"""

from __future__ import annotations
from typing import TypeVar, Generic, Callable, Generator
from copy import deepcopy
from Project3.RBnode import RBnode as Node

T = TypeVar('T')


class RBtree:
    """
    A Red/Black Tree class
    :root: Root Node of the tree
    :size: Number of Nodes
    """

    __slots__ = ['root', 'size']

    def __init__(self, root: Node = None):
        """ Initializer for an RBtree """
        # this alllows us to initialize by copying an existing tree
        self.root = deepcopy(root)
        if self.root:
            self.root.parent = None
        self.size = 0 if not self.root else self.root.subtree_size()

    def __eq__(self, other: RBtree) -> bool:
        """ Equality Comparator for RBtrees """
        comp = lambda n1, n2: n1 == n2 and (
            (comp(n1.left, n2.left) and comp(n1.right, n2.right)) if (n1 and n2) else True)
        return comp(self.root, other.root) and self.size == other.size

    def __str__(self) -> str:
        """ represents Red/Black tree as string """

        if not self.root:
            return 'Empty RB Tree'

        root, bfs_queue, height = self.root, queue.SimpleQueue(), self.root.subtree_height()
        track = {i: [] for i in range(height + 1)}
        bfs_queue.put((root, 0, root.parent))

        while bfs_queue:
            n = bfs_queue.get()
            if n[1] > height:
                break
            track[n[1]].append(n)
            if n[0] is None:
                bfs_queue.put((None, n[1] + 1, None))
                bfs_queue.put((None, n[1] + 1, None))
                continue
            bfs_queue.put((None, n[1] + 1, None) if not n[0].left else (n[0].left, n[1] + 1, n[0]))
            bfs_queue.put((None, n[1] + 1, None) if not n[0].right else (n[0].right, n[1] + 1, n[0]))

        spaces = 12 * (2 ** (height))
        ans = '\n' + '\t\tVisual Level Order Traversal of RBtree'.center(spaces) + '\n\n'
        for i in range(height):
            ans += f"Level {i + 1}: "
            for n in track[i]:
                space = int(round(spaces / (2 ** i)))
                if not n[0]:
                    ans += ' ' * space
                    continue
                ans += "{} ({})".format(n[0], n[2].value if n[2] else None).center(space, " ")
            ans += '\n'
        return ans

    def __repr__(self) -> str:
        return self.__str__()

    ################################################################
    ################### Complete Functions Below ###################
    ################################################################

    ######################## Static Methods ########################
    # These methods are static as they operate only on nodes, without explicitly
    # referencing an RBtree instance

    @staticmethod
    def set_child(parent: Node, child: Node, is_left: bool) -> None:
        """
        sets the child node of parent to a node
        :param parent: parent node for the child
        :param child: child node for parent
        :param is_left: selecting the left of right child
        :return: void function
        """
        if is_left is True:
            parent.left = child
        else:
            parent.right = child

    @staticmethod
    def replace_child(parent: Node, current_child: Node, new_child: Node) -> None:
        """
        replaces the current child for parent with new_child
        :param parent: parent node for the child
        :param current_child: the child node that has to be replaced
        :param new_child: the new child node
        :return: void functions
        """
        if current_child == parent.left:
            parent.left = new_child
        else:
            parent.right = new_child

    @staticmethod
    def get_sibling(node: Node) -> Node:
        """
        returns the sibling of a node
        :param node: node for which we need the sibling
        :return: node that is the sibling of 'node'
        """
        if node.parent is None:
            return None

        if node.parent.left == node:
            return node.parent.right
        else:
            return node.parent.left

    @staticmethod
    def get_grandparent(node: Node) -> Node:
        """
        Get grandparent of 'node'
        :param node: the node for which the grandparent is needed
        :return: grandparent node for 'node'
        """
        if node.parent is None:
            return None
        return node.parent.parent

    @staticmethod
    def get_uncle(node: Node) -> Node:
        """
        get the uncle node for 'node'
        :param node: node for which uncle is needed
        :return: the uncle node for 'node'
        """

        if node is None or node.parent is None or node.parent.parent is None:
            return None

        if node.parent.parent.left == node.parent:
            return node.parent.parent.right
        else:
            return node.parent.parent.left

    ######################## Misc Utilities ##########################

    def min(self, node: Node) -> Node:
        """
        returns the node with minimum value in tree
        :param node: the node to start our min search with
        :return: the node with minimum value
        """

        def BST_Insert_recursive(parent: Node, value):

            if parent.left is None:
                return parent
            else:
                value = parent.left
                return BST_Insert_recursive(parent.left, val)

        if node is None:
            return None
        val = node.value
        x = BST_Insert_recursive(node, val)
        return x

    def max(self, node: Node) -> Node:
        """
        returns the maximum value node from searching from 'node'
        :param node: node to start our search with
        :return: return the node with maximum value
        """
        def BST_Insert_recursive(parent: Node, val):

            if parent.right is None:
                return parent
            else:
                return BST_Insert_recursive(parent.right, val)

        if node is None:
            return None
        val = node.value
        x = BST_Insert_recursive(node, val)
        return x

    def search(self, node: Node, val: Generic[T]) -> Node:
        """
        search for node with value val
        :param node: node to be searched for
        :param val: the node should have this value
        :return: return the node if found
        """
        def BST_Insert_recursive(parent: Node, val):
            if parent.right is not None:
                if val == parent.right.value:
                    return parent.right
            if parent.left is not None:
                if val == parent.left.value:
                    return parent.left
            if parent is not None:
                if val == parent.value:
                    return parent
            if val < parent.value:
                if parent.left is None:
                    # parent.left.value = val
                    return parent
                else:
                    return BST_Insert_recursive(parent.left, val)
            else:
                if parent.right is None:
                    return parent
                else:
                    return BST_Insert_recursive(parent.right, val)

        if self.root is None:
            return None
        target = BST_Insert_recursive(self.root, val)
        return target

    ######################## Tree Traversals #########################

    def inorder(self, node: Node) -> Generator[Node, None, None]:
        """
        inorder traversal through the tree
        :param node: the node to start our traversal with
        :return: gererator type object with the node
        """
        if node is not None:
            yield from self.inorder(node.left)
            yield node
            yield from self.inorder(node.right)

    def preorder(self, node: Node) -> Generator[Node, None, None]:
        """
        preorder traversal through the tree
        :param node: the node to start our traversal with
        :return: gererator type object with the node
        """
        if node is not None:
            yield node

            yield from self.preorder(node.left)
            yield from self.preorder(node.right)

    def postorder(self, node: Node) -> Generator[Node, None, None]:
        """
        postorder traversal through the tree
        :param node: the node to start our traversal with
        :return: gererator type object with the node
        """
        if node is not None:
            yield from self.postorder(node.left)
            yield from self.postorder(node.right)
            yield node

    def children(self, node):
        """
        Generate an iteration of Positions representing p's children.
        :param node: node the childrens are needed
        :return: the children node for 'node'
        """
        if node.left is not None:
            yield node.left
        if node.right is not None:
            yield node.right

    def bfs(self, node: Node) -> Generator[Node, None, None]:
        """
        breadth first traversal traversal through the tree
        :param node: the node to start our traversal with
        :return: gererator type object with the node
        """
        node1 = node

        if node1 is not None:
            f = []
            f.append(node)

            while len(f) != 0:
                rm = f.pop(0)
                yield rm
                for c in self.children(rm):
                    f.append(c)

    ################### Rebalancing Utilities ######################

    def left_rotate(self, node: Node) -> None:
        """
        rotates the 'node' left
        :param node: node to rotate
        :return: void
        """
        new_root = node.right

        node.right = new_root.left
        if new_root.left is not None:
            new_root.left.parent = node

        new_root.left = node

        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.left:
            node.parent.left = new_root
        else:
            node.parent.right = new_root

        node.parent = new_root

    def right_rotate(self, node: Node) -> None:
        """
        rotates the 'node' right
        :param node: node to rotate
        :return: void
        """
        new_root = node.left

        node.left = new_root.right
        if new_root.right is not None:
            new_root.right.parent = node

        new_root.parent = node.parent
        if node.parent is None:
            self.root = new_root
        elif node == node.parent.right:
            node.parent.right = new_root
        else:
            node.parent.left = new_root
        new_root.right = node

        node.parent = new_root

    def insertion_repair(self, node: Node) -> None:
        """
        if the tree is unbalanced due to insertion the balance the tree
        :param node: the node that was inserted
        :return: void
        """
        if node.parent is None:
            node.is_red = False
            return
        if not node.parent.is_red:
            return

        parent_node = node.parent
        grandparent_node = self.get_grandparent(node)
        uncle_node = self.get_uncle(node)

        if uncle_node is not None and uncle_node.is_red is True:
            parent_node.is_red = uncle_node.is_red = False
            grandparent_node.is_red = True
            self.insertion_repair(grandparent_node)
            return
        if node == parent_node.right and parent_node == grandparent_node.left:
            self.left_rotate(parent_node)
            node = parent_node
            parent_node = node.parent
        elif node == parent_node.left and parent_node == grandparent_node.right:
            self.right_rotate(parent_node)
            node = parent_node
            parent_node = node.parent

        parent_node.is_red = False
        grandparent_node.is_red = True

        if node == parent_node.left:
            self.right_rotate(grandparent_node)
        else:
            self.left_rotate(grandparent_node)

    def treeNonNullAndRed(self, node):
        """
        helper funtion if node is not None and red
        :param node: checking this node
        :return: bool
        """
        if node is None:
            return False
        return node.is_red is True

    def treeIsNullOrBlack(self, node):
        """
        helper funtion if node is  None or not red
        :param node: checking this node
        :return: bool
        """
        if node is None:
            return True
        return node.is_red is False

    def bothChildrenAreBlack(self, node):
        """
        helper funtion if node's children are black
        :param node: checking this node
        :return: bool
        """
        if node.left is not None and node.left.is_red is True:
            return False
        elif node.right is not None and node.right.is_red is True:
            return False
        return True

    def case1(self, node):
        """ Helper function for prepare removal"""
        if node.is_red is True or node.parent is None:
            return True
        else:
            return False

    def case2(self, node: Node, sibling: Node):
        """ Helper function for prepare removal"""

        if sibling.is_red:
            node.parent.is_red = True
            sibling.is_red = False
            if node == node.parent.left:
                self.left_rotate(node.parent)
            else:
                self.right_rotate(node.parent)
            return True

        return False

    def case3(self, node: Node, sibling: Node):
        """ Helper function for prepare removal"""

        if node.parent.is_red is False and self.bothChildrenAreBlack(sibling):
            sibling.is_red = True
            self.prepare_removal(node.parent)
            return True
        return False

    def case4(self, node: Node, sibling: Node):
        """ Helper function for prepare removal"""

        if node.parent.is_red is True and self.bothChildrenAreBlack(sibling):
            node.parent.is_red = False
            sibling.is_red = True
            return True
        return False

    def case5(self, node: Node, sibling: Node):
        """ Helper function for prepare removal"""
        if self.treeNonNullAndRed(sibling.left) and self.treeIsNullOrBlack(sibling.right) \
                and node == node.parent.left:
            sibling.is_red = True
            sibling.left.is_red = False
            self.right_rotate(sibling)
            return True
        return False

    def case6(self, node: Node, sibling: Node):
        """ Helper function for prepare removal"""

        if self.treeIsNullOrBlack(sibling.left) and self.treeNonNullAndRed(sibling.right) and node == node.parent.right:
            sibling.is_red = True
            sibling.right.is_red = False
            self.left_rotate(sibling)
            return True
        return False

    def prepare_removal(self, node: Node) -> None:
        """
        prepare the tree for node to be removed
        :param node: the node that will be removed
        :return: void
        """
        if self.case1(node):
            return
        sibling = self.get_sibling(node)
        if self.case2(node, sibling):
            sibling = self.get_sibling(node)
        if self.case3(node, sibling):
            return
        if self.case4(node, sibling):
            return
        if self.case5(node, sibling):
            sibling = self.get_sibling(node)
        if self.case6(node, sibling):
            sibling = self.get_sibling(node)

        sibling.is_red = node.parent.is_red
        node.parent.is_red = False

        if node == node.parent.left:
            sibling.right.is_red = False
            self.left_rotate(node.parent)
        else:
            sibling.left.is_red = False
            self.right_rotate(node.parent)

    ##################### Insertion and Removal #########################

    def insert(self, node: Node, val: Generic[T]) -> None:
        """
        Insert node with value val in tree
        :param node: node to be inserted
        :param val: value in node
        :return: void
        """

        def bst_insert_recursive(parent: Node, insert_node: Node):
            if parent.right is not None:
                if insert_node.value == parent.right.value:
                    return
            if parent.left is not None:
                if insert_node.value == parent.left.value:
                    return
            if parent is not None:
                if insert_node.value == parent.value:
                    return
            if insert_node.value < parent.value:
                if parent.left is None:
                    parent.left = insert_node
                    insert_node.parent = parent
                else:
                    bst_insert_recursive(parent.left, insert_node)
            else:
                if parent.right is None:
                    parent.right = insert_node
                    insert_node.parent = parent
                else:
                    bst_insert_recursive(parent.right, insert_node)

        node = Node(val, False)
        node.left = node.right = None
        if self.root is None:
            self.root = node
        else:
            bst_insert_recursive(self.root, node)

        node.is_red = True
        self.insertion_repair(node)
        self.size = self.root.subtree_size()

    def bst_remove(self, value, node):
        """
        remove the node with value val in a BST
        :param value: value of node
        :param node: node to be removed
        :return: void
        """
        parent = node.parent
        curr = node

        if curr.right is None and curr.left is None:
            if parent is None:
                self.root = None
            elif parent.right is not None and parent.right.value == value:
                parent.right = None
            else:
                parent.left = None
            self.size -= 1
            return
        if curr.right is None or curr.left is None:
            if curr.right is not None:
                children_node = curr.right
            else:
                children_node = curr.left
            if parent is None:
                self.root = children_node
            elif parent.right is not None and parent.right.value == value:
                parent.right = children_node
            else:
                parent.left = children_node
            children_node.parent = parent
            self.size -= 1
            return


    def tree_remove(self, node):
        """
        Helper function for remove ,checks for appropriate conditions and prepares the removal
        if nessacary
        :param node: node to be removed
        :return: void
        """
        if node.left is not None and node.right is not None:
            pred_node = self.get_pred(node)
            pred_key = pred_node.value
            self.tree_remove(pred_node)
            node.value = pred_key
            return

        if node.is_red is False:
            self.prepare_removal(node)
        self.bst_remove(node.value, node)

        if self.root is not None and self.root.is_red:
            self.root.is_red = False

    def get_pred(self, node):
        """
        returns the predecessor of node
        :param node: node whose predecessor is returned
        :return: predecessor of node
        """
        node = node.left
        while node.right is not None:
            node = node.right
        return node

    def remove(self, node: Node, val: Generic[T]) -> None:
        """
        remove the node from the tree if found
        :param node: node to be removed
        :param val: value of node
        :return: void
        """
        if self.root is not None:
            node = self.search(node, val)
            if node is not None and node.value == val:
                self.tree_remove(node)
