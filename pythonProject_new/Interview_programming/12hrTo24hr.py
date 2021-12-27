# Python implementation for converting 12hr time format to 24 hr time format.

def timeConversion(s):
    # Here we check the time between 12:00:00AM to 12:59:59:AM

    if s[-2:] == "AM" and s[0:2] == "12":
        return "00" + s[2:-2]
    # Here we check the time 12:00:00PM to 12:59:59PM or 1:00:00AM to 11:59:59AM

    elif s[-2:] == "PM" and s[0:2] == "12" or s[-2:] == "AM":
        return str(s[:-2])
    # Here we check the remaining time intervals.

    elif s[-2:] == "PM":
        return str(int(s[:2])+12)+s[2:-2]


s = "07:05:45PM"
res = timeConversion(s)
print(res)
