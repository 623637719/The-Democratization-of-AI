# Early stopping
Early stopping is a technique used in training neural networks to prevent overfitting. Overfitting occurs when a model performs very well on the training data but fails to generalize well to new, unseen data. This happens because the model has memorized the training data instead of learning the underlying patterns, high variance.

The idea behind early stopping is to monitor the model's performance on a validation set (a separate dataset from the training data) during the training process. As the model trains, its performance on the training set will generally improve, but its performance on the validation set may eventually start to deteriorate, even as the training set performance continues to improve. This is a sign that the model is starting to overfit.

### The early stopping technique works as follows:

1. Split the available data into three sets not into two sets before: a training set, a validation set, and a test set.
2. Train the model on the training set, monitoring its performance on the validation set.
3. Keep track of the model's performance on the validation set during training, typically by measuring a metric like validation loss or validation accuracy.
4. Stop the training process when the model's performance on the validation set starts to degrade, even if the training set performance continues to improve.
5. The final model is the one with the best performance on the validation set, not necessarily the one at the end of the training process.
6. By stopping the training process before the model starts to overfit, early stopping helps to prevent overfitting and improves the model's generalization performance. It is a simple yet effective technique that is widely used in deep learning and other machine learning algorithms.

<img width="500" alt="image" src="https://github.com/user-attachments/assets/31da06a1-6dab-4004-86c2-e0f0c73ac833">
