from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq)) # num ensures valid ordering
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))
    return trees[0][-1]


# To use properly algorithm:
#>>> seq = "abcdefghi"
#>>> frq = [4,5,6,9,11,12,15,16,20]
#>>> huffman(seq, frq)
#[['i', [['a', 'b'], 'e']], [['f', 'g'], [['c', 'd'], 'h']]]
