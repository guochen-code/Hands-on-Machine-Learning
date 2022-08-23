import pytz
from datetime import datetime, tzinfo, timedelta

my_var = -5 # GMT-5
UTC_timezone=pytz.timezone('UTC')
rig_time = datetime.now(rig_timezone) + timedelta(hours= my_var)
rig_time.strftime('%Y-%m-%d %I:%M:%S %p')
