# find the pair of socks in given list.

from collections import Counter


def socksMerchant(n, ar):
    new = Counter(ar)
    count = []
    for i in new.values():
        if i > 1:
            count.append(i//2)
    return sum(count)


n = 7
a = [1, 2, 1, 2, 1, 3, 2]
print("Total number of socks pair found is :", socksMerchant(n, a))
