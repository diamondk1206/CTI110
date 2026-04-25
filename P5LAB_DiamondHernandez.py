# Diamond Hernandez
# 04-25-2026
# P5LAB
# Self checkout calculations



import random

def disperse_change(change):
    cents = round(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    if dollars:
        print(f"{dollars} Dollars")
    if quarters:
        print(f"{quarters} Quarters")
    if dimes:
        print(f"{dimes} Dimes")
    if nickels:
        print(f"{nickels} Nickels")
    if pennies:
        print(f"{pennies} Pennies")


def main():
    owed = round(random.uniform(0.01, 100.00), 2)
    print(f"💰 You owe ${owed:.2f}!")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash - owed, 2)
    print(f"💰 Your change is: ${change:.2f}\n")

    disperse_change(change)


main()