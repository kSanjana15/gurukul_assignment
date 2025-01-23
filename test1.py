# x = 1
# y = 1.0
# z = "1"
# print (x , type(x))
# print(y , type(y))
# print(z , type(z))
#
# x = 2
# y = 2.0
# z = "2"
# print (x , type(x))
# print(y , type(y))
# print(z , type(z))
#
# a=b=c=10
# print(a,b,c)
#
# a=11
# b=12
# print(a+b)
# from pickle import FALSE
from turtle import TurtleGraphicsError


# fruits = ["apple", "banana", "cherry" , "mango" , "apple2"]
# print (fruits[1],fruits[3])

# numbers = [10, 20, 30, 40, 50]
# numbers.insert(2,35)
# print(numbers)

# tpl1 = ("red", "green", "blue")
# print(tpl1[0],tpl1[2])

# tpl2 = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# print(len(tpl2))


# dict1 = {"Alice": 85, "Bob": 90, "Charlie": 78}
# print(dict1.get("Bob"))
# dict1["David"] = dict1.pop("Charlie")
#dict2 = {"David" :92}
#dict3 = (dict1 | dict2)
# print(dict1)
#dict3['Bob']  =  "95"
#print(dict3)
# if 'Bob' in dict1.keys():
#     print("Bob is there")
# else:
#     print("No Bob is not here")
# dict1_len = len(dict1)
# print(dict1_len)



class student:
    def __init__(self):
        self.name = False
        self.clas = False
        self.roll = False

    def enroll(self):
        self.name = True
        self.clas = True
        self.roll = True
        print("enroll done...")

student1 = student()
student1.enroll()
