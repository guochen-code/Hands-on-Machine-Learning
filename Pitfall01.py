# error:
streaming Error other than read time: unsupported operand type(s) for -: 'str' and 'str'
    
# root cause:
values=['opla',1657617239000,3,4]
column_name=['opla','a1','a2','a3']
df_parameters = pd.DataFrame(np.array([values]), columns=column_name)
df_parameters.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1 entries, 0 to 0
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   opla    1 non-null      object
 1   a1      1 non-null      object
 2   a2      1 non-null      object
 3   a3      1 non-null      object
dtypes: object(4)
memory usage: 160.0+ bytes
'''
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! THEY ARE ALL OBJECT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# one solution: write to csv and read from csv
name='test666'

import os
if os.path.isfile(f'{name}.csv'):
    df_parameters.to_csv(f'{name}.csv',mode='a',index=False,header=False)
else:
    df_parameters.to_csv(f'{name}.csv',mode='w',index=False)
    
df=pd.read_csv(f'{name}.csv')

df.info()

'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   opla    5 non-null      object
 1   a1      5 non-null      int64 
 2   a2      5 non-null      int64 
 3   a3      5 non-null      int64 
dtypes: int64(3), object(1)
memory usage: 288.0+ bytes
'''

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOW THEY ARE OBJECT AND INT64 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
root cause: np.array(). remove np.array() and use list directly.
