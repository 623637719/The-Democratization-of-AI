Normalization is a data preprocessing technique used to standardize the range of independent variables or features of data. It is a common requirement for many machine learning algorithms, as they tend to perform better when the input features are on a similar scale.

The main reasons for normalizing data are:

1. Scale Differences: Without normalization, features with large numeric ranges will dominate the objective function of a machine learning algorithm, overshadowing features with smaller ranges. This can lead to poor model performance.
2. Numerical Stability: Many machine learning algorithms, such as gradient-based optimizers, perform better when the input features are on a similar scale. Normalization helps improve numerical stability and convergence during the training process.
3. Faster Convergence: Normalization can lead to faster convergence of the optimization algorithms used in machine learning models, as the parameters can be updated more effectively.
There are several normalization techniques, the most common ones are:

## Min-Max Normalization (Feature Scaling): 

This technique rescales the features to a common range, usually between 0 and 1. 

Let's assume we have a input X with the following characteristics:

Minimum value of X is X_min
Maximum value of X is X_max

An individual data point from the feature X is represented as x

x_normalized = (x - X_min) / (X_max - X_min)

(x - X_min): This part subtracts the minimum value of the feature X from the individual data point x. This shifts the values so that the minimum value becomes 0.
(X_max - X_min): This part calculates the range of the feature X, which is the difference between the maximum and minimum values.
(x - X_min) / (X_max - X_min): This part divides the shifted value from step 1 by the range calculated in step 2. This rescales the values to the range between 0 and 1.
The resulting x_normalized value will be between 0 and 1, where 0 represents the minimum value of the original feature X, and 1 represents the maximum value of the original feature X.

### Between -1 and 1

x_normalized = 2 * (x - X_min) / (X_max - X_min) - 1
