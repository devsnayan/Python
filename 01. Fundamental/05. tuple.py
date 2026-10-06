# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# python Tuples
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

var_1 = "a","b","c","d","e","f","g" #without parentheses
var_2 = ("a","b","c","d","e","f","g") #with perentheses
var_3 = 1,2,3,4,5,6
var_4 = 4,5,6,7,8,9,0

# Direct Print
print(var_1)

# check type
print(type(var_1))

# check total item
print(len(var_1))

# indexing AND Slicing
print(var_1[3])
print(var_1[3:5])
print(var_1[3:])
print(var_1[:4])
print(var_1[-3]) 

# Looping
for x in var_1:
    print(x) 

# python tuple methods
merge = var_1 + var_2
print(merge)
print(merge.count("a"))
print(merge.index("b")) 

# check item if exist
print("a" in var_1)
print("z" in var_1)

input = input("Input data: ")
print(input in var_1)

# exercise
