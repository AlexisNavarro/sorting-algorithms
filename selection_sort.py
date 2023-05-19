#Big O n^2

#to sort, we have keep track of a minimum index which will be the starting value of the array(this value will switch as we move one),
#when we find a value smaller than the value in the minimum value then we declare that value to the position that we found a smaller value
#once that is done, we then swap the positions of the current value we are located at to the smallest value we found.


def selection_sort(arr):
    size = len(arr)

    for i in range(size): 
        cur_min_indx = i #store the first index position as our current minimum
        for j in range(i+1, size): #start at the next index and stop at the last index
            if arr[j] < arr[cur_min_indx]:
                cur_min_indx = j

        #swap
        arr[i], arr[cur_min_indx] = arr[cur_min_indx], arr[i]

def main():
    arr = [2,6,5,1,3,4]
    selection_sort(arr)
    print(arr)
if __name__ == '__main__':
    main()