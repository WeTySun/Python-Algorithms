#  recursion algorithm call itself
# creating binary search function with recursion method

def bs(l, index0, indexn, value):
    if (indexn < index0):
        return None
    else:
        middlevalue = index0 + ((indexn - index0))

        if l[middlevalue] > value:
            return bs(l,index0,middlevalue - 1, value)
        elif l[middlevalue] < value:
            return bs(l,middlevalue + 1, indexn, value)
        else:
            return middlevalue

l = [8,11,24,56,88,131]
print(bs(l,0, 5, 11)) # from 0 to 5 value 11 at 1
print(bs(l, 0, 5, 100)) # from 0 to 5 value 100 at None
