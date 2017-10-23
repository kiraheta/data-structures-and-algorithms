#!/bin/usr/python

"""
mergesort implementation

mergesort(array){
    mergesort(array's left half)
    mergesort(array's right half)
    merge left and right in sorted order
}
"""


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(aList):
    if(len(aList) < 2):
        return aList[:]
    mid = int(len(aList) / 2)
    left = mergesort(aList[:mid])
    right = mergesort(aList[mid:])
    return merge(left, right)


if __name__ == '__main__':
    array = [-99, 4, 2, 6, 7, 56, 1, 0, 1, 100, 99]
    print(mergesort(array))
