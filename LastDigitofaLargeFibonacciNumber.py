"""Fast algorithm which prints last digit of a fibonacci numbers, even large numbers like 100: 354224848179261915075
Last digit: 5"""

def fib_last_digit(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1,n):
            a, b = b, (a+b) % 10
        print(b)

n = int(input())
fib_last_digit(n)
