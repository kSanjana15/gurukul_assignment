class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")

# Example usage
student = Student("Alice", 101, 95)
student.display_info()


class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth

    def calculate_perimeter(self):
        return 2 * (self.length + self.breadth)

# Example usage
rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)

print(f"Rectangle 1 - Area: {rect1.calculate_area()}, Perimeter: {rect1.calculate_perimeter()}")
print(f"Rectangle 2 - Area: {rect2.calculate_area()}, Perimeter: {rect2.calculate_perimeter()}")



import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_circumference(self):
        return 2 * math.pi * self.radius

# Example usage
circle = Circle(7)
print(f"Circle - Area: {circle.get_area():.2f}, Circumference: {circle.get_circumference():.2f}")







class Account:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.balance = balance

    def debit(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Debited {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def credit(self, amount):
        self.balance += amount
        print(f"Credited {amount}. New balance: {self.balance}")

    def print_balance(self):
        print(f"Account No: {self.account_no}, Balance: {self.balance}")

# Example usage
account = Account(12345, 1000)
account.credit(500)
account.debit(300)
account.print_balance()





class Employee:
    employee_count = 0

    @classmethod
    def increment_employee_count(cls):
        cls.employee_count += 1

    def __init__(self, name):
        self.name = name
        Employee.increment_employee_count()

# Example usage
emp1 = Employee("Alice")
emp2 = Employee("Bob")
print(f"Total Employees: {Employee.employee_count}")





class Book:
    def __init__(self, title, author, price=0.0):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: ${self.price:.2f}")

# Example usage
book1 = Book("Python Programming", "John Doe", 29.99)
book2 = Book("Learn Python", "Jane Smith")
book1.display_details()
book2.display_details()







