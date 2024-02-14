# Задача 1
class Human:
    def __init__(self, name, surname, age, id_number, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.id_number = id_number
        self.address = address

class Student(Human):
    def __init__(self, name, surname, age, id_number, address, group_number, specialty, grades):
        super().__init__(name, surname, age, id_number, address)
        self.group_number = group_number
        self.specialty = specialty
        self.grades = grades

    def calculate_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        print("Student:", self.name, self.surname)
        print("Age:", self.age)
        print("ID:", self.id_number)
        print("Address:", self.address)
        print("Group Number:", self.group_number)
        print("Specialty:", self.specialty)
        print("Grades:", self.grades)

class Staff(Human):
    def __init__(self, name, surname, age, id_number, address, position, department):
        super().__init__(name, surname, age, id_number, address)
        self.position = position
        self.department = department

    def display_info(self):
        print("Staff Member:", self.name, self.surname)
        print("Age:", self.age)
        print("ID:", self.id_number)
        print("Address:", self.address)
        print("Position:", self.position)
        print("Department:", self.department)


# Задача 2
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

    def show(self):
        super().show()
        self.make_sound()

class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

    def show(self):
        super().show()
        self.make_sound()


# Задача 3
class Transport:
    pass

class Type:
    pass

class Car(Transport, Type):
    pass

class Train(Transport, Type):
    pass

class Plane(Transport, Type):
    pass

class Cargo(Type):
    pass

class Passenger(Type):
    pass

class CarCargo(Car, Cargo):
    pass

class CarPassenger(Car, Passenger):
    pass

class TrainCargo(Train, Cargo):
    pass

class TrainPassenger(Train, Passenger):
    pass

class PlaneCargo(Plane, Cargo):
    pass

class PlanePassenger(Plane, Passenger):
    pass


# Задача 4
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def display_info(self):
        print("Figure Information:")

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        import math
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.radius

class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        import math
        s = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


# Задача 5
class CPerson:
    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def showdata(self):
        print("Name:", self.name)
        print("Surname:", self.surname)
        print("Patronymic:", self.patronymic)

class CStudent(CPerson):
    def __init__(self, name, surname, patronymic, average_grade):
        super().__init__(name, surname, patronymic)
        self.average_grade = average_grade

    def showdata(self):
        super().showdata()
        print("Average Grade:", self.average_grade)

class CProfessor(CPerson):
    def __init__(self, name, surname, patronymic, publications, position, age):
        super().__init__(name, surname, patronymic)
        self.publications = publications
        self.position = position
        self.age = age

    def showdata(self):
        super().showdata()
        print("Publications:", self.publications)
        print("Position:", self.position)
        print("Age:", self.age)


# Задача 6
class ClassX:
    def __init__(self, x):
        self.x = x

    def input_data(self):
        self.x = float(input("Enter x: "))

    def display_data(self):
        print("X:", self.x)

class ClassY:
    def __init__(self, y):
        self.y = y

    def input_data(self):
        self.y = float(input("Enter y: "))

    def display_data(self):
        print("Y:", self.y)

class ClassZ(ClassX, ClassY):
    def calculate_product(self):
        return self.x * self.y


# Задача 7
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def food_requirements(self):
        pass

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)

    def food_requirements(self):
        return "Meat"

class Omnivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def food_requirements(self):
        return "Plants and Meat"

class Herbivore(Animal):
    def __init__(self, name):
        super().__init__(name)

    def food_requirements(self):
        return "Plants"


# Задача 7a
animals = [Predator("Lion"), Omnivore("Bear"), Herbivore("Deer")]

sorted_animals = sorted(animals, key=lambda x: (x.food_requirements(), x.name), reverse=True)
for animal in sorted_animals:
    print("Name:", animal.name)
    print("Food Requirements:", animal.food_requirements())

# Задача 7b
print("\nFirst 5 animal names:")
for animal in sorted_animals[:5]:
    print(animal.name)

# Задача 7c
print("\nLast 3 animal identifiers:")
for animal in sorted_animals[-3:]:
    print(animal.name)