from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
num_pipeline = Pipeline([
('imputer', SimpleImputer(strategy="median")),
('attribs_adder', CombinedAttributesAdder()),
('std_scaler', StandardScaler()), # alternative: MinMaxScaler()
])
dataset_num_tr = num_pipeline.fit_transform(dataset_num)


# one transformer to take care of all numeric and categorical columns:
from sklearn.compose import ColumnTransformer
num_attribs = list(dataset_num) # get numeric columns
cat_attribs = ["categorical_columns"] # get catgorical columns
full_pipeline = ColumnTransformer([
("num", num_pipeline, num_attribs),
("cat", OneHotEncoder(), cat_attribs),
])
dataset_prepared = full_pipeline.fit_transform(dataset)
