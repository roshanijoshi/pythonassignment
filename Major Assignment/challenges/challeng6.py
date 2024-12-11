#  String and Dictionary Combination
# Write a Python function that:
# ● Takes a string as input.
# ● Counts the frequency of each character in the string and stores it in a
# dictionary.
# ● Ignores spaces and considers case-insensitive comparisons


def greet_user(name):
    name.replace("","")
    frequency={}
    for each_char in name.lower():
        if each_char in frequency:
            frequency[each_char]=+1
        else:
            frequency[each_char]=1

        return frequency
name= input("Enter your name")
print(greet_user(name))

