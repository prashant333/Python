#!/bin/python3

# Complete the hourglassSum function below.
def hourglass_sum(arr, i, j):
    a = arr[i][j]
    b = arr[i][j + 1]
    c = arr[i][j + 2]
    d = arr[i + 1][j + 1]
    e = arr[i + 2][j]
    f = arr[i + 2][j + 1]
    g = arr[i + 2][j + 2]

    return a + b + c + d + e + f + g


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(len(arr))
    result = []

    for i in range(len(arr) - 2):
        for j in range(len(arr) - 2):
            sum1 = hourglass_sum(arr, i, j)
            result.append(sum1)
    print(result)
    print(max(result))
'''
sample input could be something like

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

'''
