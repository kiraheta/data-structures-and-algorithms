from stack import Stack
import unittest


class Test_Stack(unittest.TestCase):

    def test_init(self):
        s = Stack()
        self.assertEqual(0, s.size())

    def test_is_empty(self):
        s = Stack()
        self.assertEqual(0, s.size())

    def test_push(self):
        s = Stack()
        s.push(5)
        self.assertEqual(1, s.size())

    def test_pop(self):
        s = Stack()
        s.push(5)
        self.assertEqual(5, s.pop())


if __name__ == '__main__':
    unittest.main()
