students = {"Alice": 85, "Bob": 90, "Charlie": 78}
print(students)


students = {"Alice": 85, "Bob": 90, "Charlie": 78}
bobs_grade = students["Bob"]
print("Bob's grade:", bobs_grade)


students = {"Alice": 85, "Bob": 90, "Charlie": 78}
# Add a new student
students["David"] = 92
# Remove "Charlie"
students.pop("Charlie")
print(students)


students = {"Alice": 85, "Bob": 90, "Charlie": 78}
students["Bob"] = 95
print(students)


students = {"Alice": 85, "Bob": 90, "Charlie": 78}
if "Alice" in students:
    print("Yes, 'Alice' is a key in the dictionary.")
else:
    print("No, 'Alice' is not a key in the dictionary.")


students = {"Alice": 85, "Bob": 90, "Charlie": 78}
length = len(students)
print("Number of key-value pairs in the dictionary:", length)


