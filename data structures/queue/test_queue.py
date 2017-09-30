from queue import Queue
from collections import deque
import unittest


class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()

    def test_init(self):
        self.assertEqual(0, self.q.size())

    def test_is_empty(self):
        self.assertEqual(0, self.q.size())

    def test_enqueue(self):
        self.q.enqueue(3)
        self.assertEqual(1, self.q.size())

    def test_dequeue(self):
        self.q.enqueue(9)
        self.assertEqual(9, self.q.dequeue())

    def test_peek(self):
        self.q.enqueue(2)
        self.q.enqueue(3)
        self.assertEqual(2, self.q.peek())


if __name__ == '__main__':
    unittest.main()
