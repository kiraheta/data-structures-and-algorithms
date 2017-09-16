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
| :---: | | :---: | | :---: | | :---: |
| Access | Search | Insertion | Deletion |
|O (1) | O (n) | O (n) | O (n) |

| Worst | | | |
| :---: | | :---: | | :---: | | :---: |
| Access | Search | Insertion | Deletion |
| O (1) | O (n) | O (n) | O (n) |

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
