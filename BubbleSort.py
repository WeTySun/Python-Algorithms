# Bubble Sort all elements each other are compared swapped if they are not in order.

def bubblesort(list): # define bubble sort function
    for iter_num in range(len(list)-1,0,-1):
        for index in range(iter_num):
            if list[index] > list[index+1]:
                temp = list[index]
                list[index] = list[index+1]
                list[index+1] = temp



list = [19,2,31,45,6,11,121,27]
print("List before bubble sort: " + str(list))
bubblesort(list)
print("List after bubble sort: " + str(list))
