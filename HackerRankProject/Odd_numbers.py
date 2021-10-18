#!/bin/python3

import math
import os

#
# Complete the 'oddNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER l
#  2. INTEGER r
#


def oddNumbers(l, r):
    # Write your code here
    out = []
    i = l
    while i < r + 1:
        if i % 2 != 0:
            out.append(i)
        i += 1
    return out


if __name__ == '__main__':

    l = int(input().strip())

    r = int(input().strip())

    result = oddNumbers(l, r)

    print('\n'.join(map(str, result)))
    print('\n')
