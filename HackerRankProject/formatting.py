# String formatting.
def print_formatted(number):
    n = number

    # below line formats a given number into a binary, and we take the length of 
    # that output to be used later for getting the max size of each output.

    width = len("{0:b}".format(n))

    # Please refer the following link for more info: "https://thepythonguru.com/python-string-formatting/"

    for i in range(1, n+1):

        # part within curly brace can be interpreted as "{default_value:width of output followed by format code}"
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
