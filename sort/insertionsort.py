#!/bin/usr/pytho

"""
insertionsort implementation
"""


def insertionsort(aList):
    for i in range(1, len(aList)):
        key = aList[i]
        j = i - 1
        while j >= 0 and aList[j] > key:
            aList[j + 1] = aList[j]
            j -= 1
        aList[j + 1] = key
    return aList


if __name__ == '__main__':

    aList = [100, 55, 44, 40, 30, 4, 2, 6, 1, 11, 8]
    insertionsort(aList)
    print(aList)
