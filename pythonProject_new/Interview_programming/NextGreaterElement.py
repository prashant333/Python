"""
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x
is the first greater element on the right side of x in the array. Elements for which no greater element exist,
consider the next greater element as -1.
"""


def nextGreaterElement(arr):
    for i in range(len(arr)):
        next = None
        for j in range(i+1, len(arr)):
            if arr[i] < arr[j]:
                next = arr[j]
                break
        print("Next Greater Element for {} is {}".format(arr[i], next))
    print("PS: This program returns next greater element as None if no greater element if found in the list.")


x = [13, 7, 6, 12]
nextGreaterElement(x)
