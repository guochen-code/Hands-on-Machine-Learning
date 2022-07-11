(1)
X_train['Age_NA'] = np.where(X_train['age'].isnull(), 1, 0)
X_test['Age_NA'] = np.where(X_test['age'].isnull(), 1, 0)


(2)
# Let's create a list with the name of the new variables
indicators = [f"{var}_NA" for var in cols_to_use]

# Let's add the indicators
X_train[indicators] = X_train[cols_to_use].isna().astype(int)
X_test[indicators] = X_test[cols_to_use].isna().astype(int)
