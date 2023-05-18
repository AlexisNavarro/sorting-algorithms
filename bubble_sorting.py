#how it works:
#in bubble sort, this algorithm compares the current value to the one next to it
#if the current value is greater than the adjacent value, then we swap their places in the list
#in the case that the current value is less than the next, then we need to compare the next value along with the values adjacent to it.

def bubble_sort(values):

    size = len(values)

    #number of times the sorting algorithm will iterate.
    for i in range(size - 1): 
        switch = False #change to true if we sort, false if we don't

        #Iterating before we get to the last value in the list, we don't want to access the last value since there is nothing more to compare it to.
        for j in range(size-1-i): 
            if values[j] > values[j+1]:
                tmp = values[j] #store the value that is greater than the next value in a temp variable.
                values[j] = values[j+1] #place the smaller value at the current postion. 
                values[j+1] = tmp #place the greater value in the next position.
                switch = True
       
        if not switch:
            break
        
def bubble_sort_transaction(accounts):
    selection = input("what do you want to sort by? name, transaction_amount, or device: ") 

    size = len(accounts)
    for i in range(size - 1):
        switched = False
        for j in range(size - 1):
            a = accounts[j][selection] #access a specific index with the given key then compare the value
            b = accounts[j+1][selection]



            if a > b:
                tmp = accounts[j]
                accounts[j] = accounts [j+1]
                accounts[j+1] = tmp
                switched = True

        if not switched:
            break


def main():


    values = [5,9,2,1,67,34,88,34]
    bubble_sort(values)
    print(values)

    elements = [1,2,3]
    bubble_sort(elements)
    print(elements)

    #will sort names since it will be comparing the first letter of the names(strings)
    names = ["jose", "alexis", "carlos", "brandon"]
    bubble_sort(names)
    print(names)


    accounts =   [
        { 'name': 'Jose',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'Alexis', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'Carlos',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'Brandon',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]

    bubble_sort_transaction(accounts)
    print("\n",accounts)

if __name__ == '__main__':
    main()