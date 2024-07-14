# How a Neuron Calculates its Output or Forward propagation
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

### Visualisation: 
<img width="436" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/0f6c20d1-2471-4e19-b889-d4581be65cd3">


## Activation Functions
Activation functions introduce non-linearity into the network, allowing it to learn complex patterns. Some common activation functions are:

1. Step Function: Output is 0 if the input is below 0, and 1 if the input is 0 or above.
2. Sigmoid Function: Squashes the input between 0 and 1, producing a smooth S-shaped curve.
3. Rectified Linear Unit (ReLU): Output is 0 if the input is negative, and the input value if the input is positive.

Using an activation function is crucial for neural networks to learn non-linear relationships in the data.

## Deeper Networks
As the neural network becomes deeper, with more hidden layers, it can learn more complex patterns in the data. However, the computation required also increases, which can lead to performance issues. Techniques like forward and backpropagation are used to train these deeper networks effectively.
