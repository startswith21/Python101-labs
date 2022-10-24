#Replicate one of the oldest known encryption in code.
#Apply a Cesar cipher of 7 to the 'secret' variable.
#You can start with the following code:
#move each letter by 7 steps in alphabet

sentence = "I hear the gooseberries are doing well this year, and so are the mangoes."
cipher = 7
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefgh"
char_index = " "
encrypted = " "

for char in sentence:                                 #this is not working
    if char in alphabet:
        char_index = (alphabet.index(char) + cipher)
        encrypted += sentence[char_index]            

print(encrypted)
