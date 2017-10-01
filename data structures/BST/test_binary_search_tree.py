from binary_search_tree import BinarySearchTree
import unittest


class Test_BinarySearchTree(unittest.TestCase):

    def setUp(self):
        self.b = BinarySearchTree()

    def test_init(self):
        self.assertEqual(None, self.b.root)

    def test_length(self):
        self.assertEqual(0, self.b.size)

    def test_put(self):
        self.b.put(55, "cat")
        self.assertEqual(1, self.b.size)


if __name__ == '__main__':
    unittest.main()