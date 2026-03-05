# Diamond Hernandez
# 02-26-2026
# P2HW2
# List of Grades

print("------My Test Grades of the Semester------\n")

mod1= float(input("\nEnter grade for Module 1:"))
mod2= float(input("\nEnter grade for Module 2:"))
mod3= float(input("\nEnter grade for Module 3:"))
mod4= float(input("\nEnter grade for Module 4:"))
mod5= float(input("\nEnter grade for Module 5:"))
mod6= float(input("\nEnter grade for Module 6:"))

# Make list
modulegrades = [mod1, mod2, mod3, mod4, mod5, mod6]

# Calculate numbers

lowest = min(modulegrades)
highest = max(modulegrades)
total = sum(modulegrades)
average = total / len(modulegrades)

# Display list

print("\n------Results------")
print(f"{'Lowest Grade:'}", min(modulegrades))
print(f"{'Highest Grade:'}", max(modulegrades))
print(f"{'Sum of Grades:'}", sum(modulegrades))
print(f"{'Average:'}", sum(modulegrades) / len(modulegrades))

print("-------------------")
