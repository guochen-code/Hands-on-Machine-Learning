from sklearn.model_selection import train_test_split
train_set, test_set = train_test_split(data_set, test_size=0.2, random_state=42)
# alternatively, [X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)], if x/y splitted.
# Random sampling is fine given a large enough data set. 
# Otherwise, it will introduce a significant sampling bias, not representative of the whole population.
# Solutions: stratified sampling. The population is divided into homogeneous subgroups called strata, and the right number of instances is sampled from each stratum to guarantee that the test set is representative of the overall population.
# However, you should not have many strata as it is important to have sufficient number of instances in each stratum otherwise the estimate of stratum's importance may be biased.
# steps:
# 1. select an important attribute to predict the target variable.
# 2. select reasonable number of strata.
# 3. use pd.cut() function to create the selected attribute_rename with decided number of categories.
data_set["selected attribute_rename"] = pd.cut(data_set["selected attribute"], bins=[#1, #2, #3, #4, #5, np.inf], labels=[1, 2, 3, 4, 5])

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(data_set, data_set["selected attribute_rename"]):
strat_train_set = data_set.loc[train_index]
strat_test_set = data_set.loc[test_index]

# check the selected attribute category proportions in the test set:
strat_test_set["selected attribute_rename"].value_counts() / len(strat_test_set)

# Now you should remove the selected attribute so the data is back to its original state:
for set_ in (strat_train_set, strat_test_set):
set_.drop("selected attribute_rename", axis=1, inplace=True)

  
  
def split_train_test(data, test_ratio):
  shuffled_indices = np.random.permutation(len(data))
  test_set_size = int(len(data) * test_ratio)
  test_indices = shuffled_indices[:test_set_size]
  train_indices = shuffled_indices[test_set_size:]
  return data.iloc[train_indices], data.iloc[test_indices]
