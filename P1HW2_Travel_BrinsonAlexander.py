# The program takes information entered by the user and calculates and displays their travel expenses.
# 9/20/2022
# CTI-110 P1HW2 - Travel Expense
# Alexander Brinson

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

print ('Enter your budget:', end=' ')
budget = int(input())
print() # these empty prints work to move the next print down another line

print ('Enter your travel destination:', end=' ')
destination = input()
print()

print ('Enter the cost of gas:', end=' ')
gas = int(input())
print()

print ('Enter the cost of accomodations:', end=' ')
accomodation = int(input())
print()

print ('Enter the cost of food:', end=' ')
food = int(input())
print()

expenses = gas + accomodation + food

new_budget = budget - expenses
print('-------Travel Expenses-------')
print()

print('Location: ', destination)
print('Initial Budget: ', budget)
print()

print('Cost of Gas: ', gas)
print('Cost of Accomodations: ', accomodation)
print('Cost of Food: ', food)
print()

print('Remaining Budget: ', new_budget)


