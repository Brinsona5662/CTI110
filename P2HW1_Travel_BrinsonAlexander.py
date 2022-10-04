# The program takes information entered by the user and calculates and displays their travel expenses.
# 9/29/2022
# CTI-110 P2HW1 - Travel Expense
# Alexander Brinson

# Display "This program calculates your travel expenses"
# Ask for user's budget
# User inputs budget
# Ask user's destination
# User inputs destination
# Ask for cost of gas
# User inputs cost of gas
# Ask for cost of accomodations
# User inputs cost of accomodations
# Ask for cost of food
# User inputs cost of food
# Add expenses with a 6% tax
# Subtract expenses from the user's budget
# Display user's initial budget, destination, cost of various things, expenses, and remaining budget

print('This program calculates your travel expenses')
print('--------------------------------------------')
print() # these empty prints work to move the next print down another line

print ('Enter your budget:', end=' ')
budget = float(input())
print()

print ('Enter your travel destination:', end=' ')
destination = input()
print()

print ('How much do you think you will be spending on gas?:', end=' ')
gas = float(input())
print()

print ('How much will you spending on accomodations?:', end=' ')
accomodation = float(input())
print()

print ('Finally, how much do you think you will be spending on food?:', end=' ')
food = float(input())
print()

expenses = gas + accomodation + food

new_budget = budget - expenses
print('---------Travel Expenses---------')
print('Location:              ' + destination)
print('Initial Budget:        $', budget)
print('Cost of Gas:           $', gas)
print('Cost of Accomodations: $', accomodation)
print('Cost of Food:          $', food)
print('---------------------------------')
print()
print('Remaining Budget:      $', new_budget)
