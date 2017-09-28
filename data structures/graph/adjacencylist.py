#!/usr/bin/python

"""
Adjacency List Implementation
"""

class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
