#  Strings
# Write a Python program that:
# ● Takes a string as input.
# ● Reverses the string.
# ● Counts the number of vowels (a, e, i, o, u) in the string.
# ● Converts the string to uppercase.
 
name= "Roshani"
print(f'Your name is {name}')
rev=''.join(reversed(name))
print(f'The reverse of your name is:{rev}')

vowel_count = 0
for i in name:
    if i in "aeiouAEIOU":
        vowel_count += 1

print(vowel_count)


name=name.upper()
print(name)