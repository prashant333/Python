""" Python program for bubble sort.

Bubble sort works by repeatedly swapping the two elements if they are in wrong order.
"""


def bubble_sort(a):
    for i in range(len(a)):
        for j in range(0, (len(a)-i-1)):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

    return a


a = [5, 1, 4, 2, 8]
result = bubble_sort(a)
print(result)
