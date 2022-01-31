# countdown timmer using python
import time


def countdown(t):
    while t:
        minute, sec = divmod(t, 60)
        # timer = '{:02d}:{:02d}'.format(minute, sec)
        timer = f'{minute:02d}:{sec:02d}'
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print("Countdown completed!")


t = int(input("Enter time in seconds: "))
countdown(t)
