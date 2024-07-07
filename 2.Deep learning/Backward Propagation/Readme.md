# A Beginner's Guide to Backpropagation
Introduction to Backpropagation
Backpropagation is the core algorithm that powers the training of most modern neural networks. It is a supervised learning technique that allows neural networks to efficiently learn the parameters (weights and biases) that minimize the error between the network's predictions and the true target outputs.

The key insight behind backpropagation is that we can compute the gradient of the loss function with respect to each parameter in the network, and then use this gradient information to update the parameters in the direction that decreases the loss.

## How it works

### Forward Propagation: 
The input data is fed through the neural network layers, producing an output prediction as discussed before.
### Backward Propagation: 
The error between the prediction and the true target output is computed, and this error is then propagated backwards through the network, computing the gradients of the loss with respect to each parameter.

The core idea is to use the chain rule from calculus to efficiently compute these gradients. By knowing the gradients, we can then update the network parameters in the direction that decreases the loss function.

### Implementing Backpropagation

    import numpy as np

    # Define the neural network structure
    num_inputs = 2
    num_hidden = 3
    num_outputs = 1

    # Initialize the weights randomly
    W1 = np.random.randn(num_hidden, num_inputs)
    b1 = np.random.randn(num_hidden, 1)
    W2 = np.random.randn(num_outputs, num_hidden)
    b2 = np.random.randn(num_outputs, 1)

    # Define the activation function (sigmoid)
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    # Forward propagation
    def forward_prop(X):
        z1 = np.dot(W1, X) + b1
        a1 = sigmoid(z1)
        z2 = np.dot(W2, a1) + b2
        a2 = sigmoid(z2)
        return a1, a2

    # Backward propagation
    def backward_prop(X, y, a1, a2):
        m = X.shape[1]
    
        # Compute gradients
        dz2 = a2 - y
        dW2 = (1/m) * np.dot(dz2, a1.T)
        db2 = (1/m) * np.sum(dz2, axis=1, keepdims=True)
    
        da1 = np.dot(W2.T, dz2)
        dz1 = da1 * a1 * (1 - a1)
        dW1 = (1/m) * np.dot(dz1, X.T)
        db1 = (1/m) * np.sum(dz1, axis=1, keepdims=True)
    
        return dW1, db1, dW2, db2

    # Gradient descent update
    def gradient_descent(X, y, num_iters, alpha):
        for i in range(num_iters):
            a1, a2 = forward_prop(X)
            dW1, db1, dW2, db2 = backward_prop(X, y, a1, a2)
        
            # Update parameters
            W1 -= alpha * dW1
            b1 -= alpha * db1
            W2 -= alpha * dW2
            b2 -= alpha * db2
    
        return W1, b1, W2, b2

    # Example usage
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    W1, b1, W2, b2 = gradient_descent(X, y, num_iters=10000, alpha=0.1)
    
This code implements a simple two-layer neural network and demonstrates the backpropagation algorithm to train the network's parameters. The forward_prop function computes the outputs of the network, the backward_prop function computes the gradients, and the gradient_descent function updates the weights and biases using these gradients.
