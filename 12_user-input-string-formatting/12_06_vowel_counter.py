# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.
# count all a e i o u and print total number of each vowel 
user_answer = str(input("Enter your word here: "))
count_a = 0
count_e = 0
count_i = 0
count_o = 0
count_u = 0
for letter in user_answer:
    if letter == "a":
        count_a += 1
    if letter == "e":
        count_e += 1
    if letter == "i":
        count_i += 1
    if letter == "o":
        count_o += 1
    if letter == "u":
        count_u += 1
print(f"The total number of 'a' is: {count_a}.")
print(f"The total number of 'e' is: {count_e}.")
print(f"The total number of 'i' is: {count_i}.")
print(f"The total number of 'o' is: {count_o}.")
print(f"The total number of 'u' is: {count_u}.")
