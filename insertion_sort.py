
#big O(n^2)
#
def insertion_sort(arr):
    for i in range(1, len(arr)): #start at index 1 and move to the right
        j = i 
        while arr[j-1] > arr[j] and j > 0: #iterate the list to the left but don't go less than 0
            arr[j-1], arr[j] = arr[j], arr[j-1] #swap values
            j-=1 


def main():
    arr = [11,9, 29, 7, 2, 15, 28]
    insertion_sort(arr)
    print(arr)
    

if __name__ == '__main__':
    main()