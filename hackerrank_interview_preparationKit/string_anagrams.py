#!/bin/python3

from collections import Counter
# Complete the 'makeAnagram' function below.
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b


def makeAnagram(a, b):
    # Write your code here
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_b.subtract(ct_a)
    return sum(abs(i) for i in ct_b.values())


if __name__ == '__main__':

    a = input("Enter first string: ")

    b = input("Enter second string: ")

    res = makeAnagram(a, b)

    print("Number of character deletion required to make anagram is:", res)
