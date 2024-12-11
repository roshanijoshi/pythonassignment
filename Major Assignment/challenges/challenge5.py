#  Dictionaries (Basics)
# Write a Python program that:
# ● Creates a dictionary with keys as numbers from 1 to 5 and values as
# their squares.
# ● Prints all the keys and values.
# ● Updates the value of key 3 to 27.
# ● Deletes the key 5 from the dictionary.

num_squares ={
    "1":1**2,
    "2":2**2,
    "3":3**2,
    "4":4**2,
    "5":5**2,

}
print(f'The squares of numbers are:{num_squares}')
num_squares["3"]=27
print(f'The changed value of key 3 is:{num_squares}')
del num_squares["5"]
print(f'The remaining number squares are:{num_squares}')



