#!/bin/python3
# Complete the 'plusMinus' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def plusMinus(arr):
    # Write your code here
    n = len(arr)
    pos, neg, zer = 0, 0, 0

    for i in range(n):
        if arr[i] < 0:
            neg += 1
        elif arr[i] > 0:
            pos += 1
        else:
            zer += 1
    print(f"{pos / n:6f}\n{neg / n:6f}\n{zer / n:6f}")


if __name__ == '__main__':
    n = int(input("Input total number of elements: ").strip())

    arr = list(map(int, input("Inputs: ").rstrip().split()))

    plusMinus(arr)
