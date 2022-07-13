# Imputing
# first to check how many missing values and ask why missing?
# drop missing
# fill missing: column mean value, backfill, forward fill
# categorical encoding then fill missing for categorical features
data_set.dropna(subset=["column_name"]) #drop missing rows for the column
data_set.drop("column_name", axis=1) #drop the entire column
median = data_set["column_name"].median() 
data_set["column_name"].fillna(median, inplace=True) # fill missing with mean value
# using SimpleImputer
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
# drop categorical columns
data_set_num = data_set.drop("categorical_columns", axis=1)
imputer.fit(data_set)
# check results
imputer.statistics_
housing_num.median().values
# do the job
X = imputer.transform(data_set_num)
#The result is a NumPy array. Back to dataframe:
data_set = pd.DataFrame(X, columns=data_set_num.columns)
********************************************************************************************************************************
# Encoding (ordinal and one-hot encoding)
# 1) ordinal
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
dataset_cat_encoded = ordinal_encoder.fit_transform(dataset_cat)
# list of categories
ordinal_encoder.categories_
# 2) one-hot
>>> from sklearn.preprocessing import OneHotEncoder
>>> cat_encoder = OneHotEncoder()
>>> data_cat_1hot = cat_encoder.fit_transform(dataset_cat)
# data_cat_1hot is a SciPy sparse matrix, instead of a NumPy array. Save memory.
# convert to array if you want:
housing_cat_1hot.toarray()
# check list of categories:
cat_encoder.categories_


*********************************************
from pandas import get_dummies
df=pd.get_dummies(df,columns=one_hot_encode_cols,drop_first=True) # reduce multi-colinearality

one_hot_encode_cols=df.dtypes[df.dtypes==np.object]
one_hot_encode_cols=one_hot_encode_cols.index.tolist()

'''
In practice, we shouldn't be using get-dummies in our machine learning pipelines. It is however useful, for a quick data exploration. Let's look at this with examples.

If the variable colour has 3 categories in the train data, it will create 2 dummy variables. 
However, if the variable colour has 5 categories in the test data, it will create 4 binary variables, 
therefore train and test sets will end up with different number of features and will be incompatible with training and scoring using Scikit-learn.
'''
