import pytz
import datetime
country='Europe/Moscow'

tz_to_display= pytz.timezone(country) # timezone of the country
local_time=datetime.datetime.now(tz=tz_to_display) # return the present time there 
print("The time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.now()))

#print(pytz.country_names)

for x in pytz.country_names:
    print("{}: {}".format(x,pytz.country_names[x]),end='\n')
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display=pytz.timezone(zone)
            local_time=datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}: {}".format(zone,local_time))
    else:
        print("\t\tNo time zone defined")
        