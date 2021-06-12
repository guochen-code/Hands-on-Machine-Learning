# Tell which hyperparameters you want it to experiment with and what values to try out
# It will evaluate all the possible combinations of hyperparameter values, using cross-validation.
from sklearn.model_selection import GridSearchCV
param_grid = [
{'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
{'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid, cv=5,
scoring='neg_mean_squared_error',
return_train_score=True)
grid_search.fit(housing_prepared, housing_labels)
# All in all, the grid search will explore 12 + 6 = 18 combinations of RandomForestRegressor hyperparameter values, and it will train each model five times (since we are
# using five-fold cross validation). In other words, all in all, there will be 18 × 5 = 90 rounds of training!

# Finally, you can get the best combination of parameters like this:
grid_search.best_params_

grid_search.best_estimator_


#If GridSearchCV is initialized with refit=True (which is the default), then once it finds the best estimator using crossvalidation,
# it retrains it on the whole training set. This is usually a good idea since feeding it more data will likely improve its performance.

# One step further: Randomized Search
# The grid search approach is fine when you are exploring relatively few combinations, like in the previous example, but when the hyperparameter search space is large, it is
# often preferable to use RandomizedSearchCV instead. This class can be used in much the same way as the GridSearchCV class, but instead of trying out all possible combinations,
# it evaluates a given number of random combinations by selecting a random value for each hyperparameter at every iteration.
# This approach has two main benefits:
# • If you let the randomized search run for, say, 1,000 iterations, this approach will explore 1,000 different values for each hyperparameter (instead of just a few values
# per hyperparameter with the grid search approach).
# • You have more control over the computing budget you want to allocate to hyperparameter search, simply by setting the number of iterations.
