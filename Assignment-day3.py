def max_of_three(num1, num2, num3):
    """Return the maximum of three numbers."""
    return max(num1, num2, num3)

# Example usage
result = max_of_three(10, 20, 15)
print("The maximum number is:", result)

def multiply_list(numbers):
    """Multiply all numbers in the given list."""
    result = 1
    for num in numbers:
        result *= num
    return result

# Example usage
sample_list = (8, 2, 3, -1, 7)
output = multiply_list(sample_list)
print("The product of the numbers is:", output)

def reverse_string(s):
    """Return the reversed version of the input string."""
    return s[::-1]

# Example usage
sample_string = "1234abcd"
reversed_string = reverse_string(sample_string)
print("Reversed string is:", reversed_string)


def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
try:
    number = 10
    print(f"The factorial of {number} is: {factorial(number)}")
except ValueError as e:
    print(e)



def distinct_elements(input_list):
    """Return a new list with distinct elements while maintaining order."""
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

# Example usage
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = distinct_elements(sample_list)
print("Unique List:", unique_list)




def is_prime(num):
    """Check if the number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage
number = 37
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")



def even_numbers(input_list):
    """Return a list of even numbers from the given list."""
    return [num for num in input_list if num % 2 == 0]

# Example usage
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = even_numbers(sample_list)
print("Even numbers:", result)


def count_case_letters(input_string):
    """Count the number of uppercase and lowercase letters in the given string."""
    upper_count = 0
    lower_count = 0

    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count


# Example usage
sample_string = 'The quick Brow Fox'
upper_count, lower_count = count_case_letters(sample_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)


def sum_of_list(numbers):
    """Return the sum of all numbers in the given list."""
    return sum(numbers)

# Example usage
sample_list = [1, 2, 3, 4, 5]
total = sum_of_list(sample_list)
print("The sum of the numbers in the list is:", total)



def is_palindrome(s):
    """Check if the passed string is a palindrome."""
    # Normalize the string: remove spaces and convert to lowercase
    normalized_str = ''.join(s.split()).lower()
    # Check if the string is equal to its reverse
    return normalized_str == normalized_str[::-1]

# Example usage
sample_string = "A man a plan a canal Panama"
if is_palindrome(sample_string):
    print(f'"{sample_string}" is a palindrome.')
else:
    print(f'"{sample_string}" is not a palindrome.')