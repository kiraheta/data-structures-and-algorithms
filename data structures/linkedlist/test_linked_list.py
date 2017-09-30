from linked_list import LinkedList
import unittest


class Test_LinkedList(unittest.TestCase):

    def setUp(self):
        self.l = LinkedList()

    def test_init(self):
        self.assertEqual(0, self.l.size())

    def test_is_empty(self):
        self.assertEqual(0, self.l.size())


if __name__ == '__main__':
    unittest.main()
