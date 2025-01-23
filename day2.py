# Get user input
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")


# Get user input
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print(f"The number {number} is positive.")
elif number < 0:
    print(f"The number {number} is negative.")
else:
    print("The number is zero.")


# Get marks from the user
marks = float(input("Enter the marks: "))

# Determine the grade based on the grading scale
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Display the grade
print(f"The grade for marks {marks} is: {grade}")





