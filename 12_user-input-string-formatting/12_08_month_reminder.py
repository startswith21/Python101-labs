# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.
# link number with month

user_input = int(input("Enter a number between 1 and 12: "))
if user_input > 12 or user_input < 1:
    print("Error")
if user_input <=12 and user_input >= 1:
    if user_input == 1:
        print("January")
    if user_input == 2:
        print("February")
    if user_input == 3:
        print("March")
    if user_input == 4:
        print("April")
