# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game.
sword = False
play = True
while play == True:
    print("Welcome to the 'Dungeons and Dragons' Game!")
    user_name = str(input("Enter your name: "))
    print(f"Hello {user_name}! You are now entering the dungeon...\n"
       "In the hallway you are seeing two closed doors. Which room are you going to enter? The left one or the right one?")
    user_dec = str(input("Enter 'left' or 'right': ")).lower().strip()
    if user_dec == "left":
        user_dec = str(input("This room appears to be empty. Do you want to have a closer look or go back to the hallway?\n" 
    "Enter 'look around' or 'go back': ")).lower().strip()
        if user_dec == "look around":
            sword = True
            user_dec = str(input("You found a magic sword! Take it! Do you want to enter the other room? Enter 'yes' or 'no': "))
            if user_dec == "yes":
              user_dec = str(input("There is a dragon standing right in front of you! Do you want to fight it? Enter 'yes' or 'no':")).lower().strip()
              if user_dec == "yes" and sword == True:
                  print("You won, you defeated the dragon!")
              if user_dec == "no":
                  print("You are back in the hallway.")
                  

        elif user_dec == "go back":
            print("You are back in the hallway.")
            

    elif user_dec == "right":
        user_dec = str(input("There is a dragon standing right in front of you! Do you want to fight it? Enter 'yes' or 'no':")).lower().strip()
        if user_dec == "yes" and sword == False:
            print("You don't have a magic sword, you lost!")
        if user_dec == "no":
            print("You are back in the hallway.")
            
    else:
        pass
# user_dec = str(input("Do you want to play again? Enter 'yes' or 'no': ")).lower().strip()
#             if user_dec == "yes":
#                 play = True
#             if user_dec == "no":
#                 play = False







