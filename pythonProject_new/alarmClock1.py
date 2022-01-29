""" This program demonstrates how to build alarm clock using python."""

import os
import time
import datetime
import random
import webbrowser

print("********* Alarm Clock *********")
# checking if the video file is present or not.
if not os.path.isfile("alarmSong.txt"):
    print("creating alarm file..")
# if the video file is not present we create one.
    with open("alarmSong.txt", 'w') as alarmSong:
        alarmSong.write("https://www.youtube.com/watch?v=g-F7pvOlbdw")

# validating the time input


def checkAlarmTime(t):
    # hour format

    if len(t) == 1:
        if 0 <= t[0] <= 24:
            return True
    # hour and minute format

    elif len(t) == 2:
        if 0 <= t[0] <= 24 and 0 <= t[1] <= 60:
            return True

    # hour, minute and second format
    elif len(t) == 3:
        if 0 <= t[0] <= 24 and 0 <= t[1] <= 60 and 0 <= t[2] <= 60:
            return True
    else:
        return False


print("Please set a time for the alarm (Ex. 10:15 or 22:20:50)")
while True:

    # taking user input for alarm time

    alarm_time = list(map(int, (input(">> ").strip().split(":"))))
    try:
        if checkAlarmTime(alarm_time):
            break
        else:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter value in HH:MM or HH:MM:SS format")

# convert the time to seconds
seconds_hms = [3600, 60, 1]  # Number of seconds in an Hour, Minute, and Second
alarm_seconds = sum([a*b for a, b in zip(seconds_hms[:len(alarm_time)], alarm_time)])
# Get the current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a, b in zip(seconds_hms, [now.hour, now.minute, now.second])])
# Calculate the number of seconds until alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds
# If time difference is negative, set alarm for next day
if time_diff_seconds < 0:
    # set the alarm for next day
    alarm_time += 86400

print("Alarm will go off in {}".format(datetime.timedelta(seconds=time_diff_seconds)))
# sleep until alarm time.
time.sleep(time_diff_seconds)

print("It's time to wake up!")
# open the alarm file
with open("alarmSong.txt", "r") as alarmfile:
    select_video = alarmfile.readlines()
# from the videos select a random video and open in browser.
webbrowser.open(random.choice(select_video))
