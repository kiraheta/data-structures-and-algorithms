from stack import Stack
import unittest


class Test_Stack(unittest.TestCase):

    def test_init(self):
        s = Stack()
        self.assertEqual(0, s.size())


if __name__ == '__main__':
    unittest.main()
