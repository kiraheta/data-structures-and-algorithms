# Sort Algorithms
![language python](https://img.shields.io/badge/language-python-blue.svg)

## Bubble Sort

>A simple sorting algorithm that repeatedly steps through the list to be sorted,
compares each pair of adjacent items and swaps them if they are in the wrong
order. The pass through the list is repeated until no swaps are needed, which
indicates that the list is sorted. The algorithm, which is a comparison sort, is
named for the way smaller or larger elements "bubble" to the top of the list.

#### Big O

###### Time & Space Complexity
| Best | Average | Worst || Worst |
| :---: | :---: | :---: | :---: | :---: |
| O (n) | O (n^2) | O (n^2)|| O (1) |

*Animation of [Bubble Sort](https://upload.wikimedia.org/wikipedia/commons/c/c8/Bubble-sort-example-300px.gif)*

#### Implementation
[bubblesort.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/sort/bubblesort.py)

#### Reference
https://en.wikipedia.org/wiki/Bubble_sort

---

## Insertion Sort

>A simple sorting algorithm that builds the final sorted array (or list) one item at a time. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there. It repeats until no input elements remain.

#### Big O

###### Time & Space Complexity
| Best | Average | Worst || Worst |
| :---: | :---: | :---: | :---: | :---: |
| O (n) | O (n^2) | O (n^2)|| O (1) |

*Animation of [Insertion Sort](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)*

#### Implementation
[insertionsort.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/sort/insertionsort.py)

#### Reference
https://en.wikipedia.org/wiki/Insertion_sort

---

## Selection Sort

>A sorting algorithm that divides the input list into two parts: the sublist of
items already sorted, which is built up from left to right at the front (left)
of the list, and the sublist of items remaining to be sorted that occupy the
rest of the list. Initially, the sorted sublist is empty and the unsorted
sublist is the entire input list. The algorithm proceeds by finding the smallest
(or largest, depending on sorting order) element in the unsorted sublist,
exchanging (swapping) it with the leftmost unsorted element (putting it in
sorted order), and moving the sublist boundaries one element to the right.

#### Big O

###### Time & Space Complexity
| Best | Average | Worst || Worst |
| :---: | :---: | :---: | :---: | :---: |
| O (n^2) | O (n^2) | O (n^2)|| O (1) |

*Animation of [Selection Sort](https://upload.wikimedia.org/wikipedia/commons/b/b0/Selection_sort_animation.gif)*

#### Implementation
[selectionsort.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/sort/selectionsort.py)

#### Reference
https://en.wikipedia.org/wiki/Selection_sort

---

## Merge Sort

>A divide and conquer  recursive sorting algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.

#### Big O

###### Time & Space Complexity
| Best | Average | Worst || Worst |
| :---: | :---: | :---: | :---: | :---: |
| O (n log n) | O (n log n) | O (n log n)|| O (n) |

*Animation of [Merge Sort](https://upload.wikimedia.org/wikipedia/commons/c/cc/Merge-sort-example-300px.gif)*

#### Implementation
[mergesort.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/sort/mergesort.py)

#### Reference
https://en.wikipedia.org/wiki/Merge_sort

---

## Quick Sort

>Quicksort is a divide and conquer algorithm, which first divides a large array into two smaller sub-arrays: the low elements and the high elements. Quicksort can then recursively sort the sub-arrays.

>The steps are:

>    1. Pick an element, called a pivot, from the array.

>    2. Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.

>    3. Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.

>The base case of the recursion is arrays of size zero or one, which are in order by definition, so they never need to be sorted.

>The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance.

#### Big O

###### Time & Space Complexity
| Best | Average | Worst || Worst |
| :---: | :---: | :---: | :---: | :---: |
| O (n log n) | O (n log n) | O (n^2)|| O (n) |

*Animation of [Quick Sort](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)*

#### Implementation
[quicksort.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/sort/quicksort.py)

#### Reference
https://en.wikipedia.org/wiki/Quicksort
