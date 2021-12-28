#!/bin/python3

# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):

    # 2**32 -1 represents the highest possible 32 bit number representation
    # The -1 is because integers start at 0, but our counting starts at 1.

    return (2**32 - 1) - n


if __name__ == '__main__':

    q = int(input("Enter total number of inputs: ").strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        print(result)
