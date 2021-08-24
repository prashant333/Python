# This program demonstrate how python stores the data of an array and how the size of array grows.

import sys
data = []
for i in range(10):
    a = len(data)
    b = sys.getsizeof(data)
    print("length: {0:3d}; size in bytes: {1:4d}".format(a, b))
    data.append(None)
