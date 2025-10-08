def squares_dictionary(numbers):
    return {num: num * num for num in numbers}


try:
    numbers = [int(x) for x in input("Введите числа через пробел: ").split()]
    squares = squares_dictionary(numbers)
    print("Словарь квадратов:", squares)
except ValueError:
    print("Ошибка! Убедитесь, что вводите только целые числа.")
