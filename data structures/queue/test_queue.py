from queue import Queue
from collections import deque
import unittest


class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()
