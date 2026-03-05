# Diamond Hernandez
# 03-04-2026
# P3LAB
# Enter money as a float

# Currency to coins

# Get amount
amount = float(input("Enter the amount of money as a float: $"))

# Convert to coins
cents = int(amount * 100)

dollars = cents // 100
cents = cents - dollars * 100

quarters = cents // 25
cents = cents - quarters * 25

dimes = cents // 10
cents = cents - dimes * 10

nickels = cents // 5
cents = cents - nickels * 5

pennies = cents

# Print results

if dollars == 0 and quarters == 0 and dimes == 0 and nickels == 0 and pennies == 0:
    print("No change")
if dollars == 1:
    print("1 Dollar")
elif dollars > 1:
    print(f"{dollars} Dollars")
if quarters == 1:
    print("1 Quarter")
elif quarters > 1:
    print(f"{quarters} Quarters")
if dimes == 1:
    print("1 Dime")
elif dimes > 1:
    print(f"{dimes} Dimes")
if nickels == 1:
    print("1 Nickel")
elif nickels > 1:
    print(f"{nickels} Nickels")
if pennies == 1:
    print("1 Penny")
elif pennies > 1:
    print(f"{pennies} Pennies")