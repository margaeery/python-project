class President:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = ""
        return cls._instance
    
    def set_name(self, name):
        self.name = name
    
    def speak(self):
        return f"Президент {self.name} выступает с речью"


president1 = President()
president1.set_name("Иванов")
print("Президент 1:", president1.speak())

president2 = President()
president2.set_name("Петров")

print("\nПрезидент 1:", president1.speak())
print("Президент 2:", president2.speak())

print("\nЭто один и тот же человек?",president1 is president2)
