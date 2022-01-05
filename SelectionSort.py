# Selection Sort
# Goes through list to find minimum and puts it at the beginning, skips sorted portion and repeats until list is sorted
# Time Complexity: O(n^2)
#   - Cycle 1: n-1
#   - Cycle 2: n-2
#   - Last cycle: 1
#   - (n-1) + (n-2)... + 3 + 2 + 1 = (n(n-1))/2 = n^2


# Selection Sort
def SelectionSort(array):

    # Loop through array
    for current in range(len(array)):
        # Set first element as min
        min = current
        # Loop through portioned array (excluding previous min values in the beginning)
        for i in range(current+1, len(array)):
            # If the current element index is less than the min element index
            if array[i] < array[min]:
                # Set min index to current element index
                min = i
                #print(array[min])

        # Swap current with min value
        temp = array[current]
        array[current] = array[min]
        array[min] = temp
        print(array[current])

# TESTING

# Initialize array
array = [8,2,5,1,6,3]

# Selection Sort
SelectionSort(array)
print(array)
                

