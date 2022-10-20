# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.
import sys
flag = True
while flag == True:
    print("true")
    user_choice = input("You can enter 'quit' if you want to get out: ")
    if user_choice == "quit":
        break
    
