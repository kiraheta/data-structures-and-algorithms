from binary_search_tree import BinarySearchTree
import unittest


class Test_BinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.b = BinarySearchTree()

    def test_init(self):
        self.assertEqual(0, self.b.size)


if __name__ == '__main__':
    unittest.main()
