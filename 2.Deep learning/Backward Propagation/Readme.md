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
    num_inputs = 2  # Number of input features
    num_hidden = 3  # Number of hidden neurons in the single hidden layer
    num_outputs = 1  # Number of output neurons

    # Initialize the weights randomly
    W1 = np.random.randn(num_hidden, num_inputs)  # Weights for the input to hidden layer
    b1 = np.random.randn(num_hidden, 1)  # Bias for the hidden layer
    W2 = np.random.randn(num_outputs, num_hidden)  # Weights for the hidden to output layer
    b2 = np.random.randn(num_outputs, 1)  # Bias for the output layer


    # Define the activation function (sigmoid)
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))  # Sigmoid activation function


    # Forward propagation
    def forward_prop(X):
        z1 = np.dot(W1, X.T) + b1  # Linear transformation for hidden layer
        a1 = sigmoid(z1)  # Activation for hidden layer
        z2 = np.dot(W2, a1) + b2  # Linear transformation for output layer
        a2 = sigmoid(z2)  # Activation for output layer
        return a1, a2  # Return activations for both layers


    # Loss function (mean squared error)
    def compute_loss(y, a2):
        m = y.shape[0]  # Number of training examples
        loss = (1 / m) * np.sum((a2 - y.T) ** 2)  # Mean squared error
        return loss  # Return the computed loss


    # Backward propagation
    def backward_prop(X, y, a1, a2):
        m = X.shape[0]  # Number of training examples

        # Compute gradients
        dz2 = a2 - y.T  # Gradient of loss with respect to z2
        dW2 = (1 / m) * np.dot(dz2, a1.T)  # Gradient of loss with respect to W2
        db2 = (1 / m) * np.sum(dz2, axis=1, keepdims=True)  # Gradient of loss with respect to b2

        da1 = np.dot(W2.T, dz2)  # Gradient of loss with respect to a1
        dz1 = da1 * a1 * (1 - a1)  # Gradient of loss with respect to z1 (using the derivative of sigmoid)
        dW1 = (1 / m) * np.dot(dz1, X)  # Gradient of loss with respect to W1
        db1 = (1 / m) * np.sum(dz1, axis=1, keepdims=True)  # Gradient of loss with respect to b1

        return dW1, db1, dW2, db2  # Return all gradients


    # Gradient descent update
    def gradient_descent(X, y, num_iters, alpha):
        global W1, b1, W2, b2  # Use global variables to update weights and biases
        for i in range(num_iters):
            a1, a2 = forward_prop(X)  # Perform forward propagation
            dW1, db1, dW2, db2 = backward_prop(X, y, a1, a2)  # Perform backward propagation

            # Update parameters
            W1 -= alpha * dW1  # Update W1
            b1 -= alpha * db1  # Update b1
            W2 -= alpha * dW2  # Update W2
            b2 -= alpha * db2  # Update b2
    
            # Print the loss every 1000 iterations
            if i % 1000 == 0:
                loss = compute_loss(y, a2)  # Compute the loss
                print(f"Iteration {i}, loss: {loss}")  # Print the current iteration and loss
    
        return W1, b1, W2, b2  # Return the final weights and biases
    
    
    # Example usage
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # Input data
    y = np.array([[0], [1], [1], [0]])  # Expected output (XOR function)
    
    W1, b1, W2, b2 = gradient_descent(X, y, num_iters=10000, alpha=0.1)  # Train the neural network
    
    # Make predictions
    _, a2 = forward_prop(X)  # Perform forward propagation with the trained weights
    predictions = a2.T  # Transpose the predictions to match the input shape
    print("Predictions after training:")  # Print the predictions
    print(predictions)  # Display the predictions
    
This code implements a simple two-layer neural network and demonstrates the backpropagation algorithm to train the network's parameters. The forward_prop function computes the outputs of the network, the backward_prop function computes the gradients, and the gradient_descent function updates the weights and biases using these gradients.
