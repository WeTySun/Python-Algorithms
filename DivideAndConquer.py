""" Divide and Conquer find number by using three steps:
Divide/break - breaking problem into smaller sub-problems
Conquer/solve - receives smaller sub-problems and problems solved on their own
Merge/Combine - smaller sub-problems are solved and this method recursively formulate a solution of the original problem
"""

# creating binary search function

def bs(list, val):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size
# finding the middle value
    while idx0 <= idxn:
        midval = (idx0 + idxn)

        if list[midval] == val:
            return midval
# comparing the value the middle value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    if idx0 > idxn:
        return None

# creating sorted list
l = [3,5,34,45,75,96]

# printing the search result

print(bs(l,75))
print(bs(l,2))
