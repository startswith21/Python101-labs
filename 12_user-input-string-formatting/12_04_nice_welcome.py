# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.
username = input("Enter your name: ")
firstname = username.split()[0]
flag = False
for char in username:
    if char == " ":
        flag = True
if flag == True:
    print(f"Hello there {firstname}!")
else:
    print(f"Hello there {username}!")
