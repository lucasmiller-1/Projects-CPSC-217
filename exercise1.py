# A program that takes a users name and age, and converts their age in years to age in dog years.

# Read the name and age inputs from the user.

name = input("Enter your name: ")
age = int(input("Enter your age (years): "))

# Convert the given age in years to age in dog years.

dogyears = age * 7

# Report the result. Include the users given name, age in years and age in dog years in the print statement.

print("Score! It is crazy that ", name, " is ", str(age), ". That's ", str(dogyears), " in dog years! Crazy!")