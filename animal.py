class Animal:
    def sound(self):
        """Prints the sound made by an animal."""
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        """Prints the sound made by a dog, overriding the Animal sound method."""
        print("Bark")

# Example usage
if __name__ == "__main__":
    # Create an Animal instance and call its sound method
    generic_animal = Animal()
    generic_animal.sound()  # Output: Animal sound

    # Create a Dog instance and call its sound method
    dog = Dog()
    dog.sound()  # Output: Bark