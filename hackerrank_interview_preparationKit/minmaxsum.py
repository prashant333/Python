#!/bin/python3
# Complete the 'miniMaxSum' function below.
# The function accepts INTEGER_ARRAY arr as parameter.

def miniMaxSum(arr):
    # Write your code here
    n = len(arr)
    new_arr = sorted(arr)
    min_x = sum(new_arr[:n - 1])
    max_y = sum(new_arr[1:])
    print(str(min_x) + " " + str(max_y))

    # below is one line solution for this problem, it used built in function min and max.
    # print(sum(arr)-max(arr), sum(arr)-min(arr))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
