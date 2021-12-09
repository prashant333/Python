"""
Print FizzBuzz.

This program print fizz is the number is divisible by 3, and buzz if the number is divisible by 5.
However if the number is divisible by both 3 and 5 then print FizzBuzz.
"""

n = list(range(1, int(input("Input the number range: "))))
print(n)
for i in range(len(n)+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
    else:
        print(i, -1)
