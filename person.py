class Person:
    # Class variable to track the number of instances
    count = 0

    def __init__(self):
        """Initializes a new instance of Person and increments the count."""
        Person.count += 1

    @classmethod
    def get_count(cls):
        """Returns the current count of instances."""
        return cls.count

# Example usage
if __name__ == "__main__":
    # Create instances of Person
    person1 = Person()
    person2 = Person()
    person3 = Person()
    person4 = Person()

    # Get the current count
    print(Person.get_count())  # Output: 4