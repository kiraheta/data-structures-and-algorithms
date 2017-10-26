#!/bin/usr/python

"""
quicksort implementation
"""


def quicksort(aList):
    if len(aList) <= 1:
        return aList
    else:
        pivot = aList[len(aList) // 2]
        lo = [x for x in aList if x < pivot]
        mid = [x for x in aList if x == pivot]
        hi = [x for x in aList if x > pivot]
        return quicksort(lo) + mid + quicksort(hi)

if __name__ == '__main__':
    aList = [100, 55, 44, 40, 30, 4, 2, 6, 1, 11, 8]
    print(quicksort(aList))

