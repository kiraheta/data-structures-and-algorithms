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
    """ Implementation of Stack"""

    def __init__(self):
        """
        Inits Queue with empty double ended queue
        """
        self.queue = deque()

    def is_empty(self):
        """
        Returns True if Queue is empty
        """
        return len(self.queue) == 0

    def enqueue(self, item):
        """
        Adds item into Queue
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Pops first item from Queue
        """
        return self.queue.popleft()

    def size(self):
        """
        Returns length of Queue
        """
        return len(self.queue)

# queue example
queue = Queue() # pylint: disable=locally-disabled, invalid-name
print(queue.size())
print(queue.is_empty())
queue.enqueue('carrots')
queue.enqueue('hummus')
print(queue.is_empty()) 
print(queue.size())
print(queue.dequeue())
print(queue.size())
