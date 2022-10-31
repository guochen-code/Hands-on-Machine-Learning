import json

d_new=pd.read_json('regression-104001.json')
df_result = pd.json_normalize(d_new['result'])

df = pd.DataFrame([json.loads(i) for i in df_result['oplaParams']])
ds = df[['bitDepth', 'holeDepth', 'SBP', 'SPP', 'Auto Choke', 'Choke A', 'Choke B', 'Flow In', 'autoMode',
         'Pipe Cap', 'Annular Cap', 'Well Cap', 'Target SBP', 'Choke Safe']]

# add timestamp and oplajobnumber columns
ds.insert(0, 'timestamp', pd.to_numeric(df_result['timestamp']))
ds.insert(0, 'oplajobnumber', df_result['oplajobnumber'])

******************************************************************************************

import json

d_new=pd.read_json('regression-104001.json')
df_result = pd.json_normalize(d_new['result'])

df = pd.DataFrame([i for i in df_result['oplaParams']])

******************************************************************************************
If oplaParams is string type:
    Do parse to a make Jason objects for (witsParams and oplaParams) and use them
Else:
    They are already Jason, just use them as they are
