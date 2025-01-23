colors = ("red", "green", "blue")
print(colors)

colors = ("red", "green", "blue", "yellow")
first_element = colors[0]
last_element = colors[-1]
print("First element:", first_element)
print("Last element:", last_element)

colors = ("red", "green", "blue")
# Attempt to change the second element
try:
    colors[1] = "yellow"
except TypeError as e:
    print("Error:", e)


coordinates = (10, 20, 30)
x, y, z = coordinates
print("x =", x)
print("y =", y)
print("z =", z)


colors = ("red", "green", "blue")
if "blue" in colors:
    print("Yes, 'blue' is present in the tuple.")
else:
    print("No, 'blue' is not in the tuple.")


days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
length = len(days)
print("Length of the tuple:", length)


