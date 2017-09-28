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

    def addNeighbor(self, nbr, weight = 0):
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
        self.vertList = {}
        self.numVertices = 0
