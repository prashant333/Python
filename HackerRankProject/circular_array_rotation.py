#!/bin/python3

# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    if k > len(a):
        # we are taking mod of K in order to avoid repetition of shift.
        k = k % len(a)
    k = len(a) - k
    # Using slice operation to shift values of array.
    a = a[k:] + a[:k]
    # using comprehension to return value for each queries on shifted array.
    return [a[i] for i in queries]


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(result)

