import time

# print(time.gmtime(0))

#print(time.localtime(time.time()))

# print(time.time())

print(time.gmtime(0))
print()
time_here=time.localtime()
print(time_here)
print()
print("Year:",time_here[0],time_here.tm_year)
print("Month:",time_here[1],time_here.tm_mon)
print("Day:",time_here[2],time_here.tm_mday)
print(time_here.tm_zone)
print(time_here.tm_gmtoff)
'''
Explanation of the Output
tm_year=2024: The current year is 2024.
tm_mon=7: The current month is July.
tm_mday=6: The current day of the month is the 6th.
tm_hour=10: The current hour (in 24-hour format) is 10.
tm_min=24: The current minute is 24.
tm_sec=36: The current second is 36.
tm_wday=5: The day of the week is Friday (0 = Monday, ..., 6 = Sunday).
tm_yday=188: The day of the year is the 188th day.
tm_isdst=1: Daylight Saving Time flag is 1 
(which means DST is in effect).

'''