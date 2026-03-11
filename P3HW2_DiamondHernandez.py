# Diamond Hernandez
# 03-11-2026
# P3HW2
# Employee pay information


# Get data
name = input('Enter employee name: ')
hours = float(input('Enter number of hours worked this week: '))
pay_rate = float(input('Enter employee hourly pay rate: '))

# Calculate overtime
if hours > 40:
    overtime_hours = hours - 40
else:
    overtime_hours = 0
overtime_pay = overtime_hours * pay_rate * 1.5

# Calculate regular
regular_hrs = hours - overtime_hours
regular_pay = regular_hrs  * pay_rate

# Get gross pay
gross_pay = regular_pay + overtime_pay

# Show results
print("------------------------------------------")
print('Employee name:', name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<10}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay'}")
print('----------------------------------------------------------------------------------')
print(f"{hours:<15.1f}{pay_rate:<12.1f}{overtime_hours:<10.1f}${overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:.2f}")