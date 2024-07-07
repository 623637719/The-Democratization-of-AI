# Neural Networks: A Beginner's Guide
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

## How a Neuron Calculates its Output
The output of a neuron is calculated as follows:

1. Multiply each input by its corresponding weight.
2. Add the biases to the weighted sum of the inputs.
3. Apply the activation function to the result.
4. This can be represented mathematically as:

$y = activation_function(sum(x * w) + b)$

where:

y is the output of the neuron
x are the inputs
w are the weights
b is the bias
activation_function() is the non-linear activation function
## Building a Simple Neural Network
Let's build a simple neural network to predict how much a normal person would like a person based on their age and appearance:

age = int(input("Age:\n"))
looks = int(input("Looks:\n"))

weight_age = -10
weight_looks = 1
bias = 25

output = weight_age * age + weight_looks * looks + bias

print(output)
In this example:

The weight for age is set to -10, meaning the older the person, the less James Charles would like them.
The weight for looks is set to 1, meaning the more attractive the person, the more James Charles would like them.
The bias is set to 25, which shifts the output to a more reasonable range.
Activation Functions
Activation functions introduce non-linearity into the network, allowing it to learn complex patterns. Some common activation functions are:

Step Function: Output is 0 if the input is below 0, and 1 if the input is 0 or above.
Sigmoid Function: Squashes the input between 0 and 1, producing a smooth S-shaped curve.
Rectified Linear Unit (ReLU): Output is 0 if the input is negative, and the input value if the input is positive.
Using an activation function is crucial for neural networks to learn non-linear relationships in the data.

Deeper Networks
As the neural network becomes deeper, with more hidden layers, it can learn more complex patterns in the data. However, the computation required also increases, which can lead to performance issues. Techniques like forward and backpropagation are used to train these deeper networks effectively.
