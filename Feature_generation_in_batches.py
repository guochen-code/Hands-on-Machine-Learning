######## Z-score feature
def add_deviation_feature(X,feature,category):
  category_gb=X.groupby(category)[feature]
  category_mean=category_gb.transform(lambda x:x.mean())
  category_std=category_gb.transform(lambda x: x.std())
  deviation_feature=(X[feature]-category_mean)/category_std
  X[feature+'_Dev_'+category]=deviation_feature
  
  

######## Polynomial features
from sklearn.preprocessing import PolynominalFeatures
pf=PolynominalFeatures(degree=2)
features=['a','b','c']
pf.fit(df[features])
pf.get_feature_names() ##################################################################################### return x0,x1,x0^2,X0 X1, X1^2
feature_array=pf.transform(df[features])
pd.DataFrame(feature_array,columns=pf.get_feature_names(input_features=features)) ############################ return real names

#### PolynomialFeatures has to be done prior to scaler in pipeline: if you standardize first you will end up with negative and positive values 
for values that have all been positive, therefore changing all the interaction terms. Also bring them down to a smaller scale. so rather than the first value times the second
value both being above 1 and therefore increasing the value even more. If you scale it down to values that are maybe 0.5 and 2, we are actually reducing the value.
