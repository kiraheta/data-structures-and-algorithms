#!/usr/bin/python

# Python Dictionary Hash Table and Examples
#
# @Author: Kenny Iraheta
# @Date: 2017-04-25

# setup dict for example
dict = {} # empty dict
# store key-value pairs in dict
dict = {'a':'apples', 'b':'bananas', 'c':'carrot'}
dict['d'] = 'donuts'

# Lookup Value
print (dict['a'])

# Get KeyError if not in dict
#print (dict['e'])

# Ensure no KeyError
if 'e' in dict:
    print (dict['e'])

# Prints 'none' if key not in dict
print (dict.get('e'))

# True if key in dict
print ('b' in dict)

# Iterates all key/value in dict
for key in dict:
    print (key)

# Iterates all key/values in sorted order in dict
for key in sorted(dict.keys()):
    print (key, dict[key])

# Printing with % operator
print ("Homer loves %(d)s!" % dict)

# Deleting a key/value pair
del dict['d']
print (dict) # No more donuts!
