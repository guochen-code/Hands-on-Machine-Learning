# three(3) common methods:

# 1) min-max scaling
# (x-min)/(max-min), bound values to a specific range from 0 to 1.
# neural networks often expect an input value ranging from 0 to 1.
# largely affected by outliers/mistakes.
from sklearn.preprocessing import MinMaxScaler
MinMaxScaler()

# 2) z-score/standardization
# (x-average)/standard deviation
# resulting distribution has unit variance.
# much less affected by outliers/mistakes.
# may be a problem to some algorithms like neural networks.
from sklearn.preprocessing import StandardScaler
StandardScaler()

# 3) robust sscaling
# similar to min-max, but instead maps the interquartile range (the 75th percentile value minus the 25th percentile value) to (0,1). 
# this means the variable itself takes values outside of the (0,1) interval. 
# impacted least by the extreme values.
from sklearn.preprocessing import RobustScaler
RobustScaler()
