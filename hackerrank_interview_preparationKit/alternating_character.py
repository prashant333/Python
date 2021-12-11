#!/bin/python3
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    return count


if __name__ == '__main__':

    q = int(input("Enter total number of values: ").strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print("\n" + "result")

