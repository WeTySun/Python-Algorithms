"""Interpolation search works searching specifically for given element. To work for this algorithm list must be
sorted."""

def interpolationsearch(val, x):
    index0 = 0
    indexn = (len(val) - 1)

    while index0 <= indexn and x >= val[index0] and x <= val[indexn]:
        mid = index0 +\
                int(((float(indexn - index0)/(val[indexn] - val[index0]))
                     * ( x - val[index0])))

        if val[mid] == x:
            return "Found " + str(x) + " at index " + str(mid)

        if val[mid] < x:
            index0 = mid + 1
    return "Searched element not in the list"



list = [1,2,3,4,5,6,7,8,9,10]

print(interpolationsearch(list, 9))
