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
