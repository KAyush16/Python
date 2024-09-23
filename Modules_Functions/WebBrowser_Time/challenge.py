'''
Write a small program to display inforamtion on the :
-> four clock whose function we have just looked at: i.e, time(), pref_counter, 
monotonic() and process_time().

use the documentation for the get_clock_info() function, to work out how to call it for each of the 
clock

'''
import time

clock_type=["time", "monotonic", "perf_counter", "process_time"]
for clock in clock_type:
    info=time.get_clock_info(clock)#get_info_clock: to get info about the clock(haar ek iteration mai clock type change hoga) 
    print(f"Clock: {clock}")
    print(f"Adjustable: {info.adjustable}")
    print(f"Implementation: {info.implementation}")
    print(f"Monotonic: {info.monotonic}")
    print(f"Resolution: {info.resolution}")
    print()
    
print(time.localtime())
'''
Adjustable: Whether the clock is adjustable.
Implementation: The name of the clock's implementation.
Monotonic: Whether the clock is monotonic.
Resolution: The resolution of the clock in seconds.
'''