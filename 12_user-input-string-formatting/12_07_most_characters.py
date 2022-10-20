# Write a script that takes three strings from the user
# and prints the longest string together with its length.
# Example Input:hello world greetings
# Example Output: 9, greetings
# count character of each string, compare character counts between strings, can be of the same length!,
# determine the longest one 
user_input1 = input("Enter your first word: ")
user_input2 = input("Enter your second word: ")
user_input3 = input("Enter your third word: ")
numchar_input1 = len(user_input1)
numchar_input2 = len(user_input2)
numchar_input3 = len(user_input3)

if numchar_input1 > numchar_input2 and numchar_input1 > numchar_input3:
    print(f"{user_input1}, {numchar_input1}")
if numchar_input2 > numchar_input1 and numchar_input2 > numchar_input3:
    print(f"{user_input2}, {numchar_input2}")
if numchar_input3 > numchar_input1 and numchar_input3 > numchar_input2:
    print(f"{user_input3}, {numchar_input3}")

if numchar_input3 == numchar_input1 or numchar_input3 == numchar_input2 or numchar_input1 == numchar_input2:
    print("at least two strings are of equal length")


