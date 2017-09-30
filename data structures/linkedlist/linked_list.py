#!/usr/bin/python

"""
Singly Linked List implementation
"""

class Node:
    """Implementation of Node"""

    def __init__(self, item=None, next=None):
        """Inits Node with empty item and next"""
        self.item = item
        self.next = next

    def get_item(self):
        """Returns item from Node"""
        return self.item

    def get_next(self):
        """Returns next from Node"""
        return self.next

    def set_item(self, item):
        """Sets item in Node"""
        self.item = item

    def set_next(self,next):
        """Sets next in Node"""
        self.next = next

class LinkedList:
    """Implementation of LinkedList"""

    def __init__(self,head=None):
        """Inits head with empty item"""
        self.head = head

    def is_empty(self):
        """Returns True if LinkedList is empty"""
        return self.head == None

    def insert(self,item):
        """Insert item in node"""
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def delete(self,item):
        """Deletes item in node"""
        curr = self.head
        prev = None
        found = False
        while curr and found is False:
            if curr.get_item() == item:
                found = True
            else:
                prev = curr
                curr = curr.get_next()
        if curr is None:
            raise ValueError("Item not in list")
        if prev is None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    def search(self,item):
        """Searches item in LinkedList"""
        curr = self.head
        found = False
        while curr and found is False:
            if curr.get_item() == item:
                found = True
            else:
                curr = curr.get_next()
        if curr is None:
             print("Item not in list")
        return found

    def size(self):
        """Returns length of LinkedList"""
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.get_next()
        return count

# test Node
# test = Node('hello')
# print(test.get_item())
# print(test.get_next())

# if __name__ == '__main__':
#     # test LinkedList
#     linked_list = LinkedList() # pylint: disable=locally-disabled, invalid-name
#     print(linked_list.is_empty())
#     linked_list.insert(10)
#     print(linked_list.size())
#     print(linked_list.is_empty())
#     print(linked_list.search(9))
#     print(linked_list.search(10))
#     linked_list.delete(10)
#     print(linked_list.size())
#     print(linked_list.is_empty())
