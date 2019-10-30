#If the item is present, the best case is O(1), the average case is O(n/2), and the worst case is O(n).

def sequential_search(seq, n):
    for item in seq:
        if item == n: return True
    return False

def test_sequential_search(module_name = 'this module'):
    seq = [1, 5, 6, 8, 3]
    n1 = 5
    n2 = 7
    assert(sequential_search(seq, n1) == True)
    assert(sequential_search(seq, n2) == False)

    s = 'Tests in {name} have {con}!'
    print(s.format(name=module_name, con='passed'))

if __name__ == '__main__':
    test_sequential_search()
