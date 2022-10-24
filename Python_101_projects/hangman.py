# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.
# Hard-code a word that needs to be guessed in the script
# Print an explanation to the user
# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
# Ask for user input
# Allow only single-character alphabetic input
# Create a counter for how many tries a user has
# Keep asking them for their guess until they won or lost
# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
# Display a winning message and the full word if they win
# Display a losing message and quit the game if they don't make it

target_word = "GLANCE"
empty_word = "_" * len(target_word)
total_numguesses = 6
rem_numguesses = 6
allguessed_letters = []
guessed_letter = []
index = []
name = input("Enter your name: ")

print(f"Hello {name}, you are going to play hangman and you have 6 guesses! Good luck!\n"
      f"This is the empty word: {empty_word}")

while guessed_letter != target_word and rem_numguesses > 0:
    user_input = input("Enter letter: ").upper()
    rem_numguesses -= 1
    
    for char in user_input:
        if char in target_word:           
            allguessed_letters.append(user_input)
            index = [i for i, l in enumerate(target_word) if l == char]
            for i in index:
                empty_word = empty_word[:i] + char + empty_word[i+1:]
            print(f"The letter {user_input} is present in the word: {empty_word} ")                     
        else:
            print("Wrong letter! '_'")
    print(f"Number of guesses that you have left: {rem_numguesses}") 

if empty_word == target_word:
    print(f"You won! The word is: {target_word}.")
if empty_word != target_word:
    print(f"You lost. The word is: {target_word}.")
