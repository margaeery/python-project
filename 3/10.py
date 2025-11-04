class NumberIterator:
    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError("Шаг не может быть равен нулю")
        if (step > 0 and start > end) or (step < 0 and start < end):
            raise ValueError("Неверное направление последовательности")
            
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current > self.end:
            raise StopIteration
        if self.step < 0 and self.current < self.end:
            raise StopIteration
            
        result = self.current
        self.current += self.step
        return result


def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: Введите целое число")


start = get_integer_input("Введите начальное число: ")
end = get_integer_input("Введите конечное число: ")
step = get_integer_input("Введите шаг: ")

print(f"\nПоследовательность от {start} до {end} с шагом {step}:")
try:
    iterator = NumberIterator(start, end, step)
    for number in iterator:
        print(number, end=" ")
    print()
except ValueError as e:
    print(f"Ошибка: {e}")
