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

    def test_get(self):
        self.b[33] = "cat"
        self.assertEqual("cat", self.b.get(33))

    def test_delete(self):
        self.b[22] = "dog"
        self.b.delete(22)
        self.assertEqual(0, self.b.size)


if __name__ == '__main__':
    unittest.main()
