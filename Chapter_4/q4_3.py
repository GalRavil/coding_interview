"""
Given a sorted (increasing order) array, write an algorithm to create a binary
tree with minimal height
"""
from binary_tree import BinaryTree


def balanced_tree(ordered):
    bt = BinaryTree()
    add_range(bt, ordered, 0, len(ordered) - 1)
    return bt


def add_range(bt, ordered, low, high):
    if low <= high:
        mid = (low + high) // 2

        bt.add(ordered[mid])
        add_range(bt, ordered, low, mid - 1)
        add_range(bt, ordered, mid + 1, high)



# ========= Test =============
import unittest


class Test_BalancedTree(unittest.TestCase):
    def setUp(self):
        data = range(10)
        self.bt = balanced_tree(data)

    def test_root(self):
        self.assertEqual(self.bt.root.value, 4)

    def test_left_leaf(self):
        self.assertEqual(self.bt.root.left.value, 1)

    def test_right_leaf(self):
        self.assertEqual(self.bt.root.right.value, 7)

if __name__ == '__main__':
    unittest.main()
