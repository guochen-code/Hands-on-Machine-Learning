# (1) winsorization: clip features values between two chosen values of lower bound and upper bound
pd.Series(x).hist(bins=30)
upperbound,lowerbound=np.percentile(x,[1,99])
y=np.clip(x,upperbound,lowerbound)
pd.Series(y).hist(bins=30)

# (2) rank transformation (concatenate train and test data before applying the rank transformation)
rank([-100,0,1e5])==[0,1,2]
rank([1000,1,10])=[2,0,1]
scipy.stats.rankdata

# (3) log transform
np.log(1+x)

# (4) raising to the power <1
np.sqrt(x+2/3)
