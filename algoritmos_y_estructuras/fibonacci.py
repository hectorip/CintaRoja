# 0, 1, 1, 2, 3, 5 , 8, 13, 21, 34
# Fib(n) = Fib(n-1) + Fib(n-2)
# Fib(3) = Fib(2) + Fib(1) = 1 + 0 = 1
# Fib(4) = Fib(3) + Fib(2) = 1 + 1 = 2


def fib(n):

    if n < 2:
        return n-1
    
    return fib(n-1) + fib(n-2)

print(fib(10))
