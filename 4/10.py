numbers = [1, 2, 3, 4, 5]

result1 = list(map(lambda x: x + 10, numbers))
result2 = list(map(lambda x: x*3, result1))

result3 = list(map(lambda x: x ** 2, numbers))
result4 = list(map(lambda x: x/2, result3))

print("numbers", numbers)
print("x+10:", result1)
print("(x+10)*3:", result2)
print("x**2:", result3)
print("x**2/2:", result4)
