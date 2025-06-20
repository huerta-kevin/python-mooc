# This program already contains two integer variables, x and y:
# x = 27
# y = 15

# Please complete the program so that it also prints out the following:
# 27 + 15 = 42
# 27 - 15 = 12
# 27 * 15 = 405
# 27 / 15 = 1.8

# The program should work correctly even if the values of the variables are
# changed. That is, if the first two lines are replaced with this
# x = 4
# y = 9

# the program should print out the following:
# 4 + 9 = 13
# 4 - 9 = -5
# 4 * 9 = 36
# 4 / 9 = 0.4444444444444444

# Write your solution here
x = 27
y = 15

addition = (x + y)
subtraction = (x - y)
multiplication = (x * y)
division = (x / y)

print(f"{x} + {y} = {addition}")
print(f"{x} - {y} = {subtraction}")
print(f"{x} * {y} = {multiplication}")
print(f"{x} / {y} = {division}")
