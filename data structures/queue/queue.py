#!/usr/bin/python

"""
Queue implementation
"""


class Queue:
    """Implementation of Queue"""

    def __init__(self):
        """Inits Queue with empty list"""
        self.queue = []

    def is_empty(self):
        """Returns True if Queue is empty"""
        return self.queue == []

    def enqueue(self, item):
        """Adds item into Queue"""
        self.queue.insert(0, item)

    def dequeue(self):
        """Pops first item from Queue"""
        return self.queue.pop()

    def peek(self):
        """Returns first item from Queue"""
        return self.queue[-1]

    def size(self):
        """Returns length of Queue"""
        return len(self.queue)
