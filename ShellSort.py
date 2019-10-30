"""Shell sort algorithm sort list elements away from each other, so this algorithm divides list in a half."""

def shellSort(user_list):
    
    gap = len(user_list) // 2
    while gap > 0:

        for i in range(gap, len(user_list)):
            temp = user_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and user_list[j - gap] > temp:
                user_list[j] = user_list[j - gap]
                j = j-gap
            user_list[j] = temp

# Reduce the gap for the next element

        gap = gap//2

l = [100,23,6,432,7,2,1,73]

shellSort(l)
print(l)
