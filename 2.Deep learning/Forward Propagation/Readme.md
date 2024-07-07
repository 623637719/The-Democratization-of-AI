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

       y = activation_function(sum(x * w) + b)

where:

y is the output of the neuron
x are the inputs
w are the weights
b is the bias
activation_function() is the non-linear activation function
## Building a Simple Neural Network
Let's build a simple neural network to predict how much a random person would like a person based on their age and appearance:

       age = int(input("Age:\n"))
       looks = int(input("Looks:\n"))

       weight_age = -5
       weight_looks = 1
       bias = 25

       output = weight_age * age + weight_looks * looks + bias

       output_with_activation_function = max(0,output) # Appling ReLu activation function

       print(output_with_activation_function)
       
In this example:

The weight for age is set to -5, meaning the older the person, the less the person would like them.
The weight for looks is set to 1, meaning the more attractive the person, the more the person would like them.
The bias is set to 125, which shifts the output to a more reasonable range.

Visualisation: 
<img width="922" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/622e53eb-6963-4bd9-ba8f-02c378fddb9a" width="500">


## Activation Functions
Activation functions introduce non-linearity into the network, allowing it to learn complex patterns. Some common activation functions are:

1. Step Function: Output is 0 if the input is below 0, and 1 if the input is 0 or above.
2. Sigmoid Function: Squashes the input between 0 and 1, producing a smooth S-shaped curve.
3. Rectified Linear Unit (ReLU): Output is 0 if the input is negative, and the input value if the input is positive.

Using an activation function is crucial for neural networks to learn non-linear relationships in the data.

## Deeper Networks
As the neural network becomes deeper, with more hidden layers, it can learn more complex patterns in the data. However, the computation required also increases, which can lead to performance issues. Techniques like forward and backpropagation are used to train these deeper networks effectively.
