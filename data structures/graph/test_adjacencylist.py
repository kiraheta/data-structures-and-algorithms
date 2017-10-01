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

    def test_getVertex(self):
        self.assertEqual(None, self.g.getVertex(22))

    def test_addEdge(self):
        self.g.addVertex(10)
        self.g.addVertex(20)
        self.g.addVertex(30)
        self.g.addEdge(10, 30, 5)
        for v in self.g:
            for w in v.getConnections():
                weight = v.getWeight(w)
        self.assertEqual(5, weight)

    def test_getVertices(self):
        self.g.addVertex(10)
        self.assertEqual(1, len(self.g.getVertices()))


if __name__ == '__main__':
    unittest.main()
