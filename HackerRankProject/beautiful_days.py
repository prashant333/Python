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

    for x in range(i, j + 1):
        y = int(str(x)[::-1])

        if (abs(x - y) % k) == 0:
            count += 1
    return count


if __name__ == '__main__':

    first_multiple_input = input("Please enter the values:").rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    print(" Total number of beautiful days :" + str(result))

