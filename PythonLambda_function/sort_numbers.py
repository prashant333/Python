# This program used lambda function to sort a gievn list.
"""
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
"""
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]

result = sorted(array_nums, key=lambda x: 0 if x == 0 else -1/x)
print(result)

