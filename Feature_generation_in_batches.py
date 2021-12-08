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

(1) PolynominalFeatures before Scaler
# PolynomialFeatures has to be done prior to scaler in pipeline: if you standardize first you will end up with negative and positive values 
# for values that have all been positive, therefore changing all the interaction terms. Also bring them down to a smaller scale. so rather than the first value times the second
# value both being above 1 and therefore increasing the value even more. If you scale it down to values that are maybe 0.5 and 2, we are actually reducing the value.
(2) Watch out if use lasso or ridge
# pf=PolynomialFeatures(degree=2,include_bias=False)
X_pf=pf.fit_transform(X)
# because linear lasso or ridge model used later already have this bias term(intercept) in their model.
