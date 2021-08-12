# Implementing binary recursion for adding a given list.

def binary_sum(s, start, stop,):
    if start > stop:
        return 0
    elif start == stop-1:
        return s[start]
    else:
        mid = (start+stop)//2
        return binary_sum(s, start, mid) + binary_sum(s, mid, stop)


s = list(map(int, input("Enter a list value: ").split()))
print(binary_sum(s, 0, len(s)))
