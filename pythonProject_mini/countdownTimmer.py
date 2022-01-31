# countdown timmer using python
import time


def countdown(t):
    while t:
        minute, sec = divmod(t, 60)  # used to convert given input into minutes and second
        # timer = '{:02d}:{:02d}'.format(minute, sec)
        timer = f'{minute:02d}:{sec:02d}'
        print(timer, end="\r")  # print the counter
        time.sleep(1)   # while loop will run every 1 sec, hence printing the counter with decreasing sec count.
        t -= 1          # reduce the time, i,e sec by 1
    print("Countdown completed!")


t = int(input("Enter time in seconds: "))
countdown(t)
