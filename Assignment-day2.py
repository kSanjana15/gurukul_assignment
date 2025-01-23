# # Input three numbers from the user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
#
# # Logic to find the maximum number
# if num1 >= num2 and num1 >= num3:
#     max_number = num1
# elif num2 >= num1 and num2 >= num3:
#     max_number = num2
# else:
#     max_number = num3
#
# # Output the maximum number
# print(f"The maximum of the three numbers is: {max_number}")


# # Input a number from the user
# number = int(input("Enter a number: "))
#
# # Check if the number is even or odd using the modulus operator
# if number % 2 == 0:
#     print(f"{number} is an even number.")
# else:
#     print(f"{number} is an odd number.")


# # Input a number from the user
# number = float(input("Enter a number: "))
#
# # Check if the number is positive, negative, or zero
# if number > 0:
#     print(f"{number} is a positive number.")
# elif number < 0:
#     print(f"{number} is a negative number.")
# else:
#     print(f"The number is zero.")



# # Input marks from the user
# marks = float(input("Enter the student's marks: "))
#
# # Determine the grade based on the marks
# if marks >= 90:
#     grade = 'A'
# elif marks >= 80:
#     grade = 'B'
# elif marks >= 70:
#     grade = 'C'
# elif marks >= 60:
#     grade = 'D'
# else:
#     grade = 'F'
#
# # Output the grade
# print(f"The student's grade is: {grade}")



# # Create and write to the file
# with open("sample.txt", "w") as file:
#     file.write("Hello, this is a sample file.")
#
# # Read and display the content from the file
# with open("sample.txt", "r") as file:
#     content = file.read()
#
# # Output the content of the file
# print("File Content:")
# print(content)




# # Open and read the file
# with open("sample.txt", "r") as file:
#     content = file.read()
#
# # Split the content into words
# words = content.split()
#
# # Count the number of words
# word_count = len(words)
#
# # Output the word count
# print(f"The number of words in the file is: {word_count}")


# # Input a number from the user
# number = int(input("Enter a number to display its multiplication table: "))
#
# # Display the multiplication table using a for loop
# print(f"Multiplication table for {number}:")
# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")