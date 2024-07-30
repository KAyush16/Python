import pytz
import datetime
country='Europe/Moscow'

tz_to_display= pytz.timezone(country)
local_time=datetime.datetime.now(tz=tz_to_display)
print("TImr time in {} is {}".format(country,local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))