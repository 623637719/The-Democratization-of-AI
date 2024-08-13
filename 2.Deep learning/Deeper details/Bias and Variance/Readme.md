# Bias:

Bias refers to the error introduced by approximating a real-world problem with a simplified model. A model with high bias tends to oversimplify the problem and fails to capture the underlying patterns in the data. This results in poor performance on both the training and test data. High bias can lead to underfitting, where the model is unable to learn the relevant features and relationships in the data.

**Example of high bias:**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/82699827-8414-4174-bb6a-c182583df218">

# Variance:

The amount of variance refers to the difference in accuarcy between the training and testing data, this is caused by overfitting on the training data but does poorly on unseen test data. High variance models capture too many details and noise in the training data, and fail to generalize well to new, unseen examples.

**Example of high variance:**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/58e3cc42-e6de-4ff8-9e5c-2dab93d074a0">

# Just right:

**Doesn't overfit or underfit:**

<img width="500" alt="image" src="https://github.com/user-attachments/assets/e57db0f3-d6d6-4581-94b1-aa2113f1a5ca">


# **The bias-variance tradeoff:**

There is a fundamental tradeoff between bias and variance in machine learning.
Simpler models tend to have higher bias and lower variance, while more complex models have lower bias but higher variance.
The goal in machine learning is to find the right balance between bias and variance to achieve good generalization performance.
This is typically done by tuning the model complexity, regularization techniques, and the amount of training data.
Underfitting (high bias) and overfitting (high variance) are both undesirable, and the aim is to find the sweet spot that minimizes the overall error. Techniques to address bias and variance will be discussed in following Deeper details:
