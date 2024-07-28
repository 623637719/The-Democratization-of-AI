### Implementing Backpropagation of the simple method (You can find [full code](https://github.com/623637719/The-Democratization-of-AI/blob/main/2.Deep%20learning/Backward%20Propagation/NN.py) in this folder) 

        import numpy

Importing libraries to make calculations easier.

        # Hyperparameters
        input_size = 2    # Number of input neurons
        hidden_size = 2   # Number of hidden neurons
        output_size = 1   # Number of output neurons
        learning_rate = 0.01
        epsilon = 0.00001    # Small value for numerical gradient estimation

<img width="880" alt="image" src="https://github.com/user-attachments/assets/1e68b018-477e-4851-a90e-021b3707d821">


We are initialising a Neuro Network with two input neurons, 1 hidden layer of two neurons, and 1 output neuron.
We are going to train the NN to recognise XOR logic gate:

| Input A     | Input B     | Output   |
| ----------- | ----------- | -------- |
| 0           | 0           | 0        |
| 1           | 0           | 1        |
| 0           | 1           | 1        |
| 1           | 1           | 0        |
        
        # Example usage with dummy data
        X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y_true = np.array([[0], [1], [1], [0]])

In code form

        # Weights and biases initialization
        W1 = np.random.randn(input_size, hidden_size) # For the weights from the input layer to the hidden layer
        b1 = np.random.randn(1, hidden_size) # For the biases from the input layer to the hidden layer
        W2 = np.random.randn(hidden_size, output_size) # For the weights from the hidden layer to the output layer
        b2 = np.random.randn(1, output_size) # For the biases from the hidden layer to the output layer
        
np.random.randn give random numbers to initialise the weights and biases to random numbers between 0 and 1

        def ReLU(x):
                return np.maximum(x,0)

        def sigmoid(x):
            return 1 / (1 + np.exp(-x))
            
ReLU and Sigmoid function in code form
        
        def forwardpropagation(X):
            z1 = np.dot(X, W1) + b1
            a1 = ReLU(z1)
            z2 = np.dot(a1, W2) + b2
            a2 = sigmoid(z2)
            return a2  # Returning final output a2

Example of foward propagation, Sigmoid suits the output layer while ReLU suits input and hidden layers

        def compute_loss(y_true, y_pred):
            epsilon = 1e-15  # small value to prevent log(0)
            y_pred = np.clip(y_pred, epsilon, 1 - epsilon)  # clip to prevent log(0) or log(1 - 0)
            return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

This computes the loss between the computed and true y by using Binary Cross-Entropy Loss

        def backpropagation(X, y_true):
            global W1, b1, W2, b2, epsilon

            # Initialize gradients
            grad_W1 = np.zeros_like(W1)
            grad_W2 = np.zeros_like(W2)
            grad_b1 = np.zeros_like(b1)
            grad_b2 = np.zeros_like(b2)

Setting up the the backpropagation

            # Compute loss for current parameters
            y_pred = forwardpropagation(X)
            loss = compute_loss(y_true, y_pred)

Using the functions set up beforehand to calculate the y computed and the loss between the true y and ours

            # Gradient for W1
            for i in range(W1.shape[0]): #Loops through all the weights
                for j in range(W1.shape[1]):
                    W1[i, j] += epsilon # it adds the nudge
                    y_pred = forwardpropagation(X) # It finds the new computed y
                    loss_new = compute_loss(y_true, y_pred) # finds the new loss
                    grad_W1[i, j] = (loss - loss_new) / epsilon # finds the gradient
                    W1[i, j] -= epsilon # reverts the nudge back
        
            # Gradient for W2
            for i in range(W2.shape[0]):
                for j in range(W2.shape[1]):
                    W2[i, j] += epsilon
                    y_pred = forwardpropagation(X)
                    loss_new = compute_loss(y_true, y_pred)
                    grad_W2[i, j] = (loss - loss_new) / epsilon
                    W2[i, j] -= epsilon
        
            # Gradient for b1
            for i in range(b1.shape[1]):
                b1[0, i] += epsilon
                y_pred = forwardpropagation(X)
                loss_new = compute_loss(y_true, y_pred)
                grad_b1[0, i] = (loss - loss_new) / epsilon
                b1[0, i] -= epsilon
        
            # Gradient for b2
            for i in range(b2.shape[1]):
                b2[0, i] += epsilon
                y_pred = forwardpropagation(X)
                loss_new = compute_loss(y_true, y_pred)
                grad_b2[0, i] = (loss - loss_new) / epsilon
                b2[0, i] -= epsilon
        
            return grad_W1, grad_W2, grad_b1, grad_b2

Finds the gradient of each hyperparameter and the loss by calculating how much the nudge on the hyperparameter causes the loss to change.

        def train(X, y_true, epochs):
            global W1, b1, W2, b2
        
            for epoch in range(epochs):
                # Perform backpropagation and update weights and biases
                grad_W1, grad_W2, grad_b1, grad_b2 = backpropagation(X, y_true)
        
                W1 += learning_rate * grad_W1
                W2 += learning_rate * grad_W2
                b1 += learning_rate * grad_b1
                b2 += learning_rate * grad_b2
        
                # Compute and print loss every 100 epochs
                if (epoch+1) % 100 == 0:
                    y_pred = forwardpropagation(X)
                    loss = compute_loss(y_true, y_pred)
                    print(f'Epoch {epoch+1}, Loss: {loss:.4f}')
                    
<img width="680" alt="image" src="https://github.com/user-attachments/assets/96076b52-3fcb-42cf-8fa5-4e79e72c06e6">

The main training function, epochs is the amount of training that is going to happen. Using the backpropagation function it finds the gradients and then changes the hyperparameters using it. The learning rate controls how fast the model learns(faster does not mean better).

        train(X, y_true, epochs=1000)

Trains the network by calling the X and the true y and training 1000 times(epochs).

        while True:
            try:
                i_a = float(input("Input a: "))
                i_b = float(input("Input b: "))
        
                # Normalize input for prediction
                input_data = np.array([[i_a, i_b]])
                prediction = forwardpropagation(input_data)[0, 0]
                print(f"Prediction: {prediction:.4f}")
        
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
For the user to test the model

Sample result for training it 100 thousand times

<img width="218" alt="image" src="https://github.com/user-attachments/assets/1be45cc4-bacd-4669-98c6-f00b08a94e85">

<img width="637" alt="image" src="https://github.com/user-attachments/assets/b9cc049b-805b-41db-aec0-ff44814529b7">
