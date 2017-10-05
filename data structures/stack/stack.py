#!/usr/bin/python

"""
Stack implementation
"""


class Stack:
    """Implementation of Stack"""

    def __init__(self):
        """Inits Stack with empty list"""
        self.stack = []

    def is_empty(self):
        """Returns True if Stack is empty"""
        return self.stack == []

    def push(self, item):
        """Pushes item into Stack"""
        self.stack.append(item)

    def pop(self):
        """Pops last item from Stack"""
        return self.stack.pop()

    def peek(self):
        """Returns last item from Stack"""
        return self.stack[-1]

    def size(self):
        """Returns length of Stack"""
        return len(self.stack)
