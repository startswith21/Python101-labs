# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.
# will enter eg 5999, break or continue 
user_input = int(input("Enter number between 0 and 1000000000: "))
guess = 0

while user_input != guess:
    guess += 1
    if guess == user_input:
        print(f"Found it! It is: {guess}")

    

