"""
Factorial of a given number.

This program uses recursion to find the factorial of a given number.
"""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


number = int(input("Enter a number: "))
print(factorial(number))

