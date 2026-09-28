# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# python Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# Dictionaries are written with curly brackets, and have keys and values:

person_one = {
    "name"  : "Mohammad Nayan",
    "age"   : 26,
    "height" : "5f 8in",
    "weight" : "79 KG"
}

country_capitals = {
  "United States": "Washington D.C.", 
  "Italy": "Rome", 
  "England": "London",
  "Bangladesh" : "Dhaka"
}

# Direct Print
print(person_one)

# check type
print(type(person_one))

# check total item
print(len(person_one))

# Access Dictionary Items
print("Access Dictionary Name Item: ", person_one["name"].upper())

# Change Dictionary Items
person_one["name"] = "Mohammad Yeasin Arfat Nayan"
print(person_one)

# Add Items to a Dictionary
person_one["hair"] = "Long and Curly"
print(person_one)

# Remove Dictionary Items
del person_one["hair"] #specfic key delete
print(person_one)

#person_one.clear() #clear all items by clear()
# print(person_one)

# Dictionary Membership Test or test if exist
print("name" in person_one)
print("hair" in person_one)


# --------------------------------------
# Looping
# output key and values
for key, value in person_one.items():
    print(f"{key.capitalize()}: {value}")

# outpur only key
for person in person_one:
    print(person)

# output only values
for person in person_one:
    value = person_one[person]
    print(value)


