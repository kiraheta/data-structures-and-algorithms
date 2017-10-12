# Sort Algorithms

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

#### Reference

https://en.wikipedia.org/wiki/Bubble_sort

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
