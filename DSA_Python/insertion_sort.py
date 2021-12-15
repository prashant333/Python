# this program implements the insertion sort algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        while arr[i-1] > key and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
    return arr


x = [6, 8, 2, 12, 4]
result = insertion_sort(x)
print(result)
