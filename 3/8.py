class Counter:
    def __init__(self, start=0):
        self._value = start
    
    def _validate_step(self, step_input):
        try:
            step = int(step_input)
        except ValueError:
            raise ValueError("Шаг должен быть целым числом")
        
        if step < 0:
            raise ValueError("Шаг должен быть положительным")
        
        return step
    
    def up(self, step=1):
        validated_step = self._validate_step(step)
        self._value += validated_step
        return self._value
    
    def down(self, step=1):
        validated_step = self._validate_step(step)
        self._value -= validated_step
        return self._value
    
    def reset(self):
        self._value = 0
        return self._value
    
    def get_value(self):
        return self._value



counter = Counter()

while True:
    print(f"\nТекущее значение: {counter.get_value()}")
    print("1 - Увеличить")
    print("2 - Уменьшить") 
    print("3 - Сбросить")
    print("4 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        step_input = input("На сколько увеличить? ")
        try:
            result = counter.up(step_input)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    elif choice == "2":
        step_input = input("На сколько уменьшить? ")
        try:
            result = counter.down(step_input)
            print(f"Результат: {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    elif choice == "3":
        result = counter.reset()
        print(f"Счётчик сброшен: {result}")
    
    elif choice == "4":
        print("Выход из программы")
        break
    
    else:
        print("Неверный выбор")
