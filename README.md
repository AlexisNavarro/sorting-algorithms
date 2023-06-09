# sorting-algorithms
The purpose of this sorting algorithms is for me to be able to demonstrate my knowledge on sorting algorithm concepts while also re-establishing the basic fundamentals of sorting algorithms.

## Bubble Sorting

In bubble sort, this algorithm compares the current value to the one next to it if the current value is greater than the adjacent value, then we swap their places in the list in the case that the current value is less than the next, then we need to compare the next value along with the values adjacent to it.

## Insertion Sort

The purpose of insertion sort is to be able to sort an array by selecting an index and comparing it to the values before it
if we find a value that is greater than the current value in our current index, then we INSERT the current value before the greater value.

Running Time:
* big O(n^2)
## Quick Sort

A **Divide and Conquer** algorithm!


Quick sort works by allowing us to sort an array by dividing the array into 2 using a pivot which can be selected randomly or by a user once the pivot is selected, we need to find the values that are greater and less than the pivot, once that is found then we now have to  swap the greater value and the less than value with each other. Eventually, there will be a need where the pivot needs to be repositioned when the there is a value greater to the pivot itself and that would occur normally at the end once the values swapped from before is done. This algorithm will be using recursion being that its the best fit to use in divide and conquer algorithms.

Running time:
* big O(n^2) worst case
* big O(n*log(n)) best and worst case

## Selection Sort



To be able to do selection sorting, we have keep track of a minimum index which will be the starting value of the array(this value will switch as we move one), when we find a value smaller than the value in the minimum value then we declare that value to the position that we found a smaller value once that is done, we then swap the positions of the current value we are located at to the smallest value we found.


## Merge Sort

A **Divide and Conquer** algorithm!

To be able to do merge sort, you first need to be able to Split the arrays into halves until they can't be split anymore (stops at 1 element in a sub array). Once the arrays and sub arrays are fully split, then its time to compare the last sub arrays with each other and sort them into a new array

Running time:
* big O(n*log(n)) optimal running time 

## Heap Sort

Heap sort is essentially used for binary trees specifically when you want to sort them, in this heap sort implementation I implemented a max heap rather than a min heap. The max heap will be comparing the root node with the child and in this case the root node shall be always greater than the left most children nodes. while the right child nodes will be always greater than the root node and the left child nodes.

Running times:
* Build the max_heapify is big O(log(n))
* Create and build heap is big O(n)
* Final time complexity of heap sort is big O(n*log(n))
