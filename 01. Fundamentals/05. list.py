# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# python List
# List is a collection which is ordered and changeable. Allows duplicate members.
# In Python, lists are used to store multiple data at once.
# Suppose we need to record the ages of 5 students. Instead of creating 5 separate variables, we can simply create a list.

var_1 = [112,113,114,115,116,117,118]
var_2 = [116,117,118,119,120,121,122]
mixed = ["Apple",121,True,"Orange"]
ages = [24,15,17,20]

# Empty set
empty_list1 = list()
empty_list2 = []

# Direct print
print(mixed)

# Check Type
print(type(mixed))

# Check total Item
print(len(mixed))

# --------------------
# indexing AND Slicing
print(var_1)
print(var_1[3])
print(var_1[3:5])
print(var_1[3:])
print(var_1[:4])
print(var_1[-3]) 

# -------------------------
# python tuple concatination
merge = var_1 + var_2
print(merge)
# print(merge.count("a"))
# print(merge.index("b"))

# ------------------------
# Add Elements to a List
# Using append() //add an item
print("Print before append: ", mixed)
mixed.append("Nayan")
print("Print after append: ", mixed)

# Using extend() //add all items
mixed.extend(var_1)
print("print after add var_1: ", mixed)

# Using insert() // use the insert() method to add an element at the specified index.
mixed.insert(0,"Risha")
print(mixed)

# ------------------
# Change List Items 
# changing the second item to 'Yeasin'
mixed[1] = "Yeasin"
print(mixed)

# --------------------
# Remove an Item
del mixed[1]
print(mixed)
del mixed[2:5] # del from specfic range
print(mixed)

# Using remove()
mixed.remove('Risha')
print(mixed)

# ------------------
# Iterating through a List
for x in mixed:
    print(x)


# ----------------
# Check if an Element Exists in a List
print(118 in mixed)
print("Risha" in mixed)

# -----------------
# List Comprehension
# one
numbers = [n**2 for n in range(1, 6)]

print(numbers)    

# Two 
numbers = []
for n in range(1, 25):
    numbers.append(n**3)
    print(numbers)






