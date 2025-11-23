from functools import reduce

def compose(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions)

def add_5(x):
    return x + 5

def multiply_3(x):
    return x * 3

def square(x):
    return x ** 2


composed = compose(add_5, multiply_3, square)
print(composed(2))
