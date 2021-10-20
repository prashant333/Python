#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    for i in range(len(arr)):
        x = arr.index(i+1)
        arr[i], arr[x] = arr[x], arr[i]
    return arr


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(str(res) + '\n')

