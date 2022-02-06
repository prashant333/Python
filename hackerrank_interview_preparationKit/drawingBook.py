#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    return min(p//2, n//2-p//2)


"""
n//2 is the number of pages to flip to reach page n
p//2 is the number of pages to flip to reach p from the front
n//2 - p//2 is the number of pages to flip to reach p from the back 
"""
n = int(input("Length of the book: "))
p = int(input("Page number to flip:"))

print(pageCount(n,p))
