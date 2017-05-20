#!/usr/bin/python

"""
 Stack implementation

 @Author: Kenny Iraheta
 @Date: 2017-04-25

 Each stack op takes O(1) time
"""

class Stack:
    """ Implementation of Stack"""

    def __init__(self):
        """
        Inits Stack with empty list
        """
        self.stack = []

    def is_empty(self):
        """
        Returns True if Stack is empty
        """
        return self.stack == []

    def push(self, item):
        """
        Pushes item into Stack
        """
        self.stack.append(item)

    def pop(self):
        """
        Pops last item from Stack
        """
        return self.stack.pop()

    def peek(self):
        """
        Returns last item from Stack
        """
        return self.stack[-1]

    def size(self):
        """
        Returns length of Stack
        """
        return len(self.stack)

if __name__ == '__main__':
    # Stack example
    stack = Stack() # pylint: disable=locally-disabled, invalid-name

    print(stack.is_empty()) # True since empty
    stack.push('burgers')
    stack.push('fries')
    print(stack.peek())
    print(stack.is_empty()) # False since not empty
    print(stack.pop())
    print(stack.size())
    print(stack.pop())
    print(stack.is_empty()) # True since empty again
