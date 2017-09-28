#!/usr/bin/python

"""
Adjacency List Implementation
"""

class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __self__(self):
        return str(self.id) + ' connectedTo: ' +
        str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()
