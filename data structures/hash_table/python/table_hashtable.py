from hashtable import HashTable
import unittest


class Test_HashTable(unittest.TestCase):

    def setUp(self):
        self.h = HashTable()

    def test_init(self):
        self.assertEqual(11, self.h.size)

    def test_put(self):
        self.h[22] = "cat"
        self.assertEqual("cat", self.h[22])

    def test_hashfunction(self):
        self.assertEqual(1, self.h.hashfunction(78, 11))


if __name__ == '__main__':
    unittest.main()
