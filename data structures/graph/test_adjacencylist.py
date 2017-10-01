from adjacencylist import Graph
import unittest


class Test_Graph(unittest.TestCase):

    def setUp(self):
        self.g = Graph()

    def test_init(self):
        self.assertEqual(0, self.g.numVertices)

    def test_addVertex(self):
        self.g.addVertex(22)
        self.assertEqual(1, self.g.numVertices)


if __name__ == '__main__':
    unittest.main()
