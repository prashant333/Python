
def simpleArraySum(ar):
    total = 0
    for i in range(0, len(ar)):
        total = total + ar(i)
    return total


if __name__ == '__main__':

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)
