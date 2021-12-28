#!/bin/python3

# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):

    return (2**32 - 1) - n


if __name__ == '__main__':

    q = int(input("Enter total number of inputs: ").strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(result)
