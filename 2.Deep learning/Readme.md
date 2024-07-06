### [The Surprisingly Long History of Machine Learning](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/History%20of%20Machine%20Learning)

## What is Deep Learning?
Deep learning is a subset of machine learning that uses neural networks, which mimics how neurones in the brain work, with many layers (hence "deep") to model and understand complex patterns in data. These models require large amounts of data and significant computational power, often utilizing GPUs and TPUs for training due to the stupendous amount of calculating that has to go through it.

## A brief summary of how a Deep Learning Model works:

Forward propagation is responsible for making predictions and/or testing the model, while backward propagation adjusts the model based on errors to optimize its accuracy. This cyclical process of prediction and adjustment continues until the model achieves satisfactory performance.

### Forward Propagation
<img src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/ad04c250-afde-4ca2-a38d-876ea2d3b314" width="100" height="100">

Input Layer: The model receives input data.

Hidden Layers: The data is passed through multiple hidden layers. Each layer applies a set of weights and biases, followed by an activation function, to transform the input data.

- Weights and Biases: These are parameters that get adjusted to tinker with the output of the model.

- Activation Function: Functions like ReLU, sigmoid, or tanh introduce non-linearity, enabling the model to learn complex patterns.

Output Layer: The final transformed data produces a prediction or classification result.
### Backward Propagation
Loss Calculation: The model's prediction is compared to the actual target value using a loss function to calculate the error and therefore what to change.

Gradient Calculation: The error is propagated backward through the network. Gradients of the loss function with respect to each weight and bias are computed.

Parameter Update: Using algorithms like gradient descent, the model updates its weights and biases to minimize the loss. This step is repeatedly performed over many iterations (epochs) to improve the model's performance.


