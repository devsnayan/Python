
# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# Python String
# We use single quotes or double quotes to represent a string in Python. For example,

first_name = "Mohammad"
middle_name = " Yeasin Arfat "
last_name = "Nayan"
full_name = first_name+middle_name+last_name

# Output
print(full_name)

# print index number
print(full_name[2])

# print range by index
print(full_name[9:15])

# Check Len
print(len(full_name))

# Check type
print(type(full_name))

# Compare
print(first_name == last_name)

# Looping
for letter in full_name:
    print(letter)


# String Membership Test
print(first_name in full_name)
print("Risha" in full_name)

# Escape Sequences 
example_one = "He said, \"What's there?\"" #double quote
example_two = 'He said, "What\'s there?"' #single quote
print(example_one)


# Python String Formatting (f-Strings)
print(f'My first name is {first_name} and last name is {last_name}.')
