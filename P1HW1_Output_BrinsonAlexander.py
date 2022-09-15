# this program asks the user for two numbers, then calculates various equations
# 9/15/2022
# CTI 110 WarmUp
# Alexander Brinson

user_num = int(input('Enter integer:\n'))
# this asks the user for a number

print('You entered:', user_num)
num_squared = user_num * user_num
print (user_num, 'squared is', num_squared)
num_cubed = user_num * user_num * user_num
print('And', user_num, 'cubed is', num_cubed, '!!')
# this displays the number, it's square, and it's cube

user_num2 = int(input('Enter another integer:\n'))
num2_sum = user_num + user_num2
num2_prod = user_num * user_num2
print(user_num,'+', user_num2, 'is', num2_sum)
print(user_num,'*', user_num2, 'is', num2_prod)
# this asks for another number and calculates and displays the sum and product of the two numbers