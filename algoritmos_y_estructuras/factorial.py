def factorial(n):
    if n > 1:
        n_1 = factorial(n-1)
        print("N es : ", n, ", fact(n-1): ", n_1)
        return n * n_1
    return 1

print(factorial(5))
    # 5 * 24
    # 4 * 6
    # 3 * 2