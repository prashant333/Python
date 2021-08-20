"""
recursive algorithm

Write a recursive algorithm to compute the integer part of the base-two
logarithm of nm using only addition and integer division.
"""
import math


def log_2_int(n):
    if n < 2:
        return 0
    else:
        return 1+log_2_int(n//2)


for n in [100, 5, 7, 1.9, 0.1, 6]:
    print(n, log_2_int(n), math.log(n, 2))
