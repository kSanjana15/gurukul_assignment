# Define the Car class
class Car:
    # Constructor to initialize the car attributes
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    # Method to display car details
    def display_details(self):
        print(f"Car Details:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}")

# Create an object of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Display the details of the car
my_car.display_details()