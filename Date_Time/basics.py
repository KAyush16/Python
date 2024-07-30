import datetime

my_day1=datetime.datetime(2024,5,4,11,20,12)
print(my_day1)

my_day2=datetime.datetime(2024,5,6,13,22,14)
print(my_day2)

my_difference=my_day2-my_day1
print(my_difference)

print(my_difference.total_seconds())#in seconds 
