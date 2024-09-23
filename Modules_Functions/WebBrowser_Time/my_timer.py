import time
from time import time as my_timer
import random

input("Press Enter to start")

wait_time=random.randint(1,6) # randint function generates random integer between 1 and 6 
time.sleep(wait_time)# pauses the execution of the program for wait_time seconds.
start_time=my_timer()
input("Press Enter to stop")

end_time=my_timer()

print("Started at "+time.strftime("%X",time.localtime(start_time)))
print("Ended at "+time.strftime("%X",time.localtime(end_time)))
print(f"Your reaction time was {end_time-start_time} seconds")

'''
pref_counter -> it is the most precise clock and its very useful for bench maring in 
code {higher resolutions}

monotonic -> Measures the elapsed time(time taken by an event to occur between the start of the time and the end of the time)
in a monotonic manner.The current value of a monotonic clock, which is 
"guaranteed never to go backward."

process_time -> return the time that CPU spends executing the current process rather than the
actual elapsed time 

'''
# if we want to measure actual elapsed time: best is to use the perf_counter