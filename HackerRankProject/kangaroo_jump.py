#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    # Write your code here

    """ We are using y=mx +c line equation to check if the two given will
    ever intersect each other. With the exception being that if x2 > x1 and v2 > v1, then
     the two kangaroo will never meet.
     After solving the equation we get the value as (x1-x2)/(v2-v1) = y.

     If the value of y is an integer then the line will intersect each other."""
    
    if x2 > x1 and v2 > v1:
        return 'NO'
    x = x1-x2
    v = v2-v1
    y = x % v
    if y == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
