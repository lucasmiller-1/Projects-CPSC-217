# This is a program that reads an age in human years and converts it to dog years using a more accurate conversion.
# First read the users age in human years.

age = float(input("Enter an age in human years: "))

# Then use the updated conversion and convert to dog years.
# Print the results.
# The instructions specify to loop program until a value less than 0 is entered.

while age >= 0:
    if age <= 2:
        dogyears = age * 10.5
    else:
        dogyears = 2 * 10.5 + (age-2) * 4
    
    print("That's equal to ", dogyears, "dog years.")

    age = float(input("Enter an age in human years: "))






