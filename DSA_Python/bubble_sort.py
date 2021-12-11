""" Python program for bubble sort.

Bubble sort works by repeatedly swapping the two elements if they are in wrong order.
"""


def bubble_sort(a):
    # this is used to traverse the entire list
    for i in range(len(a)):
        # here we decrement the count by i and 1, since the last elements are already sorted form the last loop.
        for j in range(0, (len(a)-i-1)):
            # comparing the two concurrent list items.
            if a[j] > a[j+1]:
                # swapping the two elements if they in wrong order.
                a[j], a[j+1] = a[j+1], a[j]
    return a


a = [5, 1, 4, 2, 8]
result = bubble_sort(a)
print(result)
