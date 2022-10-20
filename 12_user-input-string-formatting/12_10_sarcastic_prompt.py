# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
# unkown words, string char count
user_opinion = input("Enter your opinion: ")
mock_opinion = ""
count = 0
for char in user_opinion:
    count += 1
    if count % 2 == 0:   
        mock_opinion += char.upper()
        
    else:
        mock_opinion += char.lower()
print(mock_opinion)

complain = input("Complain here: ")
sarcasm_complain=""
count = 1
for char in complain:
    if count % 2 == 0: 
        sarcasm_complain += char.upper()
        count+=1
    else:
       sarcasm_complain += char
       count +=1
print (sarcasm_complain)