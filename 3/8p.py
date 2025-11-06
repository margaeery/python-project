class Person:
    def __init__(self):
        self._name = ""
        self._age = 0
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Имя не может быть пустым")
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise ValueError("Возраст должен быть числом")
        if value < 0 or value > 150:
            raise ValueError("Возраст должен быть от 0 до 150")
        self._age = value


person = Person()

while True:
    print("\n1 - Ввести имя")
    print("2 - Ввести возраст")
    print("3 - Показать информацию")
    print("4 - Выйти")
    
    choice = input("Выберите действие: ")
    
    if choice == "1":
        name = input("Введите имя: ")
        try:
            person.name = name
            print("Имя сохранено")
        except ValueError as e:
            print(f"Ошибка: {e}")
    
    elif choice == "2":
        try:
            age = int(input("Введите возраст: "))
            person.age = age
            print("Возраст сохранен")
        except ValueError as e:
            print("Возраст должен быть числом от 0 до 150")
    
    elif choice == "3":
        print(f"Имя: {person.name}")
        print(f"Возраст: {person.age}")
    
    elif choice == "4":
        print("Выход")
        break
    
    else:
        print("Неверный выбор")
