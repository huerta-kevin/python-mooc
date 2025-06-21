# Please write a program which asks the user for two numbers and an operation. If the
# operation is add, multiply or subtract, the program should calculate and print out the
# result of the operation with the given numbers. If the user types in anything else, the
# program should print out nothing.
#
# Some examples of expected behaviour:

# Number 1: 10
# Number 2: 17
# Operation: add
#
# 10 + 17 = 27

# Number 1: 4
# Number 2: 6
# Operation: multiply
#
# 4 * 6 = 24

# Number 1: 4
# Number 2: 6
# Operation: subtract
#
# 4 - 6 = -2

# Write your solution here
number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

add = number1 + number2
multiply = number1 * number2
subtract = number1 - number2

if operation == "add":
    print(f"{number1} + {number2} = {add}")

if operation == "multiply":
    print(f"{number1} * {number2} = {multiply}")

if operation == "subtract":
    print(f"{number1} - {number2} = {subtract}")
