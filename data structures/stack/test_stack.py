from stack import Stack
import unittest


class Test_Stack(unittest.TestCase):

    def setUp(self):
        self.s = Stack()

    def test_init(self):
        self.assertEqual(0, self.s.size())

    def test_is_empty(self):
        self.assertEqual(0, self.s.size())

    def test_push(self):
        self.s.push(5)
        self.assertEqual(1, self.s.size())

    def test_pop(self):
        self.s.push(5)
        self.assertEqual(5, self.s.pop())

    def test_peek(self):
        self.s.push(2)
        self.assertEqual(2, self.s.peek())

    def test_size(self):
        self.s.push(1)
        self.s.push(3)
        self.assertEqual(2, self.s.size())


if __name__ == '__main__':
    unittest.main()
