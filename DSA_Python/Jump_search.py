import math
#import Linear_search


def linear_search(B, item, loc):
    print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return loc+i
        i += 1
    return -1


def jump_search(arr, x, l):
    print("\t Entering Jump search")
    m = int(math.sqrt(l))
    i = 0
    while i <= l-1:
        print("Processing Block - {}".format(arr[i: i + m]))
        if arr[i+m-1] == x:
            return i+m-1
        elif arr[i+m-1] > x:
            B = arr[i: i+m-1]
            return linear_search(B, x, i)
        i += m

    B = arr[i:i + m]
    print("Processing Block - {}".format(B))
    return linear_search(B, x, i)


a= [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
l = len(a)
result = jump_search(a, 233, l)
print("Element is present at index " + str(result))

"""
Let's do a more general analysis of how Jump Search performs. We'll once again consider the worst-case scenario 
where the element to be found is at the end of the list.

For a list of n elements and a block size of m, Jump Search would ideally perform n/m jumps. Considering the 
block size to be as √n, the runtime too would be O(√n).

This puts Jump Search in between Linear Search (worst) with a runtime complexity of O(n) and Binary Search (best) 
with a runtime complexity of O(log n). Hence, Jump Search can be used in places where the binary search is not 
feasible and linear search is too costly.
"""