#!/bin/python3

# Complete the rotLeft function below.
'''
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
'''

# alternate solution 1

'''
def rotLeft(a, d):
    # Write your code here
    for i in range(d):
        temp = a[0]
        for j in range(n-1):
            a[j] = a[j+1]
        a[len(a) - 1] = temp
    return a
'''

# alternate solution 2


def rotLeft(a, d):
    a = list(a)
    return a[d:] + a[:d]


if __name__ == '__main__':
    nd = input("Enter two values:").split()
# size of array
    n = int(nd[0])
# no of left rotation
    d = int(nd[1])
# array
    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    print(*result)

