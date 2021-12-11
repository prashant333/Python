"""
 selection sort example.

The selection sort algorithm sorts an array by repeatedly finding the minimum element (considering ascending order)
from unsorted part and putting it at the beginning
"""


def selection_sort(li):
    for i in range(len(li)):
        min_idx = i
        for j in range(i + 1, len(li)):
            if li[min_idx] > li[j]:
                min_idx = j
        li[i], li[min_idx] = li[min_idx], li[i]

    print(li)


b = [18, 40, 32, 15]
selection_sort(b)
