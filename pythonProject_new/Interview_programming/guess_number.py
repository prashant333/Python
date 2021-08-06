"""
Number guessing.

Write a Python program to guess a number between 1 to 9.
"""
import random

guess, user_int = random.randint(1, 9), 0
while guess != user_int:
    user_int = int(input("Enter a number between 1 and 9, unless prompted: "))
print("well guess")

