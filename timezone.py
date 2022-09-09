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

##################################################################### use timezone string (automatically accounts for daylight saving?)
# above example, you know the base number is utc timezone, thus -5 hours
# here you need to specify utc timezone otherwise the machine will assume the given time is in local timezone

(1) assgin timezone
ts=1662741316000
utc_dt = datetime.utcfromtimestamp(ts / 1000.0)
print(utc_dt) -> 2022-09-09 16:35:16 # no timezone assigned, machine will assume it is in local timezone !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
utc = pytz.timezone('UTC')
utctime = utc.localize(utc_dt)
print(utctime) -> datetime.datetime(2022, 9, 9, 16, 35, 16, tzinfo=<UTC>) # has timezone information !!!!!!!!!!!!!!!!

(2) convert to a different timezone
target_tz = pytz.timezone('America/Denver')
target_tz.normalize(utctime.astimezone(target_tz)).strftime('%Y-%m-%d %I:%M:%S %p') -> '2022-09-09 10:35:16 AM'
localtz.normalize(utctime.astimezone(localtz)).dst() # check daylight saving time -> datetime.timedelta(seconds=3600)


********************************************************************* above in MTD, GMT-6 *************************************************************************

********************************************************************* check in MST, GMT-7 *************************************************************************

# it is indeed automatically taken care by pytz
ts=1670002560000
utc_dt = datetime.utcfromtimestamp(ts / 1000.0)
utc = pytz.timezone('UTC')
utctime = utc.localize(utc_dt)
utctime.strftime('%Y-%m-%d %I:%M:%S %p') -> '2022-12-02 05:36:00 PM'
localtz = pytz.timezone('America/Denver')
localtz.normalize(utctime.astimezone(localtz)).strftime('%Y-%m-%d %I:%M:%S %p') -> '2022-12-02 10:36:00 AM'
localtz.normalize(utctime.astimezone(localtz)).dst() -> datetime.timedelta(0)
