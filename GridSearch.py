# Input which hyperparameters what values to try out.
# It will run all combinations of hyperparameter values with cross-validation.
from sklearn.model_selection import GridSearchCV
param_grid = [
{'n_estimators': [#, #, #], 'max_features': [#, #, #, #]},
{'bootstrap': [False], 'n_estimators': [#, #], 'max_features': [#, #, #]},
]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=#,
scoring='neg_mean_squared_error',
return_train_score=True)
grid_search.fit(data_prepared, data_labels)
# The grid search above will explore different combinations of RandomForestRegressor hyperparameter values, and it will train each model # times (depending on
# how many folds cross validation you are using). 

# Finally, get the best parameters:
grid_search.best_params_

grid_search.best_estimator_

# Bonus:
# Initialize the GridSearchCV with refit=True (which is the default), it retrain the model on the whole training set with the best hyperparameter values found.

# One step further: Randomized Search
# when the hyperparameter search space is large, it is often preferable to use RandomizedSearchCV.
# This approach has two main benefits:
# • Able to explore more values per hyperparameter. Much larger search space.
# • Setting the number of iterations to have more control over computing time.
