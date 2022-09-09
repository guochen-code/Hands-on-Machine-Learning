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
