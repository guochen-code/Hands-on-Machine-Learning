# Hands-on-Machine-Learning
Highlights in Machine Learning

Data preparation:
  train_test split (stratified sampling)
  Imputing (missing data)
  Encoding (categorical data)
  Scaling (min-max or z-score/standardization)
  Pipelines

Train models (The goal is to shortlist a few promising models):
  cross-validatoin
  underfitting
  overfitting
 
Fine tune selected models:
  GridSearch
  RandomSearch
  Ensemble
  Voting/bagging/boosting/stacking

Analyze best models and their errors:
  
Evaluate your final model on test set:
  Usually  slightly worse than the results you got with cross-validation, because you fine tuned your model to perform well on the validation data.
  DO NOT fine tune the model based on your test set.
