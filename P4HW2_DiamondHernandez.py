# Diamond Hernandez
# 03-28-2026
# P4HW2
# Employee pay calculations

print("\033[95m", end="")

def main():
    total_employees = 0
    total_overtime_pay = 0.0
    total_regular_pay = 0.0
    total_gross_pay = 0.0

    while True:
        name = input('🍓 Enter employee\'s name or "Done" to terminate: ')
        if name == "Done":
            break
        hours = float(input(f'🍓 How many hours did {name} work? '))
        rate = float(input(f'🍓 What is {name}\'s pay rate? '))

        # Calculate overtime
        if hours > 40:
            overtime_hours = hours - 40
            regular_hours = 40
        else:
            overtime_hours = 0
            regular_hours = hours

        # Calculate all pay
        regular_pay = regular_hours * rate
        overtime_pay = overtime_hours * rate * 1.5
        gross_pay = regular_pay + overtime_pay

        # Get totals
        total_employees += 1
        total_overtime_pay += overtime_pay
        total_regular_pay += regular_pay
        total_gross_pay += gross_pay

        # Display results
        print(f"\n🍓 Employee name:   {name}\n")
        print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
        print("---------------------------------------------------------------------------")
        print(f"{hours:.1f}           ${rate:.2f}      {overtime_hours:.1f}       "
              f"${overtime_pay:.2f}        ${regular_pay:.2f}      ${gross_pay:.2f}\n")

    # Complete
    print(f"\n🍓 Total number of employees entered: {total_employees}")
    print(f"🍓 Total amount paid for overtime: ${total_overtime_pay:.2f}")
    print(f"🍓 Total amount paid for regular hours: ${total_regular_pay:.2f}")
    print(f"🍓 Total amount paid in gross: ${total_gross_pay:.2f}")

main()