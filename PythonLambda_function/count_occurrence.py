# count the occurrence of an item in a given list.

"""
Below code used counter built in method to count the occurrences of all the elements.
from collections import Counter
cntr = Counter(givenList)
#Counter({3: 4, 5: 3, 4: 2, 8: 2, 0: 2, 2: 2, 1: 1})
cntr[5]
# 3
"""

def countOccurrence(givenList, val):
    check_list = lambda i: givenList[i] == val
    result = sum(1 for i in range(len(givenList)) if check_list(i))
    return result


givenList = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
print(countOccurrence(givenList, 5))
