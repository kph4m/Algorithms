# Bubble Sort
# Sorts a list by comparing 2 adjacent elements and swapping them if the 
# first element is less than the second element until list is sorted
# Time Complexity: O(n^2)
#   - Cycle 1: n-1
#   - Cycle 2: n-2
#   - Last cycle: 1
#   - (n-1) + (n-2)... + 3 + 2 + 1 = (n(n-1))/2 = n^2


# Bubble Sort
def BubbleSort(array):

    # Outer loop to access array elements
    for i in range(len(array)):

    # Inner loop to compare array elements
        for j in range(0,len(array) - i - 1):

            # If element > element + 1, swap
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp



# Optimized Bubble Sort
# Creates a swapped variable that indicates if list is already sorted, thus skipping over unnecessary processes
def OptBubbleSort(array):

    # Outer loop to access array elements
    for i in range(len(array)):

        # Keep track of swapped
        swapped = False

        # Inner loop to compare array elements
        for j in range(0,len(array) - i - 1):

            # If element > element + 1, swap
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
                swapped = True
    
        # If swapped = False, skip
        if swapped is False:
            print("List is already sorted")
            break


# TESTING

# Initialize Array
array1 = [5,2,7,3,1,4]
array2 = [3,7,4,9,5,2]

# Bubble Sort
BubbleSort(array1)
print(array1)

# Optimized Bubble Sort
OptBubbleSort(array2)
print(array2)