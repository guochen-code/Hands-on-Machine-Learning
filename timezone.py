import pytz
from datetime import datetime, tzinfo, timedelta

my_var = -5 # GMT-5
UTC_timezone=pytz.timezone('UTC')
rig_time = datetime.now(UTC_timezone) + timedelta(hours= my_var)
rig_time.strftime('%Y-%m-%d %I:%M:%S %p')


# from timestamp in miliseconds, e.g. 1662739495000
utc_dt = datetime.utcfromtimestamp(ts / 1000.0)
rig_time = utc_dt + timedelta(hours=gmt_offset)
connection_time = rig_time.strftime('%Y-%m-%d %I:%M:%S %p')


example:
from datetime import datetime, timedelta
import pytz

##################################################################### use -/+ a number from UTC
ts=1662739495000
utc_dt = datetime.utcfromtimestamp(ts / 1000.0)
print(type(utc_dt))
rig_time = utc_dt + timedelta(hours=-5)
connection_time = rig_time.strftime('%Y-%m-%d %I:%M:%S %p')
connection_time
'''
<class 'datetime.datetime'>
'2022-09-09 11:04:55 AM'
'''

##################################################################### use timezone string (good for daylight saving?)
utc_dt.astimezone(pytz.timezone("Asia/Hong_Kong"))
'''
datetime.datetime(2022, 9, 10, 6, 4, 55, tzinfo=<DstTzInfo 'Asia/Hong_Kong' HKT+8:00:00 STD>)
'''

utc_dt.astimezone(pytz.timezone("Asia/Hong_Kong")).strftime('%Y-%m-%d %I:%M:%S %p')
'''
'2022-09-10 06:04:55 AM'
'''


  
