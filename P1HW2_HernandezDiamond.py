# Diamond Hernandez
# 02-12-2026
# P1HW2
# Calculate and display travel expenses

print("This program calculates and displays travel expenses")
print()

# Get expenses in numbers from user
budget= int(input ("Enter budget: "))
print()
travel= (input ("Enter your travel destination: "))
print()
gas= int(input ("How much do you think you will spend on gas? "))
print()
hotel= int(input ("Approximately, how much will you need for accomodation/hotel? "))
print()
food= int(input ("Last, how much do you need for food? "))
print()

# Calculate values for total summary

balance= budget-gas-hotel-food
# Print summary of expenses
print("------Travel Expenses------")
print("Location: ", travel)
print("Initial budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", hotel)
print("Food: ", food)
print()
print("Remaining Balance: ", balance)