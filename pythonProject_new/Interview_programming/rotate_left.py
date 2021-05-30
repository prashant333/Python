#!/bin/python3

# Complete the rotLeft function below.
def rotLeft(a, d):
    for i in range(d):
        rotatebyone(a)
    return a


def rotatebyone(a):
    temp = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[len(a) - 1] = temp
    return a


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(*result)
