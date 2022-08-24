# extract am and pm / pd.to_datetime()

df_attempts['start_time']= pd.to_datetime(df_attempts['start_time'])

df_attempts['month']=df_attempts['start_time'].dt.month
df_attempts['hour']=df_attempts['start_time'].dt.hour

df_am=df_attempts[df_attempts['hour']<12]
df_pm=df_attempts[df_attempts['hour']>=12]

# calculate duration

df_drop_0['diff']=df_drop_0['end_time']-df_drop_0['start_time'] # show in minutes

df_drop_0['diff'].dt.seconds # convert to seconds


# pd.Timedelta
pd.Timedelta("1 hours")
df_drop_0['start_plus']+pd.Timedelta("24 hours")

# frequency + resample
df_attempts.groupby([pd.Grouper(key='start_time',freq='M')])['score'].sum() # option 1 monthly total score

df_test.set_index('start_time').resample('M')['score'].sum() # option 2 monthly total score

df_test.set_index('start_time').resample('Y').sum()['score'] # yearly total score



********************************************************************** datetime vs pd.to_datetime ***************************************************************
# convert string to datetime
datetime.strptime('2023-02-24 16:05:52', "%Y-%m-%d %H:%M:%S") # need to specify the format

pd.to_datetime('2023-02-24 16:05:52') # no need to specify the format. quite flexible and get the same result if input '02-24-2023 16:05:52'
# but beware that the "first position" 02 will be considered the ***month*** by default!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! unless input '24-02-2023 16:05:52'
# where 24 is bigger than 12 so it can't be month, will automatically adjust to day
# note this will apply to ONLY one value, if you have a list, for other values it still apply that first position is the month!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# you can also specifiy the format:
pd.to_datetime('02-01-2023 16:05:52',format="%d-%m-%Y %H:%M:%S")
# note that first position would be day!!!!!!!!!!! output:
'''
Timestamp('2023-01-02 16:05:52')
'''

pd.Timestamp.now() -> # Timestamp('2022-08-24 10:56:44.795747')
print(pd.Timestamp.now()) -> # 2022-08-24 10:56:29.677588
datetime.now() -> # datetime.datetime(2022, 8, 24, 10, 57, 42, 283579)
print(datetime.now()) -> # 2022-08-24 10:56:29.936571

###################################################################### timezone conversion 
# Create a timestamp object with UTC timezone:
ts = pd.Timestamp('2020-03-14T15:32:52.192548651', tz='UTC')
ts
'''
Timestamp('2020-03-14 15:32:52.192548651+0000', tz='UTC')
'''
#Change to Tokyo timezone:
ts.tz_convert(tz='Asia/Tokyo')
'''
Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
'''
# Can also use astimezone:
ts.astimezone(tz='Asia/Tokyo')
'''

************************************************************************ example
df=pd.DataFrame()
df['time']=['03-02-2023 16:05:52','02-10-2023 16:05:52','24-02-2023 16:05:52']
df['dt']=pd.to_datetime(df['time'])
df
	time	dt
0	03-02-2023 16:05:52	2023-03-02 16:05:52
1	02-10-2023 16:05:52	2023-02-10 16:05:52
2	24-02-2023 16:05:52	2023-02-24 16:05:52
df['dt']=pd.to_datetime(df['time'],format='%d-%m-%Y %H:%M:%S') # Has to be capital Y for the year!
df
  time	dt
0	03-02-2023 16:05:52	2023-02-03 16:05:52
1	02-10-2023 16:05:52	2023-10-02 16:05:52
2	24-02-2023 16:05:52	2023-02-24 16:05:52
Timestamp('2020-03-15 00:32:52.192548651+0900', tz='Asia/Tokyo')
'''
