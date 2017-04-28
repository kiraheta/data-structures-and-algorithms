#!/usr/bin/python

"""
 Queue implementation

 @Author: Kenny Iraheta
 @Date: 2017-04-28

 Each Queue op takes O(1) time
 Note: Using insert(O,x) & pop(0) incurs O(n)
"""
from collections import deque

class Queue:

    def __init__(self):
        self.queue = deque()

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft()

    def size(self):
        return len(self.queue)
