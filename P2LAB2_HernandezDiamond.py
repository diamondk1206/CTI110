# Diamond Hernandez
# 02-23-2026
# P2LAB2
# Vehicle MPGs

vehicles = {
"Camaro": 18.21,
"Prius": 52.36,
"Model S": 110,
"Silverado": 26

}

# Get keys
keys = vehicles.keys()

# Print keys
print(keys)
print()

# Choose vehicle
choice = input("Enter a vehicle to see its MPG: ")
print()

# Show MPG
mpg = vehicles[choice]
print(f"The {choice} gets {mpg} mpg.")
print()

# Get miles
miles = float(input("How many miles will you be driving? "))
print()

# Calculate gallons
gallons =  miles / mpg

# Display gallons
print(f"You will need {gallons:.2f} gallons of gas for the {choice}.")
print()

