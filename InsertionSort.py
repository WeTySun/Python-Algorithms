# Insertion sort algorithm in the beginning compare the two first elements, compare them and sort in correct order
# Then algorithm pick up third element and compare between previous two elements. This algorithm must be write
# in very efficient way because for longer and unsorted list it can take longer to compare each other and write
# in correct order.


def insertion_sort(inputList): # define insertion sort function
    for i in range(1, len(inputList)):
        j = i - 1
        next_element = inputList[i]


        while(inputList[j] > next_element) and (j >= 0):
            inputList[j+1] = inputList[j]
            j = j - 1
        inputList[j + 1] = next_element


l = [23,4,63,45,23,74,12,90]
insertion_sort(l)
print(l)
