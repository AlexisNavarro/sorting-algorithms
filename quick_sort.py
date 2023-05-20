#Divide and Conquer algorithm
#Running time
#big O(n^2) worst case
#big O(n*log(n)) best and worst case


#How it works:
#Quick sort works by allowing us to sort an array by dividing the array into 2 using a pivot which can be selected randomly or by a user
#once the pivot is selected, we need to find the values that are greater and less than the pivot, once that is found then we now have to 
#swap the greater value and the less than value with each other. Eventually, there will be a need where the pivot needs to be repositioned
#when the there is a value greater to the pivot itself and that would occur normally at the end once the values swapped from before is done.
#This algorithm will be using recursion being that its the best fit to use in divide and conquer algorithms.

 
def quick_sort(arr, left, right):
    if left < right:
        split_pos = partition(arr, left, right)
        quick_sort(arr, left, split_pos-1) #for elements less than the pivot element aka the left sub array
        quick_sort(arr, split_pos + 1, right) #for elements greater than the pivot element aka the right sub array


def partition(arr, left, right):
    i = left #will be searching for a value greater than the pivot
    j = right - 1 #will be searching for a value less than the pivot
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i+=1 # i moves to the right
        while j > left and arr[j] > pivot:
            j-=1 #j moves to the left

        if i < j:
            arr[i], arr[j] = arr[j], arr [i] #swap the elements when they don't cross the pivot 

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i] #swap the positon at i with the pivot since pivot is arr[right]
    
    return i #return i to be able to split the array 


def main():
    arr = [22, 11, 88, 66, 55, 77, 33, 44]
    quick_sort(arr,0, len(arr)-1)
    print(arr)

if __name__ == '__main__':
    main()