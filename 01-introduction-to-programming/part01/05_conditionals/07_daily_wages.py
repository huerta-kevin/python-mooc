# Please write a program which asks for the hourly wage, hours worked, and the day of
# the week. The program should then print out the daily wages, which equal hourly
# wage multiplied by hours worked, except on Sundays when the hourly wage is
# doubled.

# Hourly wage: 8.5
# Hours worked: 3
# Day of the week: Monday
# Daily wages: 25.5 euros

# Hourly wage: 12.5
# Hours worked: 10
# Day of the week: Sunday
# Daily wages: 250.0 euros

# Write your solution here
wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")

if day_of_week == "Sunday":
    wage *= 2

total_wage = wage * hours_worked
print(f"Daily wages: {total_wage} euros")
