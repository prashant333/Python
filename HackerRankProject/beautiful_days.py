#!/bin/python3

import os
#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def beautifulDays(i, j, k):

    count = 0
    # set the range between i and j

    for x in range(i, j + 1):

        # reversing the numbers by converting them to string and using slice.

        y = int(str(x)[::-1])

        # checking if the difference is divisible by K and then increasing the counter.
        
        if (abs(x - y) % k) == 0:
            count += 1
    return count


if __name__ == '__main__':
    # Taking all three input at once and storing them using split().

    first_multiple_input = input("Please enter the values:").rstrip().split()

    # Assign each value to the respectable variable.

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)
    # Change the integer value of result to string.

    print(" Total number of beautiful days :" + str(result))

