# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# Function

# ----basic-------
def basic(val):
    print(val)

basic("I'm Python Function.")

# ------- Sum calculatioin one -------
def my_sum(a,b):
    sum = a+b
    print("Sum is: ", sum)

my_sum(5,10)

#------------sum calculation two-----------
def sum_two(a,b):
    sum = a+b
    return sum

result = sum_two(10,15)
print("Sum is: ",result)


# ------- Dynamic Calculation ---------
def dynamic_cal(a,b,opt):
    if opt == "+":
        cal = f'Result of {a} {opt} {b} is: {a+b}'
        return cal
    elif opt == "-":
        cal = f'Result of {a} {opt} {b} is: {a-b}'
        return cal
    elif opt == "*":
        cal = f'Result of {a} {opt} {b} is: {a*b}'
        return cal
    elif opt == "/":
        cal = f'Result of {a} {opt} {b} is: {a/b}'
        return cal
    else:
        return "Invalid Operator!"

a = int(input("Input number a: "))
b = int(input("Input number b: "))
opt = str(input("Input number opt: "))

result = dynamic_cal(a,b,opt)
print(result)


# 
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)


# -----------recursive function-------------
# Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))

