# OOP in python!!!!!!!

#Simplest form of class in python.
# class MyClass:
#     x = 5 # Constructor?
#
# p1 = MyClass()
# print(p1.x)

#Buut..usually written in this way in real life
# class Person:
#     def __init__(this, name, age):#Built-in function (constructor)
#         this.name = name
#         this.age = age
#
#     def myFunc(this):
#         print("Hi, my name is " + this.name)
#
# p1 = Person("John", 36)
# print(p1.name)
# print(p1.age)
# p1.myFunc()
#
# p1.age = 40 # We can modify the properties like this
# print(p1.age)
#
# del p1.age # We can delete the property
# del p1 # Or delete entire p1 object

#Holy shit, I can write just like p5.js class object !!!!!!!
#It's really confortable!!!


# ----- Inheritance -----

class Person:
    def __init__(this, fname, lname):
        this.firstname = fname
        this.lastname = lname

    def printname(this):
        print(this.firstname, this.lastname)

p1 = Person("Issac", "Clerk")
p1.printname()


class Student(Person):
    pass
