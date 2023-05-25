#Divide and conquer algorithm 
#O(n*log(n)) running time (optimal)

#How it works:
#split the arrays into halves until they can't be split anymore (stops at 1 element in a sub array)
#Once the arrays and sub arrays are fully split, then its time to compare the last sub arrays with each other and sort them into a new array


def merge_sort(arr):

    if len(arr) > 1:
        left_arr = arr[ : len(arr)//2] #obtain the elements of the array from index 0, to the middle index of the array 
        right_arr = arr[len(arr)//2 : ] #obtain the elements of the array from the middle index until the end of the array

        #Keep splitting the arrays recursively till it can't be split anymore
        merge_sort(left_arr)
        merge_sort(right_arr)


        i = 0 #left array index
        j = 0 #right array index
        k = 0 #merged array index


        while i < len(left_arr) and j < len(right_arr):
            
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i+= 1
            else:
                arr[k] = right_arr[j]
                j+=1
            k+=1


        #insert every element into the merged array that was left over from the left array since there is nothing to compare it to 
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i+=1
            k+=1
        

        #insert every element into the merged array that was left over from the right array since there is nothing to compare it to 
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j+=1
            k+=1


def main():
    arr = [2,3,5,1,7,4,4,4,2,6,0]
    merge_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()