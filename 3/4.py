from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    def get_info(self):
        return f"Площадь: {self.calculate_area():.2f}, Периметр: {self.calculate_perimeter():.2f}"


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("Все стороны должны быть положительными")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Треугольник с такими сторонами не существует")
        
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def calculate_area(self):
        s = self.calculate_perimeter() / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
    
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Ошибка: Число должно быть положительным")
                continue
            return value
        except ValueError:
            print("Ошибка: Введите число")


def add_shape(shape, shape_name):
    try:
        shapes.append(shape)
        print(f"{shape_name} создан")
    except ValueError as e:
        print(f"Ошибка: {e}")


shapes = []

while True:
    print("\n1 - Создать круг")
    print("2 - Создать прямоугольник")
    print("3 - Создать треугольник")
    print("4 - Создать квадрат")
    print("5 - Показать все фигуры")
    print("6 - Выйти")
    
    choice = input("Выберите действие: ")

    if choice == "1":
        radius = get_positive_number("Введите радиус: ")
        add_shape(Circle(radius), "Круг")
            
    elif choice == "2":
        width = get_positive_number("Введите ширину: ")
        height = get_positive_number("Введите высоту: ")
        add_shape(Rectangle(width, height), "Прямоугольник")
            
    elif choice == "3":
        side1 = get_positive_number("Введите первую сторону: ")
        side2 = get_positive_number("Введите вторую сторону: ")
        side3 = get_positive_number("Введите третью сторону: ")
        add_shape(Triangle(side1, side2, side3), "Треугольник")
            
    elif choice == "4":
        side = get_positive_number("Введите длину стороны: ")
        add_shape(Square(side), "Квадрат")
            
    elif choice == "5":
        for i, shape in enumerate(shapes, 1):
            print(f"{i}. {shape.__class__.__name__}: {shape.get_info()}")
                
    elif choice == "6":
        print("Выход из программы")
        break
        
    else:
        print("Неверный выбор")
