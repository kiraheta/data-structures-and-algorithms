#!/bin/usr/python

"""
selectionsort implementation
"""

def selectionsort(aList):
    for i in range(len(aList) - 1):
        minIndex = i
        for j in range(i + 1, len(aList)):
            if aList[j] < aList[minIndex]:
                minIndex = j
        if minIndex != i:
            aList[i], aList[minIndex] = aList[minIndex], aList[i]
    return aList


if __name__ == '__main__':
    aList = [9, 3, 11, 33, 55, 99, 88, 1]
    print(selectionsort(aList))
