''' Instructions of practice exercise 7.5
Write a Python program that defines a function to check whether a given number is prime.'''


# Declares a function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Inputs a number from the user
num = int(input("Enter a number: "))

# Checks if the entered number is prime using the function and displays the output5
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

