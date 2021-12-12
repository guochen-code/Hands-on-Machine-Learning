# linear regression is going to assume normally distributed residuals, not y variable, but it can be aided by transforming y variable.

# Inverse transformation: because of previous transformation, y prediction and y are not on the same scale. we have to get them back on the same scale as our original numbers.

  
from scipy.stats.mstats import normaltest
normaltest(data.columnname.values)
# if p>0.05, fail to reject the hypothesis that it is normal.

# bocox (generalization of the square root function)
from scipy.stats import boxcox
bc_result=boxcox(data.columnname)
boxcox_columnname=bc_result[0]
lam=bc_result[1]

# inversion
from scipy.special import inv_boxcox
bc_result=boxcox(data.columnname)
boxcox_columnname=bc_result[0]
lam=bc_result[1]
inv_boxcox(boccox_columnname,lam)
