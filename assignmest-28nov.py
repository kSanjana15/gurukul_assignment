class MathOperations:
    @staticmethod
    def add_numbers(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @staticmethod
    def multiply_numbers(a, b):
        """Returns the product of two numbers."""
        return a * b

# Example usage
if __name__ == "__main__":
    # Using the static methods without creating an instance
    print(MathOperations.add_numbers(5, 3))  # Output: 8
    print(MathOperations.multiply_numbers(5, 3))  # Output: 15