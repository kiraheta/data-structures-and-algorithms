#!/bin/usr/python

"""
Bubblesort Implementation
"""


def bubblesort(aList):
    for i in range(len(aList) - 1):
        for j in range(len(aList) - 1):
            if aList[j] > aList[j + 1]:
                aList[j], aList[j + 1] = aList[j + 1], aList[j]


if __name__ == '__main__':

    aList = [44, 40, 30, 4, 2, 6, 1, 11, 8]
    bubblesort(aList)
    print(aList)
