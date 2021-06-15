#!/bin/python3

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    x, z, y = 0, 0, 0
    for i in range(0, len(arr)):
        if arr[i] > 0:
            x = x + 1
        elif arr[i] < 0:
            y = y + 1
        else:
            z = z + 1
    print(x/len(arr))
    print(y/len(arr))
    print(z/len(arr))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

"""
The first line contains an integer, n, the size of the array.
The second line contains n space-separated integers that describe arr[n] .

example - 

6
-4 3 -9 0 4 1
"""