# prepare data
import csv 
data = [1,2,3,4,5] 


# define function
from csv import writer
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)
        
        
# write to the csv file     
append_list_as_row('odd_test.csv', data)

# transpose
import pandas as pd
df=pd.read_csv('odd_test.csv',header=None)
df.transpose()

**************************************************************************************************************************************************
# multiple dataframe to csv
import os
for data in [df,df_new1,df_new2]:
    display(data)
    if os.path.isfile('filename.csv'):
        data.to_csv('filename.csv',mode='a',index=False,header=False)
    else:
        data.to_csv('filename.csv',mode='w',index=False)
