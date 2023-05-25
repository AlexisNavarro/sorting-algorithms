#Running times
#build the max_heapify is big O(log(n))
#create and build heap is big O(n)
#final time complexity of heap sort is big O(n*log(n))

#how it works:
#this is essentially used for binary trees specifically when you want to sort them, in this heap sort implementation I implemented a max heap rather than a min heap.
#the max heap will be comparing the root node with the child and in this case the root node shall be always greater than the left most children nodes.
#while the right child nodes will be always greater than the root node and the left child nodes.

def max_heapify(arr, size, i):

    largest = i #root
    left = 2 * i + 1
    right =  2 * i + 2

    #compare the left child from the root, if its greater than the root then we change the root value
    if left < size and arr[i] < arr[left]:
        largest = left
    
     #compare the right child from the root, if its greater than the root then we change the root value
    if right < size and arr[largest] < arr[right]:
        largest = right

    #actual swapping of values is done to the array 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        max_heapify(arr, size, largest) #only called when the parent is changed, which we can now sort with the new root 



def heap_sort(arr):
    size = len(arr)

    #build max heap
    #first argument, starts at the middle index, second argument checks that the value of i is greater than -1, last argument decrements minus 1.
    for i in range(size//2 - 1, -1, -1):  
        max_heapify(arr, size, i)
    
    #extract all the elements one by one and swap
    for i in range(size-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] #swap with the root element after each call is done
        max_heapify(arr, i, 0)


def main():
    arr = [10,12,13,1,2,6]
    heap_sort(arr)

    for i in range(len(arr)):
        print(arr[i])


if __name__ == '__main__':
    main()