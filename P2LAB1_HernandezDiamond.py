# Diamond Hernandez
# 02-18-2026
# P2LAB1
# Circle Formulas

import math

# Ask for radius
radius = float(input("What is the radius of the circle? "))

# Circle calculations
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Print results

print(f"\nThe diameter of the circle is {diameter:.1f}")
print(f"\nThe circumference of the circle is {circumference:.2f}")
print(f"\nThe area of the circle is {area:.3f}")
