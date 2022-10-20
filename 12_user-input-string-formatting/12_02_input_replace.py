# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please
#find character at index 0, name character and replace character
string = input("Enter several words: ")

letter = string[0]
string = string.replace(letter, "**")

print(letter)
print(string)











