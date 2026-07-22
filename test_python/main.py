# Variable = A container for a value (string, integer, float, boolean)
#            A variable behave as if it was the value it contains

# Strings
# first_name = "p2wtkn"
# drink = "coffee"
# email = "p2wtkn@fake.com"

# print(f"I'm {first_name}")
# print(f"I like {drink}")
# print(f"Yours email is {email}")

# Integers
# age = 22
# quantity = 3
# num_of_students = 28

# print(f"You're {age} years old")
# print(f"You're buying {quantity} items")
# print(f"Your class has {num_of_students} students")

# Float
# price = 10.25
# gpa = 3.5
# distance = 5.5

# print(f"The price is {price}฿")
# print(f"My gpa is: {gpa}")
# print(f"I ran {distance}km.")

# Booleans
# is_students = True
# for_sale = False

# print(f"Are you a student?: {is_students}")
# if is_students:
#     print("You are a student.")
# else:
#     print("You are NOT a students.")

# print(f"Is it for sale?: {for_sale}")
# if for_sale:
#     print("Yes, it is.")
# else:
#     print("No, it isn't.")



# Typecasting = the process of converting a variable from one data type to another
#               str(), int(), float(), bool()

# name = "p2wtkn"
# name2 = ""
# age = 22
# gpa = 3.2
# is_students = True

# print(f"name = {name}", type(name))
# age = str(age)
# print(f"age = {age}", type(age))
# age += 1
# age += "1"
# print(age)
# age = float(age)
# print(f"age = {age}", type(age))
# gpa = int(gpa)
# print(f"gpa = {gpa}", type(gpa))
# name = bool(name)
# print(f"name = {name}", type(name))
# name2 = bool(name2)
# print(f"name2 = {name2}", type(name2))



# input() = A function that prompts the user to data
#           Return the entered data as a string

# name = input("What is your name?: ")
# age = int(input("How old are you?: "))
# or you can typecast
# age = int(age)
# age = age +1

# print(f"Hello {name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old.")

# Exercise 1 Rectangle Area Calc

# length = float(input("Enter the lenght: "))
# width = float(input("Enter the width: "))
# area = length * width

# print(f"The area is: {area} sqcm.")

# Exercise 2 Shopping Cart Program

# item = input("What item would you like to buy?: ")
# price = float(input("What is the price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"You have bought {quantity} x {item}/s")
# print(f"Your total is: {total}฿")



# Madlibs game
# word game where you create a story
# by filling in blanks with random words

# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, thing): ")
# adjective2 = input("Enter an adjective (description): ")
# verb1 = input("Enter a verb ending with 'ing': ")
# adjective3 = input("Enter an adjective (description): ")

# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")