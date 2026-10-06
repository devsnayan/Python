# Sharmila Alam Risha

# python Set
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
# There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

var_1 = {112,113,114,115,116,117,118}
var_2 = {116,117,118,119,120,121,122}
var_3 = {3,4,2,4,7,9,8,5,3,1,0}


# Empty set
empty_set = set()

# Direct print
print(var_3)

# Check Type
print(type(var_3))
# Check total Item
print(len(var_3))

# using add() method
var_3.add(32)
print(var_3)

# Looping
for x in var_3:
    print(x)

# Update Python Set
var_1.update(var_2)
print(var_1)


# Remove an Element from a Set
print("Before remove item: ", var_1)
var_1.discard(113)
print("After remove item: ", var_1)

# Set Build-in function
print("Max value: ", max(var_3))
print("Min Value: ", min(var_3))
print("Sum is: ", sum(var_3))
print("Sorted: ", sorted(var_3))


# Python Set Operations
# Union of Two Sets
print('Union using |:', var_1 | var_2)
print('Union using union():', var_1.union(var_2)) 

# Set Intersection
print('Intersection using &:', var_1 & var_2)
print('Intersection using intersection():', var_1.intersection(var_2)) 

# Difference between Two Sets
print('Difference using &:', var_1 - var_2)
print('Difference using difference():', var_1.difference(var_2))

# Set Symmetric Difference
print('Symmetric using ^:', var_1 ^ var_2)
print('Symmetric using symmetric_difference():', var_1.symmetric_difference(var_2)) 

# Check if two sets are equal
# perform difference operation using &
if var_1 == var_2:
    print('Set var_1 and Set var_2 are equal')
else:
    print('Set var_1 and Set var_2 are not equal')

