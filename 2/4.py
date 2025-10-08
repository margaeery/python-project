def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)


try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    print(f"НОД({num1}, {num2}) = {gcd(num1, num2)}")
except ValueError:
    print("Ошибка! Пожалуйста, введите целые числа.")
