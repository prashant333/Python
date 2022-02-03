""" find the first and last index of a given input in sorted list. Return output in [x,y] format.
 if target is not present in the given list, return [-1, -1]
"""

result = []


def firstLast(arr, t):

    for i in range(len(arr)):
        if arr[i] == t:
            result.append(i)
            while i+1 < len(arr) and arr[i+1] == t:
                i += 1
            result.append(i)
            break
    return result


z = [1,1,2,4,5,5,5,5,5,7,7,7,7,7,7,9]
print(firstLast(z, 7))
