import numpy as np
import matplotlib.pyplot as plt

# Hyperparameters
input_size = 2  # Number of input neurons
hidden_size = 2  # Number of hidden neurons
output_size = 1  # Number of output neurons
learning_rate = 0.03

# Example usage with dummy data
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_true = np.array([[0], [1], [1], [0]])

# Weights and biases initialization
np.random.seed(0)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.random.randn(1, hidden_size)
W2 = np.random.randn(hidden_size, output_size)
b2 = np.random.randn(1, output_size)


def ReLU(x):
    return np.maximum(x, 0)


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def ReLU_derivative(x):
    return np.where(x > 0, 1, 0)


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def forwardpropagation(X):
    global z1, a1, z2, a2
    z1 = np.dot(X, W1) + b1
    a1 = ReLU(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = sigmoid(z2)
    return a2


def compute_loss(y_true, y_pred):
    epsilon = 1e-15  # small value to prevent log(0)
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # clip to prevent log(0) or log(1 - 0)
    return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))


def backpropagation(X, y_true):
    global W1, b1, W2, b2

    # Forward propagation
    y_pred = forwardpropagation(X)

    # Compute loss
    loss = compute_loss(y_true, y_pred)

    # Backward propagation
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


def train(X, y_true, epochs):
    global W1, b1, W2, b2, learning_rate

    losses = []  # List to store losses over epochs

    for epoch in range(epochs):
        # Perform backpropagation and update weights and biases
        dW1, dW2, db1, db2, loss = backpropagation(X, y_true)

        W1 -= learning_rate * dW1
        W2 -= learning_rate * dW2
        b1 -= learning_rate * db1
        b2 -= learning_rate * db2

        losses.append(loss)

        # Print loss every 1000 epochs
        if (epoch + 1) % 1000 == 0:
            print(f'Epoch {epoch + 1}, Loss: {loss:.4f}')

    # Plot loss vs epoch
    plt.figure()
    plt.plot(range(1, epochs + 1), losses)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss vs Epoch')
    plt.grid(True)
    plt.show()


train(X, y_true, epochs=1000000)

while True:
    input_a = int(input("Enter first input: "))
    input_b = int(input("Enter second input: "))

    print(forwardpropagation(np.array([[input_a, input_b]])))
