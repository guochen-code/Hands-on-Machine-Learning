# label source whether from train or test dataset before concatenate these two data sets together
train['source']= 'train'
test['source'] = 'test'
data=pd.concat([train, test],ignore_index=True)
data.shape

# calculate age at year 2016
df['DOB']=['23-May-78','07-Oct-85']
df['Age'] = df['DOB'].apply(lambda x: 116 - int(x[-2:]))

#fillna with median
data['column_name'].fillna(data['column_name'].median(),inplace=True)

# new column whether missing or not in old column !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#High proportion missing so create a new var whether present or not
data['new_column_name'] = data['old_column_name'].apply(lambda x: 1 if pd.isnull(x) else 0)
#drop old
data.drop('old_column_name',axis=1,inplace=True)

# one categorical feature has 55000 A, 42000 B, and 8000 C, 6000 D, 3000 E...... label all other letters as 'Others' except for A and B
# As a result, 3 categories remain: 'A', 'B' and 'Others'
data['column_name'] = data['column_name'].apply(lambda x: 'others' if x not in ['A','B'] else x)
data['column_name'].value_counts()
[
A         55000
B         42000
Others    26000
Name: Source, dtype: int64
]
