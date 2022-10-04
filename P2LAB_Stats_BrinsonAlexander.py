# This program takes four numbers and display their product and average both rounded and 3 digits after the decimal point
# 9/28/2022
# CTI-110 - Simple Statistics
# Alexander Brinson

# Get all four numbers
# Calculate their product and average
# Display the results both rounded and 3 digits after the decimal point

num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4) / 4
int_product = num1 * num2 * num3 * num4
int_average = (num1 + num2 + num3 + num4) / 4

print(f'{product:.0f} {average:.0f}')
print(f'{product:.3f} {average:.3f}')