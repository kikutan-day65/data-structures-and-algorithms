def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

res = factorial(5)
print(res)

res = factorial(3)
print(res)

res = factorial(9)
print(res)
