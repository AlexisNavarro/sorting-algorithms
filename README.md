# sorting-algorithms
The purpose of this sorting algorithms is for me to be able to demonstrate my knowledge on sorting algorithm concepts while also re-establishing the basic fundamentals of sorting algorithms.

## Bubble Sorting

## Insertion Sort

## Quick Sort

A **Divide and Conquer** algorithm!
Running time:
* big O(n^2) worst case
* big O(n*log(n)) best and worst case


How it works:
Quick sort works by allowing us to sort an array by dividing the array into 2 using a pivot which can be selected randomly or by a user once the pivot is selected, we need to find the values that are greater and less than the pivot, once that is found then we now have to  swap the greater value and the less than value with each other. Eventually, there will be a need where the pivot needs to be repositioned when the there is a value greater to the pivot itself and that would occur normally at the end once the values swapped from before is done. This algorithm will be using recursion being that its the best fit to use in divide and conquer algorithms.

## Selection Sort

To be able to do selection sorting, we have keep track of a minimum index which will be the starting value of the array(this value will switch as we move one), when we find a value smaller than the value in the minimum value then we declare that value to the position that we found a smaller value once that is done, we then swap the positions of the current value we are located at to the smallest value we found.
