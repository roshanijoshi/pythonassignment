# Lists
# Write a Python functiom that:
# Accepts a list of integers as input. (use split method)
# Returns the largest and smallest number in the list.
# Removes duplicates from the list.
# Sorts the list in descending order.

def  min_max_number(numbers):

    min_number=min(numbers)
    max_number=max(numbers)
    sorted_numbers= sorted(set(numbers), reverse=True)
           
    return min_number,max_number,sorted_numbers

numbers= input("Enter the list of numbers separated by commas:").split(',')

result = min_max_number(numbers)
print(result)



























