#!/usr/bin/python

"""
Adjacency List Implementation
"""


class Vertex:

    def __init__(self, key):
        """
        Constructor initializes the id and the connectedTo dictionary
        """
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
        Adds a connection between two vertices
        """
        self.connectedTo[nbr] = weight

    def __self__(self):
        """
        Returns ids of connected vertices
        """
        return str(self.id) + ' connectedTo: ' +
        str([x.id for x in self.connectedTo])

    def getConnections(self):
        """
        Returns all of the vertices in the adjacency list
        """
        return self.connectedTo.keys()

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
        return self.connectedTo[nbr]


class Graph:

    def __init__(self):
        """ 
        Constructor iniatializes dictionary vertList that maps vertex names to 
        vertex objects and numVertices to keep track of num of vertices in graph
        """
        self.vertList = {}
        self.numVertices = 0

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
        Iterates over all the vertex objects in graph object
        """
        return iter(self.vertList.values())
