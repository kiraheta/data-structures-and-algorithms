from linked_list import LinkedList
import unittest


class Test_LinkedList(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_init(self):
        self.assertEqual(0, self.l.size())

    def test_is_empty(self):
        self.assertEqual(0, self.l.size())

    def test_insert(self):
        self.l.insert(5)
        self.assertEqual(1, self.l.size())

    def test_delete(self):
        self.l.insert(4)
        self.l.delete(4)
        self.assertEqual(0, self.l.size())

    def test_search(self):
        self.l.insert(88)
        self.assertEqual(True, self.l.search(88))

    def test_size(self):
        self.l.insert(33)
        self.assertEqual(1, self.l.size())


if __name__ == '__main__':
    unittest.main()
