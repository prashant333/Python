# Program to print fibonacci sequence

from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])

val = int(input("Enter an integer: "))
print(fib(val))
