# Topics:

## [Bias and Variance](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Bias%20and%20Variance)

Bias and variance are key concepts in understanding model performance. Bias refers to errors due to overly simplistic models that underfit the training data, while variance refers to errors from models that are too complex resulting to overfitting the training data. 

## [Regularisation](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Regularisation)

Overfitting occurs when a model fits the training data too closely, resulting in poor performance on new, unseen data. Regularization addresses this issue by adding a penalty that commensurates with size of hyperparameters, which encourages the model to learn simpler, more generalizable patterns.

## [Early stopping](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Early%20stopping)

Early stopping is a regularization technique used to prevent overfitting by halting training when a model's performance on a validation set starts to degrade.

## [Normalisation](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Normalisation)

Normalisation involves scaling input features to a standard range or distribution, improving convergence speed and stability during training.

## [Vanishing exploding gradients](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Vanishing%20and%20Exploding%20Gradient)

These issues occur during backpropagation in deep networks. Vanishing gradients make learning difficult as gradients shrink, while exploding gradients cause instability with large updates.

## [Mini Batch Gradient Descent](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Minibatch%20gradient%20descent)

Mini-batch gradient descent updates model parameters using small batches of data, balancing the efficiency of batch processing with the robustness of stochastic updates.

## [Gradient Descent with Momentum](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Gradient%20Descent%20with%20Momentum)

This optimizer accelerates gradient descent by considering past gradients, improving convergence speed and helping to avoid local minima.

## [RMSprop](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/RMSprop)

The key idea behind RMSprop is to divide the learning rate for a parameter by the root mean square (RMS) of recent gradients for that parameter. This helps to address the issue of rapidly changing gradients, which can cause the learning process to become unstable.

## [Adam](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Adam)

Adam is an optimizer that combines the benefits of momentum and RMSprop, adapting learning rates individually for parameters based on first and second moments of gradients, namely the mean of the gradients and uncentered variance of the gradients.

## [Learning rate decay](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Learning%20rate%20Decay)

Learning rate decay involves reducing the learning rate over time to improve convergence and prevent oscillating above a optimum.

## [Coarse to fine](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Coarse%20to%20fine)

This approach starts with a broad overview of the hyperparameters and progressively refines to find the best hyperparameters for the best model, improving efficiency and accuracy.

## [Caviar(parallel) vs Panda(babysitting)](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details/Caviar%20vs%20Panda)

This topic compares parallel processing strategies (Caviar) with more sequential, attentive approaches (Panda), discussing trade-offs in efficiency and control.
