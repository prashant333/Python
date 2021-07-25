"""
This program extracts date and time from a given timestamp.
"""
import datetime

now = datetime.datetime.now()
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
time = lambda x: x.time()

print("year: ", year(now))
print("month:  ", month(now))
print("day: ", day(now))
print("time: ", time(now))
