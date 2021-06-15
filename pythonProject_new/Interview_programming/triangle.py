# This set of code returns * printed in triangle pattern.
"""
# method 1
def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):

        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i + 1):

            print("* ", end="")

        print("\r")
"""
# another way of printing triangle using list

"""
# method 2
def triangle(n):
    myList = []
    for i in range(1, n+1):
        myList.append("*"*i)
    print("\n".join(myList))
"""

# method 3


def triangle(n):
    for i in range(1, n + 1):
        # ljust(), rjust() will shift the pattern to left and right respectively
        print(str('#'*i).ljust(n))


n = int(input("Enter value:"))
triangle(n)


