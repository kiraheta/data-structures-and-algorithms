#!/usr/bin/python

# Common Python List Methods and Examples
#
# @Author: Kenny Iraheta
# @Date: 2017-04-24

# setup list for example
list = ['Mercury', 'Venus', 'Earth']
list2 = ['Jupiter', 'Saturn', 'Uranus']

# list.append(elem)
#
# adds a single element to the end of the List
# common err: doesn't return the new list, just
# modifies the original
list.append('Mars') # appends elem at end

# list.insert(index,elem)
#
# inserts element at given index, shifting
# elements to the right
list.insert(3,'Asteroid Belt') # appends elem at index 3

# list.extend(list2)
#
# adds elements in list2 to end of list.
# Using + or += on a list is similar to use extend.
list.extend(list2)

# list.index(elem)
#
# searches for given elem from start of list and returns
# its index. Throws a ValueError if elem doesn't appear
# (use "in" to check w/o a ValueError)
print (list.index('Mars'))

# list.remove(elem)
#
# searches for first instance of given elem and
# removes it (throws ValueError if not present)
list.append('Pluto')
print (list)
list.remove('Pluto') # search and removes Pluto from list :(
print (list)

# list.sort()
#
# sorts the list in place (doesn't return it) by
# alpha and/or numeric
list.sort()
print (list)

# list.reverse()
#
# reverses the list in place (doesn't return it)
list.reverse()
print (list)

# list.pop(index)
#
# removes and returns the element at the given
# index. Returns rightmost element if index is
# omitted (opp of append)
print (list.pop(0)) # removes and return first elem
print (list.pop())  # removes rightmost elem
