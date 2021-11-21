(1) missing values can be hidden from us and replaced by other value such as -1 or already replaced by the mean value / plot histogram to identify any unusal peaks.
(2) fillna approaches:
  2.1 -999,-1 etc: replace nan with some value outside fixed value range. The downside of this is that performance of linear models and neural networks can suffer.
  2.2 mean, median: beneficial for simple linear models and neural networks. But again for trees it can be harder to select object which had missing values in the first place.
  2.3 reconstruct value: rare case. maybe in time series.
(3) create isnull feature.
(4) In general, avoid replacing missing values before feature generation, because it can decrease usefulness of the features.
    Be very careful when generating new feature using columns with missing values. for example, ignore missing values when calculate means for each category.
(5) sometimes we can treat outliers as missing values.
(6) xgb can handle NAN.
