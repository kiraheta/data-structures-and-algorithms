#!/usr/bin/python

"""
Queue implementation
"""


class Queue:
    """Implementation of Queue"""

    def __init__(self):
        """Inits Queue with empty double ended queue"""
        self.items = []

    def is_empty(self):
        """Returns True if Queue is empty"""
        return self.items == []

    def enqueue(self, item):
        """Adds item into Queue"""
        self.items.insert(0, item)

    def dequeue(self):
        """Pops first item from Queue"""
        return self.items.pop()

    def peek(self):
        """Returns first item from Queue"""
        return self.items[-1]

    def size(self):
        """Returns length of Queue"""
        return len(self.items)
