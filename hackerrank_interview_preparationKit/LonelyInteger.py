#!/bin/python3

from collections import Counter
#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.


def lonelyinteger(a):
    # Write your code here
    #return Counter(a).most_common()[-1][0]
    result = []
    for item in a:
        result.append(a.count(item))
    answer = result.index(1)
    return a[answer]


if __name__ == '__main__':

    n = int(input("Enter the length of array: ").strip())

    a = list(map(int, input("Enter the values of array: ").rstrip().split()))

    result = lonelyinteger(a)

    print(result)
