#Condition and statement


a = 300
b = 400
c = 150
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")

#If only one of statement to excute, we can put togather
# if a == b: print("YEAHHHHHHHHH !!!!!!!!!!!")
# print("b is greater than a") if b > a else print("a is greater than b")
#or
print("b is greater than a") if b > a else print("a and b are equal") if a == b else print("a is greater than b")

# if a > b and c > a:
#     print("Both condtions are true!!!!!")

# if a > b or c > a:
#     print("one of the condtions are true!!!!!")


fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(x)
#
# for x in "apple":
#     print(x)
#
# for x in fruits:
#     print(x)
#     if x == "banana":
#         break
#
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# for x in fruits[0:2]:# Specify the range in the list
#     print(x)


#With continue statement, we can skip the iteration and go next
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)

#Specify the range

fruits2 = ["apple", "banana", "cherry", "berry", "melon", "grape"]

# for x in range(4): # 0 - 3
#     print(x)
#
# for x in range(2, 9): # 2 - 8
#     print(x)
#
# for x in range(2, 30, 3): #Specify the increment value by adding a third parameter
