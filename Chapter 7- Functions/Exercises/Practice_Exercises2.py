''' Instructions for practice exercise 7.2
Write a Python function that calculates the factorial of a 
given positive integer using recursion'''

# Declares a function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Usage of the function
num = 4
result = factorial(num)
print(f"The factorial of {num} is {result}.")
