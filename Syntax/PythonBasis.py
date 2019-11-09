# print("Hello World")

#Indentation
# if 5 > 2:#not semicolon, it's colon
    # print("Five is greater than two!!!!!!!!")

"""
This is one way to add multiline comment in python file.
Python ignore string not assigned to a variable.

jnisbnuisgnisgnsogvnosjn
sgnjsngsjgnksngksjngs
nsognsngjsnglsngksng
nsfgnsognosljng
"""

#declare
#Variables do not need to be declared with any particular
#type and can even change type after they have been set.
# N = 5
# y = "John"
# print(y)

#A variable cannot start with a number
# x = y = z = "AAAHhhhhhhhhh"
# print(x)
# print(y)
# print(z)
#
# print("I'd to yeal " + z)
#cannot print str and num togather without type change
# print("Your score is: " + str(N))

# x = 3 + 5j #type: conplex
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))

# import random
#
# print(random.randrange(1, 10))

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
#
# print(a)

# Get the characters from position 2 to position 7 (not included):
# a = "Hello,world"
# print(a[2])
# print(a[2:7])

# Negative indexing
# b = "Hello,world"
# print(b[-11:-5])

# a = "Hello,world"
# print(len(a))

# The strip() method removes any whitespace from the beginning or the end:
# a = " abcde "
# print(a)
# print(a.strip())

#---------------
#Operators
#-----------------

"""
x = 0100111010;
y = 1001101010;
z = x|y;
z == 1101111010;
"""

# x = 5
# x **=3 # x to the power of 3
# print(x)

# x = 5
# x = x | 3 # Bitwise OR
# #
# # 5: in binary 101
# # 3: in binary 11
# # So x gonna be 111, which is 7 in decimal number
# print(x)

# x = 13 # 110 in binary
# x ^= 12# Bitwise XOR
# print(x)


#List
# list1 = ["apple", "banana", "cherry"]
# print(list1[1])
# list1[1] = "blackberry"
# print(list1[1])
#
# if "apple" in list1:
#     print("apple is in the list")
#
# list1.append("orange")
# print(list1)
#
# list1.remove("blackberry")
# print(list1)
#
# # del list
# # list.clear()
#
# list2 = list1.copy()
# print(list2)
#
# list3 = list(list1)
# print(list3)

#Set
# set1 = {"apple", "banana", "cherry"}
# print(set1)

#Dictionaries
# dict1 = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# print(dict1["year"]) # print the value
# dict1["year"] = 2018
#
# print(dict1["year"])

# if "model" in dict1:
#     print("model exists as one of keys")

#Add items
# dict1["color"] = "blue"
# print(dict1)

#Remove items
# dict1.pop("model")
#or
# del dict1["model"]

#Delete dictionaries
# del dict1

#Loop through a dictionary key
# for x in dict1:
#     print(x)

#Loop through a dictionary value
# for x in dict1:
#     print(dict1[x])

#Loop through both keys and values
# for x, y in dict1.items():
#     print(x, y)
