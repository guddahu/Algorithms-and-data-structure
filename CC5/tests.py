
import unittest
from solution import game_master, TreeNode as Node


class TestCodingChallenge5(unittest.TestCase):

    def test_empty_and_single(self):
        actual = game_master(None)
        expected = 0
        self.assertEqual(expected, actual) # empty BST should have a sum of 0

        one_node = Node(4)
        actual = game_master(one_node)
        expected = 4
        self.assertEqual(expected, actual) # a BST with just one node should have the sum of that node's value

    def test_whole_tree_is_BST(self):
        tree_root1 = Node(2, Node(1), Node(3))
        actual = game_master(tree_root1)
        expected = 6
        self.assertEqual(expected, actual) # sum of all nodes of the tree, 3 Nodes

        tree_root2 = Node(5, Node(3, Node(1), Node(4)), Node(7, Node(6), Node(8)))
        actual = game_master(tree_root2)
        expected = 34
        self.assertEqual(expected, actual) # sum of all nodes of the tree, 7 Nodes

    def test_right_subtree(self):
        '''
              5
          5       7
        2   6   6   8
        '''
        tree_root1 = Node(5, Node(5, Node(2), Node(6)), Node(7, Node(6), Node(8)))
        actual = game_master(tree_root1)
        expected = 21
        self.assertEqual(expected, actual) # tree_root1.right is a BST

        tree_root2 = Node(2, None, Node(3, None, Node(4, None, Node(5, None, Node(6)))))
        actual = game_master(tree_root2)
        expected = 20
        self.assertEqual(expected, actual) # all nodes are to the right of the root; is a BST

        tree_root3 = Node(6, None, Node(5, None, Node(4, None, Node(3, None, Node(2)))))
        actual = game_master(tree_root3)
        expected = 2
        self.assertEqual(expected, actual) # all nodes are to the right of the rootl; only leaf is BST

    def test_left_subtree(self):
        '''
              5
          3       2
        2   4   3   3
        '''
        tree_root1 = Node(5, Node(3, Node(2), Node(4)), Node(2, Node(3), Node(3)))
        actual = game_master(tree_root1)
        expected = 9
        self.assertEqual(expected, actual) # tree_root1.left is a BST

        tree_root2 = Node(6, Node(5, Node(4, Node(3, Node(2)))))
        actual = game_master(tree_root2)
        expected = 20
        self.assertEqual(expected, actual) # all nodes are to the left of the root; is a BST

        tree_root3 = Node(2, Node(3, Node(4, Node(5, Node(6)))))
        actual = game_master(tree_root3)
        expected = 6
        self.assertEqual(expected, actual) # all nodes are to the left of the root; only leaf is a BST

    def test_leaves(self):
        '''
              5
          6       7
        9   3   6   5
        '''
        tree_root1 = Node(5, Node(6, Node(9), Node(3)), Node(7, Node(6), Node(5)))
        actual = game_master(tree_root1)
        expected = 9
        self.assertEqual(expected, actual) # no BSTs; largest sum is value of largest leaf

        '''
          2
        2   2
        '''
        tree_root2 = Node(2, Node(2), Node(2))
        actual = game_master(tree_root2)
        expected = 2
        self.assertEqual(expected, actual) # only 2's
        '''
              3
          4       6
        5       7   7
        '''
        tree_root3 = Node(3, Node(4, Node(5)), Node(6, Node(7), Node(7)))
        actual = game_master(tree_root3)
        expected = 7
        self.assertEqual(expected, actual) # asymetrical tree; sum is leaf value

    def test_misc(self):
        '''
                  8
            3           6
          2   4             
        1    
        '''
        tree_root1 = Node(8,Node(3, Node(2, Node(1)), Node(4)), Node(6))
        actual = game_master(tree_root1)
        expected = 10
        self.assertEqual(expected, actual) # more nodes in left subtree; left is larger
        '''
                  12
            3           10
          2   4             
        1    
        '''
        tree_root1 = Node(12,Node(3, Node(2, Node(1)), Node(4)), Node(10))
        actual = game_master(tree_root1)
        expected = 10
        self.assertEqual(expected, actual) # more nodes in left subtree; tie
        '''
                  12
            3           11
          2   4             
        1    
        '''
        tree_root1 = Node(12,Node(3, Node(2, Node(1)), Node(4)), Node(11))
        actual = game_master(tree_root1)
        expected = 11
        self.assertEqual(expected, actual) # more nodes in left subtree; right is larger
        '''
                    8
              4           12
            3   5
        '''
        tree_root = Node(8, Node(4, Node(3), Node(5)), Node(12))
        actual = game_master(tree_root)
        expected = 32
        self.assertEqual(expected, actual) # whole tree is BST, unbalanced
        '''
                    8
              4           12
            5   5
        '''
        tree_root.left.left.val = 5
        actual = game_master(tree_root)
        expected = 12
        self.assertEqual(expected, actual) # right subtree is no longer BST

    def test_large(self):
        '''
                                    12
                    11                               18
             9              11               15               21
          5     7       11      11       13      16       20      23
        1   3 6   10  11   11 11   11  11   14 16  17   19  21  22  23
        '''
        tree_root1 = Node(12, Node(11, Node(9, Node(5, Node(1), Node(3)), Node(7, Node(6), Node(10))), \
            Node(11, Node(11, Node(11), Node(11)), Node(11, Node(11), Node(11)))), Node(18, Node(15, Node(13, Node(11), Node(14)), Node(16, Node(16), Node(17))),\
                Node(21, Node(20, Node(19), Node(21)), Node(23, Node(22), Node(23)))))
        actual = game_master(tree_root1)
        expected = 60
        self.assertEqual(expected, actual) # tree_root1.right.right.left is root of subtree
        '''
                                    12
                    11                               18
             9              11               15               21
          5     7       11      11       13      16       21      23
        1   3 6   10  11   11 11   11  11   14 16  17   19  21  22  23
        '''
        tree_root1.right.right.left.val = 21
        actual = game_master(tree_root1)
        expected = 38
        self.assertEqual(expected, actual) # tree_root1.right.left.left is root of subtree
        '''
                                    12
                    11                                 19
             9              11                 15               21
          5     7       11      11         13      17       21      23
        1   3 6   10  11   11 11   11    11   14 16  18   20  22  22  23
        '''
        tree_root1.right.right.left.left.val = 20
        tree_root1.right.left.right.val = 17
        tree_root1.right.left.right.right.val = 18
        tree_root1.right.val = 19
        tree_root1.right.right.left.right.val = 22
        actual = game_master(tree_root1)
        expected = 104
        self.assertEqual(expected, actual) # tree_root1.right.left is the root of the subtree
        '''
                                        12
                        11                                 19
                9              11                 15               21
             5     7       11      11                          21     
           1   3 6       11   11 11   11                         22  
          0   2   9    11    11    11   11
        -3       8 9
        '''
        tree_root1 = Node(12, Node(11, Node(9, Node(5, Node(1, Node(0, Node(-3))), Node(3, Node(2))), Node(7, Node(6, None, Node(9, Node(8), Node(9))))), \
                    Node(11, Node(11, Node(11, Node(11)), Node(11, Node(11))), Node(11, Node(11, None, Node(11)), Node(11, None, Node(11))))), \
                    Node(19, Node(15), Node(21, Node(21, None, Node(22)))))
                    
        actual = game_master(tree_root1)
        expected = 43
        self.assertEqual(expected, actual) # 21 + 22
        '''
                                        12
                        11                                 19
                9              11                 15               21
             5     7       11      11                          21     
           1   3 6       11   11 11   11                         
          0   2   9    11    11    11   11
        -3       8 9
        '''
        tree_root1.right.right.left.right = None
        actual = game_master(tree_root1)
        expected = 21
        self.assertEqual(expected, actual) # leaf 21
        '''
                                        12
                        11                                 19
                9              11                 15               
             5     7       11      11                             
           1   3 6       11   11 11   11                         
          0   2   9    11    11    11   11
        -3       8 9
        '''
        tree_root1.right.right = None
        actual = game_master(tree_root1)
        expected = 34
        self.assertEqual(expected, actual) # 15 + 19
        '''
                                        12
                        11
                9              11               
             5     7       11      11                             
           1   3 6       11   11 11   11
          0   2   9    11    11    11   11
        -3       8 9
        '''
        tree_root1.right = None
        actual = game_master(tree_root1)
        expected = 11
        self.assertEqual(expected, actual) # leaf 11
        '''
                                        12
                        11
                6              11               
            5     11       11      11                             
           1   3 7       11   11 11   11
          0   2   9    11    11    11   11
        -3       8 10
        '''
        tree_root1.left.left.val = 6
        tree_root1.left.left.right.val = 11
        tree_root1.left.left.right.left.val = 7
        tree_root1.left.left.right.left.right.val = 9
        tree_root1.left.left.right.left.right.left.val = 8
        tree_root1.left.left.right.left.right.right.val = 10
        actual = game_master(tree_root1)
        expected = 45
        self.assertEqual(expected, actual) # 11 + 10 + 9 + 8 + 7
        '''
                                        12
                        11                                 46
                9              11              
             5     7       11      11                             
           1   3 6       11   11 11   11                         
          0   2   9    11    11    11   11
        -3       8 9
        '''
        tree_root1.right = Node(46)
        actual = game_master(tree_root1)
        expected = 46
        self.assertEqual(expected, actual) # leaf 46

if __name__ == '__main__':
    unittest.main()
