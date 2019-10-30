"""Linear searching algorithm works very simple it search item one by one, checks every item if given item founded
it returns, otherwise algorithm cotinues to find given item."""

def linearSearch(val, search):
    search_at = 0
    search_res = False

    while search_at < len(val) and search_res is False:
        if val[search_at] == search:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res


l = [1,2,3,4,5,6,7,8,9,10]

print(linearSearch(l, 7))

print(linearSearch(l, 11))
