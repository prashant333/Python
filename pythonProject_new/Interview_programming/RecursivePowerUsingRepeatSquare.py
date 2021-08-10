"""
Repeated squaring method.

This program uses repeated squaring method to find the power of a given number. This method
reduces the time complexity from O(n) to O(log n).
"""


def power(x, n):
    if n == 0:
        return 1
    else:
        partial = power(x, n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result


x = int(input("Enter value of base: "))
n = int(input("Enter value of exponent: "))
print(power(x, n))
