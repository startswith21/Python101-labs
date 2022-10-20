# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
usernumber = int(input("Enter number: "))
if usernumber < 1:
    print("number must be larger than 1")
if usernumber > 1000000000:
    print("number must be smaller than 1000000000")
if usernumber % 3 == 0:
    print("the number is divisible by 3")
if usernumber % 3 != 0:
    print("the number is not divisible by 3")

  