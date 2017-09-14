#!/usr/bin/python

"""
 Common Python List Methods and Examples

 @Author: Kenny Iraheta
 @Date: 2017-04-24
"""

# setup list for example
solar_system_1 = ['Mercury', 'Venus', 'Earth'] # pylint: disable=locally-disabled, invalid-name
solar_system_2 = ['Jupiter', 'Saturn', 'Uranus'] # pylint: disable=locally-disabled, invalid-name

# list.append(elem)
#
# adds a single element to the end of the List
# common err: doesn't return the new list, just
# modifies the original
solar_system_1.append('Mars') # appends elem at end

# list.insert(index,elem)
#
# inserts element at given index, shifting
# elements to the right
solar_system_1.insert(3, 'Asteroid Belt') # appends elem at index 3

# list.extend(list2)
#
# adds elements in list2 to end of list.
# Using + or += on a list is similar to use extend.
solar_system_1.extend(solar_system_2)

# list.index(elem)
#
# searches for given elem from start of list and returns
# its index. Throws a ValueError if elem doesn't appear
# (use "in" to check w/o a ValueError)
print(solar_system_1.index('Mars'))

# list.remove(elem)
#
# searches for first instance of given elem and
# removes it (throws ValueError if not present)
solar_system_1.append('Pluto')
print(solar_system_1)
solar_system_1.remove('Pluto') # search and removes Pluto from list :(
print(solar_system_1)

# list.sort()
#
# sorts the list in place (doesn't return it) by
# alpha and/or numeric
solar_system_1.sort()
print(solar_system_1)

# list.reverse()
#
# reverses the list in place (doesn't return it)
solar_system_1.reverse()
print(solar_system_1)

# list.pop(index)
#
# removes and returns the element at the given
# index. Returns rightmost element if index is
# omitted (opp of append)
print(solar_system_1.pop(0)) # removes and return first elem
print(solar_system_1.pop())  # removes rightmost elem
