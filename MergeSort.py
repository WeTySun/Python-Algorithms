# Merge Sort divides array into equal halves then compare them and make them in order

def merge_sort(unordered): # Define merge sort function
    if len(unordered) <= 1: # If list empty
        return unordered
# Find the middle point and devide it
    middle = len(unordered) // 2
    left_list = unordered[:middle] # Finding point in left side
    right_list = unordered[middle:] # Finding point in right side

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_h,right_h):

    res = []
    while len(left_h) != 0 and len(right_h) != 0:
        if left_h[0] < right_h[0]:
            res.append(left_h[0])
            left_h.remove(left_h[0])
        else:
            res.append(right_h[0])
            right_h.remove(right_h[0])
    if len(left_h) == 0:
        res = res + right_h
    else:
        res = res + left_h
    return res

unordered = [100, 34, 5, 75, 45, 3, 2]

print(merge_sort(unordered))
