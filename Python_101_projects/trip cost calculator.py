#Create a python script that asks a user questions in the command line. 
# The script should follow the outlined specs.
## Specs
#Receive the following arguments from the user:
#- kilometers to drive
#- liters-per-kilometer usage of the car 
#- price per liter of fuel
#Calculate the cost of the trip and display it to the user in the console.

user_km = int(input("Enter distance in km: "))
user_usage = int(input("Enter usage in liters: "))
user_fuelprize = int(input("Enter fuel prize per liter in Euro: "))

print(f"The trip will cost {user_km * user_usage * user_fuelprize} Euros")
