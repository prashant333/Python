# This program used recursion to sum all the elements of a given list.

def recursive_sum(S, n):
    if n == 0:
        return 0
    else:
        return recursive_sum(S, n-1) + S[n-1]


S = list(map(int, input("Enter list elements: ").split()))
n = len(S)
print(recursive_sum(S, n))

