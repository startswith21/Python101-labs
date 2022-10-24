# Population Growth Calculator
# Write the necessary code to display the total population count for the next 3 years (without a leap year).
# Here are the specifications:
# In the country we want to investigate:
# The current population is 380,123,456
# One person is born every 6 seconds
# One person dies every 12 seconds
# One person immigrates every 40 seconds
threeyearsinsec = 60 * 60 * 24 * 365 * 3
print(threeyearsinsec)
persons_borninthreeyears = threeyearsinsec / 6
persons_deadinthreeyears = threeyearsinsec / 12
persons_immiginthreeyears = threeyearsinsec / 40
total_popcountinthreeyears = 380123456 + persons_borninthreeyears + persons_immiginthreeyears - persons_deadinthreeyears
print(total_popcountinthreeyears)

