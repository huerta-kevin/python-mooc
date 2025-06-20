# Please write a program which asks for the user's name and address. The
# program should also print out the given information, as follows:

# Given name: Steve
# Family name: Sanders
# Street address: 91 Station Road
# City and postal code: London EC05 6AW
# Steve Sanders
# 91 Station Road
# London EC05 6AW

# Write your solution here
first = input("Given name: ")
last = input("Family name: ")
address = input("Street address: ")
city = input("City and postal code: ")

print(first + " " + last)
print(address)
print(city)
