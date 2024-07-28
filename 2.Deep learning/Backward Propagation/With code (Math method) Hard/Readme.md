# [Full code](https://github.com/623637719/The-Democratization-of-AI/blob/main/2.Deep%20learning/Backward%20Propagation/NN%20math%20method.py)

Everything is the same with the simplier method except the backpropagation function and a new ReLU_derivative and Sigmoid_derivative function:

    def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

    def ReLU_derivative(x):
    return np.where(x > 0, 1, 0)

    def backpropagation(X, y_true):
        global W1, b1, W2, b2
    
        # Forward propagation
        y_pred = forwardpropagation(X)
    
        # Compute loss
        loss = compute_loss(y_true, y_pred)

        # Finds the dimensions of X
        m = X.shape[0]
    
        # Output layer gradients
        dz2 = y_pred - y_true
        dW2 = np.dot(a1.T, dz2) / m
        db2 = np.sum(dz2, axis=0, keepdims=True) / m
    
        # Hidden layer gradients
        dz1 = np.dot(dz2, W2.T) * ReLU_derivative(z1)
        dW1 = np.dot(X.T, dz1) / m
        db1 = np.sum(dz1, axis=0, keepdims=True) / m
    
        return dW1, dW2, db1, db2, loss
        
The function backpropagation takes two arguments: X (the input data) and y_true (the true/target output). The function first performs a forward propagation through the network using the forwardpropagation function to compute the predicted output y_pred. It then computes the loss between the predicted output y_pred and the true output y_true using the compute_loss function. The number of examples in the input data X is stored in the variable m. The gradients for the output layer are computed as follows:
- dz2 represents the difference between the predicted output y_pred and the true output y_true.
- dW2 is the gradient of the loss with respect to the weights W2 of the output layer, computed as the dot product of the transposed activations of the hidden layer a1 and dz2, divided by the number of examples m.
- db2 is the gradient of the loss with respect to the biases b2 of the output layer, computed as the sum of dz2 along the axis of the examples, divided by m.
The gradients for the hidden layer are computed as follows:
- dz1 represents the backpropagated error signal from the output layer, computed by multiplying dz2 with the transposed W2 and then element-wise multiplying with the derivative of the ReLU activation function applied to the hidden layer activations z1.
- dW1 is the gradient of the loss with respect to the weights W1 of the hidden layer, computed as the dot product of the transposed input X and dz1, divided by m.
db1 is the gradient of the loss with respect to the biases b1 of the hidden layer, computed as the sum of dz1 along the axis of the examples, divided by m.
- Finally, the function returns the computed gradients dW1, dW2, db1, db2, and the loss value.
