> If you are familiarised with the basics of deep learning
> you can check out some [advanced optimization techniques](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Deeper%20details) or the rabbit hole of [transformers](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/RNN)
> [The Surprisingly Long History of Machine Learning](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/History%20of%20Machine%20Learning)
> [Vectorization]()

## What is Deep Learning?
Deep learning is a subset of machine learning that uses neural networks, which mimics how neurones in the brain work, with many layers (hence "deep") to model and understand complex patterns in data. These models require large amounts of data and significant computational power, often utilizing GPUs and TPUs for training due to the stupendous amount of calculating that has to go through it.

## What is a Neural Network?
A neural network is a type of machine learning model inspired by the structure and function of the human brain. It is composed of interconnected nodes, called artificial neurons, that work together to process and learn from data.

## Anatomy of a Neuron
A biological neuron consists of:

- Dendrites: The octopus-like structures that receive signals from other neurons.
- Axon: The branching structure that transmits signals to other neurons.

An artificial neuron has similar components:

- Inputs: The values received from the previous layer or the initial input.
- Weights: The strength of the connection between neurons, which determines the influence of each input.
- Bias: A constant value added to the weighted sum of the inputs to shift the activation of the neuron.
- Activation Function: A non-linear function that introduces non-linearity into the network, allowing it to learn complex patterns.

## A brief summary of how a Deep Learning Model works:

Forward propagation is responsible for making predictions and/or testing the model, while backward propagation adjusts the model based on errors to optimize its accuracy. This cyclical process of prediction and adjustment continues until the model achieves satisfactory performance.

## Forward Propagation
<sup>Taken from GeeksForGeeks</sup>

<img src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/ad04c250-afde-4ca2-a38d-876ea2d3b314" width="400" height="250">

<sup>The lines are all represent different weights and each neuron in the hidden layer has a bias, so the output of each neuron is m1x1 + m2x2 ...... + b </sup>

<sup>Where the x is the ouput of a neuron on the layer before it (or the input) and m is the weight that it holds, b is the bias.</sup>

Input Layer: The model receives input data.

Hidden Layers: The data is passed through multiple hidden layers. Each layer applies a set of weights and biases, followed by an activation function, to transform the input data.

- Weights and Biases: These are parameters that get adjusted to tinker with the output of the model.

- Activation Function: Functions like ReLU, sigmoid, or tanh introduce non-linearity, enabling the model to learn complex patterns.

Output Layer: The final transformed data produces a prediction or classification result.
## Backward Propagation
Loss Calculation: The model's prediction is compared to the actual target value using a loss function to calculate the error.

Gradient Calculation: The error is propagated backward through the network. Gradients of the loss function with respect to each weight and bias are computed.


Parameter Update: Using algorithms like gradient descent, the model updates its weights and biases to minimize the loss. This step is repeatedly performed over many iterations (epochs) to improve the model's performance.

**You can play with a neuro network in your browser [here](https://playground.tensorflow.org/#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.72826&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false)**

**Here is an [Video](https://www.youtube.com/watch?v=tnWvId25S6A) Explaination of this Website:**

### [Forward Propagation in Depth](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Forward%20Propagation)
### [Backward Propagation in Depth](https://github.com/623637719/The-Democratization-of-AI/blob/main/2.Deep%20learning/Backward%20Propagation/Readme.md)


