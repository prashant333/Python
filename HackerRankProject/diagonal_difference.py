#!/bin/python3

# The function accepts 2D_INTEGER_ARRAY arr as parameter.

def diagonalDifference(arr):

    temp = 0
    emp = 0
    for i in range(0, len(arr)):
        temp = temp + arr[i][i]
        emp = emp + arr[i][len(arr) - 1 - i]

    print(abs(temp - emp))


if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(arr)

#sample input could be something like

#4
#1 2 3 4
#5 6 7 8
#9 0 1 2
#3 4 5 6