"""
Library fine program using python.

Given the expected and actual return dates for a library book, create a program that calculates the
 fine (if any). The fee structure is as follows:

1. If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)

2. If the book is returned after the expected return day but still within the same calendar month and year
 as the expected return date, fine = 15 * (number of days late)
3. If the book is returned after the expected return month but still within the same calendar year as the
expected return date, the fine = 500 * (number of months late)
4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000

Charges are based only on the least precise measure of lateness. For example, whether a book is due January 1, 2017
or December 31, 2017, if it is returned January 1, 2018, that is a year late and the fine would be 10,000.t
"""

import datetime
import math
import random


def libraryFine(d1, m1, y1, d2, m2, y2):

    date_actual = datetime.datetime(y1,m1,d1)
    date_expected = datetime.datetime(y2,m2,d2)

    if date_expected >= date_actual:
        return "No fine"


first_multiple_input = input("Please give the actual return date").rstrip().split()

d1 = int(first_multiple_input[0])

m1 = int(first_multiple_input[1])

y1 = int(first_multiple_input[2])

second_multiple_input = input("Please give the expected  return date").rstrip().split()

d2 = int(second_multiple_input[0])

m2 = int(second_multiple_input[1])

y2 = int(second_multiple_input[2])

result = libraryFine(d1, m1, y1, d2, m2, y2)

print(result)