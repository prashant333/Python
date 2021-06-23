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

    """
    # Putting date into python datetime format, datetime takes input in YYYY/MM/DD format.

    date_actual = datetime.datetime(y1, m1, d1)
    date_expected = datetime.datetime(y2, m2, d2)

    # comparing date if the return date is longer than the expected date.

    if date_expected >= date_actual:
        fine = 0
        return fine

    # Comparing the year of actual return date with expected return date

    elif date_actual.year >= date_expected.year+1:
        fine = 10000
        return fine

    # If the return date is in the same month but exceeds the expected date

    elif date_actual.day > date_expected.day and date_actual.month != date_expected.month+1:
        number_of_days_late = date_actual - date_expected
        fine = 15 * number_of_days_late.days
        return fine
    """

    # second approach
    
    if y1 > y2:

        # if year of return is greater than year due

        return 10000
    elif m1 > m2 and y1 == y2:

        # if returned in the same year and month of return is greater than month due

        return (m1 - m2) * 500

    elif d1 > d2 and y1 == y2 and m1 == m2:

        # if returned in the same year and month, and the date of return is greater than due date

        return (d1 - d2) * 15
    else:
        return 0


first_multiple_input = input("Please give the actual return date : ").rstrip().split()

d1 = int(first_multiple_input[0])

m1 = int(first_multiple_input[1])

y1 = int(first_multiple_input[2])

second_multiple_input = input("Please give the expected  return date : ").rstrip().split()

d2 = int(second_multiple_input[0])

m2 = int(second_multiple_input[1])

y2 = int(second_multiple_input[2])

result = libraryFine(d1, m1, y1, d2, m2, y2)

print("$"+str(result))


