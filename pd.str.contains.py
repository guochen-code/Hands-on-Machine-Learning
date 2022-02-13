# search for multiple values

searchfor = ['17','77','79','74']

df_search=df_1[df_1['ingredents_array'].str.contains('|'.join(searchfor))]


# not contain

name=df_tests['test_title'].str.split(' ',expand=True) # expand -> name is dataframe

df_tests[~df_tests['test_title'].str.contains('Verbal')]
