# Diamond Hernandez
# 03-28-2026
# P4LAB2
# Multiplication table


# Start
print("\033[95m", end="")

run_again = "yes"

while run_again.lower() == "yes":
    # Ask user for an integer
    number = int(input("Enter an integer: "))

    if number < 0:
        print("This program does not handle negative numbers.")  # error message in pink
    else:
        print(f"\n🌸 Multiplication table for {number}: ")
        # For loop prints 1 to 12
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")

    # Ask if user wants to run again
    run_again = input("\nWould you like to run the program again? ")

print("\nExiting program!🌸")