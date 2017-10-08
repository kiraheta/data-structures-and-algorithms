# Data Structures and Algorithms

Python implementation of the following Data Structures and Algorithms:


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
// initialize a 10 element array
int array [10];
```

Two Dimensional Array

``` C++
// an array with 4 rows and 2 columns
int array[4][2] = { {0,1}, {1,3}, {3,4}, {4,6} };

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

#### Implementation
[hashtable.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/hash_table/python/hashtable.py)

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
| pop |Removes the most-recently-pushed item from the stack|
| peek |Returns the last item pushed onto the stack|

#### Implementation
[stack.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/stack/stack.py)

###### Test Implementation
[test_stack.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/stack/test_stack.py)

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

#### Queue Methods

| Method | Description |
| :---: | :---: |
| enqueue |Adds a new item to the rear of the queue|
| dequeue |Removes the front item from the queue|

#### Implementation
[queue.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/queue/queue.py)

###### Test Implementation
[test_queue.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/queue/test_queue.py)


---

## Linked List

>A linear data structure and a list of elements or nodes comprised of two items: the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list. It should be noted that head is not a separate node, but the reference to the first node. If the list is empty then the head is a null reference.

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

#### Implementation
[linked_list.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/linkedlist/linked_list.py)

###### Test Implementation
[linked_list.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/linkedlist/linked_list.py)

---

## Tree

>A tree is a collection of nodes connected by directed (or undirected) edges. A tree is a nonlinear data structure, compared to arrays, linked lists, stacks and queues which are linear data structures. A tree can be empty with no nodes or a tree is a structure consisting of one node called the root and zero or one or more subtrees.

---

## Binary Search Tree

>A BST is a binary tree where nodes are organized in the following way:

> * each node contains one key (data)
> * the keys in the left subtree are less than the key in its parent node: L < P
> * the keys in the right subtree are greater than the key in its parent node: P < R
> * duplicate keys are not allowed

> If tree is empty, then newly inserted node becomes root.
Next inserted node's key is compared to parent's key. If less, then it will be inserted in left child of root. Else, in right child of root. If a newly inserted node seeks insertion in an already occupied left or right child of root, then it's key is compared to root's key. If less, then it moves down left and it's key is compared to the root's left child node's key. Else, it moves down right and it's key is compared to the root's right child node's key

#### Big O

###### Time Complexity

| Average | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (log n) | O (log n) | O (log n)| O (log n) |

| Worst   | | | |
| :---: | :---: | :---: | :---: |
| Access | Search | Insertion | Deletion |
| O (n) | O (n) | O (n)| O (n) |

###### Space Complexity

|Worst|
| :---: |
| O (n)|

#### Implementation
[binary_search_tree.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/BST/binary_search_tree.py)

---

## Graphs

>A graph is an abstract data type comprised of a set of vertices and another of
edges. Each edge connects two vertices and may be one-way (directed graph)
or two-way. Moreover, each edge can be weighted, indicating a cost to go from
one vertex to another. A path is a sequences of vertices that are connected by
edges. A cycle is a path that starts and ends on the same vertex. A graph with
no cycles is called an acyclic graph. A directed graph with no cycles is called
a directed acyclic graph or a DAG.

#### Big O

###### Time Complexity

| Adjacency List | | | | |
| :---: | :---: | :---: | :---: | :---: |
| Add vertex | Add edge | Remove vertex | Remove edge | Query |
| O (1) | O (1) | O (V + E)| O (E) |O (V) |

| Adjacency Matrix | | | | |
| :---: | :---: | :---: | :---: | :---: |
| Add vertex | Add edge | Remove vertex | Remove edge | Query |
| O (V^2) | O (1) | O (V^2)| O (1) |O(1)|

###### Space Complexity

|Adjacency List| Adjacency Matrix|
| :---: | :---: |
| O (V + E)|O (V^2)|

#### Implementation
[adjacencylist.py](https://github.com/kiraheta/data-structures-and-algorithms/blob/master/data%20structures/graph/adjacencylist.py)

---

### References

http://interactivepython.org/runestone/static/pythonds/index.html

https://en.wikibooks.org/wiki/Data_Structures
