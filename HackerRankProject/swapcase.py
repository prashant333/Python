"""
This program demonstrate swapping of case using python.
"""


def swap_case(s):

    # builtin function swapcase()

    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
