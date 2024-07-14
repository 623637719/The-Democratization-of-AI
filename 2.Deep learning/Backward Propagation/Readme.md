# A Beginner's Guide to Backpropagation
Introduction to Backpropagation
Backpropagation is the core algorithm that powers the training of most modern neural networks. It is a supervised learning technique that allows neural networks to efficiently learn the parameters (weights and biases) that minimize the error between the network's predictions and the true target outputs.

The key insight behind backpropagation is that we can compute the gradient of the loss function with respect to each parameter in the network, and then use this gradient information to update the parameters in the direction that decreases the loss.

## How it works

### Forward Propagation: 
The input data is fed through the neural network layers, producing an output prediction as discussed before.
### Backward Propagation: 
Simpler View:

- Each hyperparameter(Weights and biases) is isolated and by nudging it slightly(increasing or decreasing by 0.0001) you can see the gradient of the hyperparameter with respect to the loss function(measures the difference between computed y and true y).

More in depth view:

- The error between the prediction and the true target output is computed, and this error is then propagated backwards through the network, computing the gradients of the loss with respect to each parameter.

- The core idea is to use the chain rule from calculus to efficiently compute these gradients. By knowing the gradients, we can then update the network parameters in the direction that decreases the loss function.

### Implementing Backpropagation of the simpler view
        import numpy

        # Hyperparameters
        input_size = 2    # Number of input neurons
        hidden_size = 2   # Number of hidden neurons
        output_size = 1   # Number of output neurons
        learning_rate = 0.01
        epsilon = 0.00001    # Small value for numerical gradient estimation
We are initialising a Neuro Network with two input neurons, 1 hidden layer of two neurons, and 1 output neuron.
We are going to train the NN to recognise XOR logic gate:
| Input A     | Input B     | Output   |
| ----------- | ----------- | -------- |
| Header      | Title       | Title    |
| Paragraph   | Text        | Text     |
    
This code implements a simple two-layer neural network and demonstrates the backpropagation algorithm to train the network's parameters. The forward_prop function computes the outputs of the network, the backward_prop function computes the gradients, and the gradient_descent function updates the weights and biases using these gradients.
