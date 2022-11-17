# CTI-110
# P4HW2 - Salary Calculator
# Alexander Brinson
# 11/17/2022
# This progrm calculates pay for multiple employees

# Pseudocode
# Display "Enter employee's name or None to terminate"
# Assign the input to variable "name"
# Determine if "name" has a value of None. If not, do the following:
# Display "How many hours did "name" work?"
# Assign the input to variable "hours_worked"
# Display "What is "name"'s pay rate?"
# Assign the input to variable "pay_rate"
# Determine if employee has worked overtime
# If the employee has worked over time, calculate overtime pay
# Calculate employee's pay for normal hours
# Display employee's name, pay rate, number of hours worked, overtime hours, overtime pay, pay for normal hours, and gross pay
# If "name" has a value of None, do the following:
# Display the number of employees entered and the total amount payed for overtime, regular hours, and grosspay

numOfEmploy = 0
totalOvertimePay = 0.0
totalRegularPay = 0.0
totalGrossPay = 0.0
name = str(input("Enter employee's name or \"None\" to terminate: "))
while name != "None":
    hours_worked = float(input("How many hours did " + name + " work? "))
    pay_rate = float(input("What is " + name + "'s pay rate? "))

    overtime = 0.0
    overtime_pay = 0.0
    reg_hours_pay = 0.0

    if hours_worked > 40:
        overtime = hours_worked - 40
        overtimePayRate = pay_rate * 1.5
        overtime_pay = overtime * overtimePayRate
        reg_hours_pay = pay_rate * 40
    else:
        reg_hours_pay = pay_rate * hours_worked
    gross_pay = reg_hours_pay + overtime_pay
    
    print()
    print('Employee name:   ' + name)
    print('')
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay    RegHour Pay    Gross Pay")
    print('--------------------------------------------------------------------------------')
    print(hours_worked, "         ", pay_rate, "      ", overtime, "      ", overtime_pay, "           ", reg_hours_pay, "         ", gross_pay)
    numOfEmploy += 1
    totalOvertimePay += overtime_pay
    totalRegularPay += reg_hours_pay
    totalGrossPay += gross_pay
    print()
    name = str(input("Enter employee's name or \"None\" to terminate: "))
print()
print("Total number of empolees entered: " + str(numOfEmploy))
print("Total amount payed for overtime: " + str(f'{totalOvertimePay:.2f}'))
print("Total amount payed for regular hours: " + str(f'{totalRegularPay:.2f}'))
print("Total amount payed in gross: " + str(f'{totalGrossPay:.2f}'))
