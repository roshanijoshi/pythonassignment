#1. Write a Python program to take two numbers as input from the user and 
# print their sum, difference, product, and division. Ensure the program
# handles division by zero gracefully.

num1=int(input("Enter your first number"))
num2=int(input("Enter your second number"))
try:
    print(f'Sum of the numbers:{num1+num2}')
    print(f'Difference of the numbers:{num1-num2}')
    print(f'Product of  the numbers:{num1*num2}')
    print(f' Division of the numbers:{num1/num2}')

except ZeroDivisionError:
    print("Division by zero is not allowed")
