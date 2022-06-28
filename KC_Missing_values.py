(1) missing values can be hidden from us and replaced by other value such as -1 or already replaced by the mean value / plot histogram to identify any unusal peaks.
(2) fillna approaches:
  2.1 -999,-1 etc: replace nan with some value outside fixed value range. The downside of this is that performance of linear models and neural networks can suffer.
  2.2 mean, median: beneficial for simple linear models and neural networks. But again for trees it can be harder to select object which had missing values in the first place.
  2.3 reconstruct value: rare case. maybe in time series.
(3) create isnull feature.
(4) In general, avoid replacing missing values before feature generation, because it can decrease usefulness of the features.
    Be very careful when generating new feature using columns with missing values. for example, ignore missing values when calculate means for each category.
(5) sometimes we can treat outliers as missing values. i.e. people born in future.
(6) xgb can handle NAN.

# appendix
(1) missing values:
The function and plots were done with the idea of "seeing" the impact of missing data on the house sales price.
If observations with missing data have, on average, lower (or higher) sales price than the rest, we could, in principle, 
infer that the fact that data is missing will be useful to better predict the price.
A silly example: we have the variable house build year, for most houses we have the value for that variable, 
  but for newer houses that were built from 2 years ago onward, the build year is still not on our records 
  (say the constructing company had problems with sending the information to us). 
  On average, the house price for newer houses will be higher. 
  We do not know that these houses are newer because we do not have the build year information. 
  But, we can use the fact that the data is missing to infer the higher cost of the house.
That is regarding the plots an the function you mention.
Regarding "handling" variables with missing data, we need to impute all missing data in all the variables that we want to use to train the model, 
because sklearn models do not work with NA. We can choose one strategy and apply that to all variables, or, 
if we have time, we can choose different strategies for different variables based on their characteristics and the percentage of missing data. 

# while Exploring the evolution of Prices with Year-variables; You have selected the median of Price not mean; any specific reason for it?
If the variable is not normally distributed, I tend to prefer the median over the mean 
because it is a better representation of the majority of the observations.

