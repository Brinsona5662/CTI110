# CTI-110
# P3HW2 - Salary
# Alexander Brinson
# 11/1/2022
# This progrm calculates an employee's pay

# Pseudocode
# Display "Enter employee's name"
# Assign the input to variable "name"
# Display "Enter number of hours worked"
# Assign the input to variable "hours_worked"
# Display "Enter employee's pay rate"
# Assign the input to variable "pay_rate"
# Determine if employee has worked overtime
# If the employee has worked over time, calculate overtime pay
# Calculate employee's pay for normal hours
# Display employee's name, pay rate, number of hours worked, overtime hours, overtime pay, pay for normal hours, and gross pay

name = str(input("Enter employee's name: "))
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

overtime = 0.0
overtime_pay = 0.0
reg_hours_pay = 0.0

if hours_worked > 40:
    overtime = hours_worked - 40
    overtime_pay = overtime * 26.25
    reg_hours_pay = pay_rate * 40
else:
    reg_hours_pay = pay_rate * hours_worked

gross_pay = reg_hours_pay + overtime_pay

print('-----------------------------------')
print('Employee name:   ' + name)
print('')
print("Hours Worked   Pay Rate   OverTime   OverTime Pay    RegHour Pay    Gross Pay")
print('--------------------------------------------------------------------------------')
print(hours_worked, "         ", pay_rate, "      ", overtime, "      ", overtime_pay, "       ", reg_hours_pay, "         ", gross_pay)
