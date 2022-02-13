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
