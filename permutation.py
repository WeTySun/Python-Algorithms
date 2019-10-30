"""Permutation or recursion algorithm can look like rock,scissor,paper game between r(rock),s(scissors),p(paper)
they take all possible options: r,s,p - rr,rs,rp,sr,ss,sp,pr,ps,pp"""

#define permutation function

def permutation(l,s):
    if l == 1:
        return s
    else:
        return [ y + x
                 for y in permutation(1, s)
                 for x in permutation(l - 1, s)]


print(permutation(1, ["r","s","p"]))
print(permutation(2, ["r","s","p"]))
