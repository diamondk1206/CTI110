# Diamond Hernandez
# 02-26-2026
# P2HW1
# Visual format changes

print("This program calculates and displays travel expenses\n")

# Get expenses in numbers from user
budget= float(input ("Enter budget: "))

travel= (input ("\nEnter your travel destination: "))

gas= float(input ("\nHow much do you think you will spend on gas? "))

hotel= float(input ("\nApproximately, how much will you need for accomodation/hotel? "))

food= float(input ("\nLast, how much do you need for food? "))

# Calculate values for total summary

balance= budget-gas-hotel-food


# Print summary of expenses
print("\n-----------Travel Expenses----------")
print(f"{'Location:':18} {travel}")
print(f"{'Initial Budget:':18} ${budget:,.2f}")
print(f"{'Fuel:' :18} ${gas:,.2f}")
print(f"{'Accomodation:' :18} ${hotel:,.2f}")
print(f"{'Food:' :18} ${food:,.2f}")
print("--------------------------------------")
print(f"\n{'Remaining Balance:':18} ${balance:,.2f}")


