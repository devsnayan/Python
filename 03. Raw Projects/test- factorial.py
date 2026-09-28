# Author: Mohammad Nayan
# Software Developer
# https://www.nayan.pro 

# factrial Calculation

def factorial(n):
    if n < 0:
        return "Factorial is undefined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        i = 1
        while i <= n:
            result *= i
            i += 1
        return result

# Example usage
number = int(input("Input a Number: "))
result = factorial(number)
print(f"The factorial of {number} is: {result}")