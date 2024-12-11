# Write a Python function that takes two numbers (integers or floats) as input
# and returns:
# Their sum
# Their difference
# Their product
# ● Their division (handle the case where division by zero might occur).

def greet_user(num1,num2):
    print(num1+num2)
    print(num1-num2)
    print(num1*num2)
    try:
     print(f'The division of two numbers:{num1/num2}')

    except ZeroDivisionError:
      print("Invalid Input")

num1=float(input("Enter the first number:"))
num2=float(input("Enter your second number:"))

greet_user(num1,num2)