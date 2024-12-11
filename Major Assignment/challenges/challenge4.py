# Tuples
# Write a Python function that:
#  Takes a tuple of integers as input.
#  Returns a new tuple with only the even numbers from the original
# tuple.
# Converts the tuple into a list and adds a new element to it.

def tupleEvenNumbers(num):
    for i in num:
        if(i % 2 == 0):
            print(i, end = "  ") 


num = (10,30,25, 34,26,30,45) 
print("The tuple numbers are:", num)
print("The tuple with only even numbers are:")
tupleEvenNumbers(num)


  








#      def division(num1=1,num2=1):
#     return num1/num2
# try:
#     result4= division(num1,num2)
#     print(f'The division of two number is:{result4}')

# except ZeroDivisionError:
#     print("Invalid input")

#      even_number= (num/2==0)
#      for _ in num:
#           if num/2==0:
#                print(num=even_number)
    
        

# tuple_list(num)
