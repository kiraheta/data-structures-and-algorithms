from queue import Queue
import unittest


class Test_Queue(unittest.TestCase):

    def setUp(self):
        self.q = Queue()
