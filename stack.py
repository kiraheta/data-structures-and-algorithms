#!/usr/bin/python

# Stack implementation

# @Author: Kenny Iraheta
# @Date: 2017-04-25

# Each stack op takes O(1) time

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)
