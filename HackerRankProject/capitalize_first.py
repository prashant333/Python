#!/bin/python3
# Complete the solve function below.

def solve(s):
    words = s.split(" ")
    capitalized_words = [w.capitalize() for w in words]
    return " ".join(capitalized_words)


if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
