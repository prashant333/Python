# Gives a list of fibonacci numbers.

def fibonacci(n):
    lis = [0, 1]
    for i in range(2, n):
        lis.append(lis[i - 2] + lis[i - 1])
    return lis[0:n]


print(fibonacci(10))
