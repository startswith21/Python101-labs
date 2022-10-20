# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.
#with max number of guesses
import random
target_number = random.randint(0, 10)
print(target_number)
tries = 0
user_guess = None

while user_guess != target_number and tries < 3:
    user_guess = int(input("Enter your number between 1-10: "))
    tries += 1
    if user_guess == target_number:
        print(f"You won! The number is {target_number}.")
        break
    else:
        print("Wrong number!")
        
if user_guess != target_number:
    print(f"You lost! The number is: {target_number}")