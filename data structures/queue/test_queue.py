from queue import Queue
from collections import deque
import unittest


class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_init(self):
        self.assertEqual(0, self.q.size())


if __name__ == '__main__':
    unittest.main()
