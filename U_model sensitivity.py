# outliers

(1) Some machine learning models are sensitive to outliers. For instance, AdaBoost may treat outliers as "hard" cases and put tremendous weights on them, 
thus producing a model with poor generalisation.

(2) Linear models, in particular linear regression, can also be sensitive to outliers.

(3) Decision trees-based models are robust to outliers. Decision trees make decisions by asking if variable x is >= than a certain value, 
and therefore the outlier will fall on each side of the equation, but it will be treated similarly to non-outlier values.

If the variable is normally distributed (Gaussian), then the values that lie outside the mean, plus or minus 3 times the standard deviation of the variable, 
are considered outliers.

outliers = mean +/- 3* std.

If the variable is skewed, a general approach is to calculate the quantiles, and then the inter-quartile range (IQR):

IQR = 75th quantile - 25th quantile
An outlier will sit outside the following upper and lower boundaries:

Upper boundary = 75th quantile + (IQR * 1.5)

Lower boundary = 25th quantile - (IQR * 1.5)

or for extreme cases:

Upper boundary = 75th quantile + (IQR * 3)

Lower boundary = 25th quantile - (IQR * 3)

# variable magnitude

Magnitude matters because:
- The regression coefficient is directly influenced by the scale of the variable. (even though model performance may be the same)
- Variables with a larger magnitude dominate those with a smaller magnitude.
- Gradient descent converges faster when features are on similar scales.
- Feature scaling helps decrease the time it takes to find support vectors for SVMs.
- Euclidean distances are sensitive to feature magnitude.

The machine learning models affected by the feature magnitude are:
(1) Linear and Logistic Regression.
(2) Neural Networks.
(3) Support Vector Machines (SVMs).
(4) KNN.
(5) K-means clustering.
(6) Linear Discriminant Analysis (LDA).
(7) Principal Component Analysis (PCA).

Machine learning models insensitive to feature magnitude are the ones based on trees:
(1) Classification and Regression Trees.
(2) Random Forests (RF.
(3) Gradient Boosted Trees.
                    
                    
***************************************************************************************************************************************************************
# Function to find upper and lower boundaries
# for skewed variables.


def find_skewed_boundaries(df, variable, distance): # distance = 1.5 or 3

    # Let's calculate the boundaries
    # for skewed distributions

    # The parameter "distance" gives us the option to
    # estimate 1.5 times or 3 times the IQR when defining
    # the boundaries.

    IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)

    lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
    upper_boundary = df[variable].quantile(0.75) + (IQR * distance)

    return upper_boundary, lower_boundary
