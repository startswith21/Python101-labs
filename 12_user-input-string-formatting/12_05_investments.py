# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.
invest_amount = int(input("Enter investment amount: "))
interest_rate = float(input("Enter interest rate in %: "))
years_invest = int(input("Enter years investment: "))

result = invest_amount * (interest_rate * 100) * years_invest
print(result)
