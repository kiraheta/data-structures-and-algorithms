#!/usr/bin/python

"""
Adjacency List Implementation
"""


class Vertex:

    def __init__(self, key):
        """
        Constructor initializes the id and the edges dictionary
        """
        self.id = key
        self.edges = {}

    def is_empty(self):
        """
        Returns True if edges is empty
        """
        return self.edges == {}

    def addNeighbor(self, nbr, weight=0):
        """
        Adds a connection between two vertices
        """
        self.edges[nbr] = weight

    def __str__(self):
        """
        Returns ids of connected vertices
        """
        return str(self.id) + ' connectedTo: ' + \
            str([x.id for x in self.edges])

    def getConnections(self):
        """
        Returns all of the vertices in the adjacency list
        """
        return self.edges.keys()

    def getId(self):
        """
        Returns id
        """
        return self.id

    def getWeight(self, nbr):
        """
        Returns the weight of the edge from this vertex to the vertex passed
        as a parameter
        """
        return self.edges[nbr]


class Graph:

    def __init__(self):
        """
        Constructor iniatializes dictionary vertList that maps vertex names to
        vertex objects and numVertices to keep track of num of vertices in graph
        """
        self.vertList = {}
        self.numVertices = 0

    def is_empty(self):
        """
        Returns True if numVertices is empty
        """
        return self.numVertices == 0

    def edges_is_empty(self):
        """
        Returns True if edges is empty
        """
        for v in self:
            return v.is_empty() == True

    def addVertex(self, key):
        """
        Adds a vertex to vertList
        """
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        Returns vertex if found
        """
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        """
        Returns n if its in vertList
        """
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        """
        Adds an edge between vertices f and t
        """
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        """
        Returns the names of all of the vertices in graph
        """
        return self.vertList.keys()

    def __iter__(self):
        """
        Iterates over all the vertex objects in graph
        """
        return iter(self.vertList.values())

    def getVerticesAndWeights(self):
        """
        Prints the connected vertices and their weight in graph
        """
        if self.is_empty():
            print("No vertices in graph.")
        if self.edges_is_empty():
            print("No edges in graph.")
        for vertex in self:
            for vertexes in vertex.getConnections():
                print('({}, {}) => {}'.format(vertex.getId(),
                                              vertexes.getId(),
                                              vertex.getWeight(vertexes)))
