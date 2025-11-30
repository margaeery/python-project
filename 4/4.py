from functools import reduce


def factorial(n):
    if n < 0:
        return None
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)


print(factorial(-5))
print(factorial(0))
print(factorial(5))
