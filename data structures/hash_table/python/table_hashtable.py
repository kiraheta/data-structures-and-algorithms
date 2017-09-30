from hashtable import HashTable
import unittest


class Test_HashTable(unittest.TestCase):

    def setUp(self):
        self.h = HashTable()

    def test_init(self):
        self.assertEqual(11, self.h.size)


if __name__ == '__main__':
    unittest.main()
