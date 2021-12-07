def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


a = [10, 23, 43, 78, 90, 26]
x = 90
result = search(a, x)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")

