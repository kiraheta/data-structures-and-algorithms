# Data Structures and Algorithms

Python & C++ implementation of the following Data Structures and Algorithms:


| | Data Structures | |
| :---: | :---: | :---: |
| Array | Hash Table| Stack |
| Queue | Linked Lists | Tree |
| | Graphs | | |

---

## Array

> A data structure that contains a fixed max number of
elements of the same data type that are referenced directly
by means of an index.

#### Big O

###### Time Complexity

| Average | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (1) | O (n) | O (n)| O (n) |

| Worst | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (1) | O (n) | O (n)| O (n) |

###### Space Complexity

|Worst|
| :---: |
| O (n)|

#### Implementation

One Dimensional Array

``` C++
// initialize a 10 element array.
int array [10];
```

Two Dimensional Array

``` C++
// an array with 4 rows and 2 columns.
int array[4][2] = { {0,1}, {1,3}, {3,4}, {4,6};

// output each array element's value                      
   for ( int i = 0; i < 4; i++ )
      for ( int j = 0; j < 2; j++ ) {
         cout << "a[" << i << "][" << j << "]: ";
         cout << a[i][j]<< endl;
      }
```
---

## Hash Table

> A data structure that maps keys to values via a hash function
that computes an index into an array of buckets.

#### Big O

###### Time Complexity

| Average | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (1) | O (1) | O (1)| O (1) |

| Worst | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (n)| O (n) |

###### Space Complexity

|Worst|
| :---: |
| O (n)|

---

## Stack

>An abstract data type that serves as a collection of elements, with two principal operations: ``push``, which adds an element to the collection, and ``pop``, which removes the most recently added element that was not yet removed. The order in which elements come off a stack gives rise to its alternative name, LIFO (for last in, first out). Additionally, a ``peek`` operation may give access to the top without modifying the stack.

#### Big O

###### Time Complexity

| Average | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (1)| O (1) |

| Worst   | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (1)| O (1) |

###### Space Complexity

|Worst|
| :---: |
| O (n)|

#### Stack Methods

| Method | Description |
| :---: | :---: |
| push |Add item onto stack|
| pop |Removes the most-recently-pushed item from the stack.|
| peek |Returns the last item pushed onto the stack|

---

## Queue

>An abstract data type whose first or recently added item is the first item removed or retrieved. This property is FIFO. Items enter a queue at its back and leave at its front.

#### Big O

###### Time Complexity

| Average | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (1)| O (1) |

| Worst   | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (1)| O (1) |

###### Space Complexity

|Worst|
| :---: |
| O (n)|
