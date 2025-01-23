class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Converts Celsius to Fahrenheit."""
        return (celsius * 9/5) + 32

    # @classmethod
    # def info(cls):
    #     """Returns a message about temperature conversions."""
    #     return "This class provides methods to convert temperatures between Celsius and Fahrenheit."

# Example usage
if __name__ == "__main__":
    # Convert Celsius to Fahrenheit
    print(TemperatureConverter.celsius_to_fahrenheit(21))  # Output: 77.0

    # Get information about the class
    #print(TemperatureConverter.info())  # Output: This class provides methods to convert temperatures between Celsius and Fahrenheit.