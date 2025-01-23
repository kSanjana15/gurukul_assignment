class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        return a * b

# Example usage
print(MathOperations.add_numbers(5, 10))  # Output: 15
print(MathOperations.multiply_numbers(4, 7))  # Output: 28




class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

# Example usage
p1 = Person("Alice")
p2 = Person("Bob")
print(Person.get_count())  # Output: 2




class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return celsius * 9/5 + 32

    @classmethod
    def info(cls):
        return "This class provides methods to convert temperatures."

# Example usage
print(TemperatureConverter.celsius_to_fahrenheit(25))  # Output: 77.0
print(TemperatureConverter.info())  # Output: This class provides methods to convert temperatures.




class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

# Example usage
animal = Animal()
dog = Dog()
animal.sound()  # Output: Animal sound
dog.sound()  # Output: Bark




class Bird:
    def fly(self):
        print("Flying")

class Fish:
    def swim(self):
        print("Swimming")

class Duck(Bird, Fish):
    pass

# Example usage
duck = Duck()
duck.fly()  # Output: Flying
duck.swim()  # Output: Swimming



from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

# Example usage
circle = Circle(5)
rectangle = Rectangle(10, 4)
print(circle.area())  # Output: 78.5
print(rectangle.area())  # Output: 40




class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}, New Balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}, Remaining Balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")

# Example usage
account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
account.withdraw(1500)





class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Woof")

class Cat(Animal):
    def speak(self):
        print("Meow")

# Example usage
dog = Dog()
cat = Cat()
dog.speak()  # Output: Woof
cat.speak()  # Output: Meow




class Calculator:
    def add(self, a, b, c=0):
        return a + b + c

# Example usage
calc = Calculator()
print(calc.add(5, 10))  # Output: 15
print(calc.add(5, 10, 20))  # Output: 35




class LivingBeing:
    def breathe(self):
        print("Breathing")

class Mammal(LivingBeing):
    def walk(self):
        print("Walking")

class Human(Mammal):
    def think(self):
        print("Thinking")

# Example usage
human = Human()
human.breathe()  # Output: Breathing
human.walk()  # Output: Walking
human.think()  # Output: Thinking


