"""
Given an array of distinct integers, transform the array into a zig zag sequence by permuting the array
elements. A sequence will be called a zig zag sequence if the first elements in the sequence are in
increasing order and the last elements are in decreasing order. You need to find the
lexicographically smallest zig zag sequence of the given array.
"""


def ZigZag(a):
    a.sort()
    x = a[:len(a)//2+1]
    x.extend(a[len(a)-1:len(a)//2:-1])
    return x


a = list(map(int, input("Enter the list elements: ").strip().split()))
print(ZigZag(a))

