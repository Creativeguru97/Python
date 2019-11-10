#Functions


# def my_function():
#     print("Hello from a function")
#
# def another_function():
#     print("Hello from another function")
#
# another_function()

# def my_function(name):
#     print("Hello from a " + name)
#
# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# Setting dafalt value
# def country(country = "Norway"):
#     print("Hello from a " + country)
#
# country("Sweden")
# country("India")
# country()
# country("Brazil")


# Passing a list as a Parameter
# def fruits(name):
#     for x in name:
#         print(x)
#
# fruitsname = ["apple", "banana", "cherry"]
# fruits(fruitsname)
# print(fruitsname)


#Return values
# def number(x):
#     return 5 * x
# print(number(3))
# print(number(32))

#Argue multiple arguements
# def number(x, y):
#     return x * y
# print(number(3, 5))
# print(number(32, 10))

#Recursion
# def recursiveFunction(k):
#     if(k > 0):
#         result = k + recursiveFunction(k - 1)
#         print(result)
#     else:
#         result = 0
#         print(result)
#     return result
#
# recursiveFunction(6)

# def recursiveFunction(k):
#     if(k > 0):
#         result = k
#
#         #---This order of two lines below is the key to change order ---
#         print(result)
#         recursiveFunction(k - 1)
#         #---This order of two lines above is the key to change order ---
#     else:
#         result = 0
#         print(result)
#     return result
#
# recursiveFunction(5)


#Lambda
#A lambda function can take any number of
# arguments, but can only have one expression.

#Syntax: lambda arguments: an expression

x = lambda a, b: a * b
print(x(4, 5))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
