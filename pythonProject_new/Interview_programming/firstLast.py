""" find the first and last index of a given input in sorted list. Return output in [x,y] format.
 if target is not present in the given list, return [-1, -1]
"""


def firstLast(arr, t):

    for i in range(len(arr)):
        if arr[i] == t:     # this is the first occurrence of the target
            start = i
            while i+1 < len(arr) and arr[i+1] == t:    # we starts to search for the last position of the target.
                i += 1
            return [start, i]      # return after the while loops is completed.

    return [-1, -1]   # return [-1,-1] if target not found


z = [1,1,2,4,5,5,5,5,5,7,7,7,7,7,7,9]
print(firstLast(z, 10))
