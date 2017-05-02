#!/usr/bin/python

"""
 Singly Linked List implementation

 @Author: Kenny Iraheta
 @Date: 2017-04-29
"""

class Node:
    """ Implementation of Node"""

    def __init__(self, item=None, next=None):
        """
        Inits Node with empty item and next
        """
        self.item = item
        self.next = next

    def get_item(self):
        """
        Returns item from Node
        """
        return self.item

    def get_next(self):
        """
        Returns next from Node
        """
        return self.next

    def set_item(self, item):
        """
        Sets item in Node
        """
        self.item = item

    def set_next(self,next):
        """
        Sets next in Node
        """
        self.next = next

class LinkedList:
    """ Implementation of LinkedList"""

    def __init__(self,head=None):
        """
        Inits head with empty item
        """
        self.head = head

    def insert(self,item):
        """
        Insert item in node
        """
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def delete(self,item):
        """
        Deletes item in node
        """

# test Node
test = Node('hello')
print(test.get_item())
print(test.get_next())
