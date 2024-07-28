# A Beginner's Guide to Backpropagation (No Code)
Introduction to Backpropagation
Backpropagation is the core algorithm that powers the training of most modern neural networks. It is a supervised learning technique that allows neural networks to efficiently learn the parameters (weights and biases) that minimize the error between the network's predictions and the true target outputs.

The key insight behind backpropagation is that we can compute the gradient of the loss function with respect to each parameter in the network, and then use this gradient information to update the parameters in the direction that decreases the loss.

## How it works

### Short summary: Forward Propagation: 
The input data is fed through the neural network layers, producing an output prediction as discussed before.

### Short summary: Backward Propagation: 
Simple method (numerical):

- Each hyperparameter(Weights and biases) is isolated and by nudging it slightly(increasing or decreasing by 0.0001) you can see the gradient of the hyperparameter with respect to the loss function(measures the difference between computed y and true y).

Math based method (Chain rule):

- The error between the prediction and the true target output is computed, and this error is then propagated backwards through the network, computing the gradients of the loss with respect to each parameter.

- The core idea is to use the chain rule from calculus to efficiently compute these gradients. By knowing the gradients, we can then update the network parameters in the direction that decreases the loss function.

### Simple method（Numerical）([with code example](https://github.com/623637719/The-Democratization-of-AI/blob/main/2.Deep%20learning/Backward%20Propagation/with%20code/Readme.md)) 

We are initialising a Neuro Network with two input neurons, 1 hidden layer of two neurons, and 1 output neuron.
We are going to train the NN to recognise XOR logic gate:

| Input A     | Input B     | Output   |
| ----------- | ----------- | -------- |
| 0           | 0           | 0        |
| 1           | 0           | 1        |
| 0           | 1           | 1        |
| 1           | 1           | 0        |
        
Then we will give random numbers between 0 and 1 to initialise the weights and biases to random numbers. 

Finds the relationship of each hyperparameter and the loss by calculating how much the nudge on the hyperparameter causes the loss to change. Step by step:

1. Adds the small number to the hyperparameter
2. Forward propagates with the nudged hyperparameter
3. Finds the loss
4. Finds the negative gradient by calculating (loss_before - loss_new) / epsilon
5. Reverts the nudge back on the hyperparameter
6. Adds the gradient to the hyperparameter, causing it to go down in loss

<img width="773" alt="image" src="https://github.com/user-attachments/assets/b61bb0f4-cca5-4e1b-a615-f0e2afaf146c">

Sample result for training it 100 thousand times

<img width="218" alt="image" src="https://github.com/user-attachments/assets/1be45cc4-bacd-4669-98c6-f00b08a94e85">

<img width="637" alt="image" src="https://github.com/user-attachments/assets/b9cc049b-805b-41db-aec0-ff44814529b7">

### !!Hard!! Math based method（chain rule）example ([with code version]()) 

Difference between the this method and the simple one is that instead of nudging the hyperparameters again and doing a forward pass everytime to find the gradient, we can instead just get the gradient of each using calculus, specifically the chain rule:

The chain rule is a fundamental concept in calculus that allows us to differentiate a composite function, i.e., a function that is composed of other functions. It is particularly useful when computing gradients in machine learning and optimization problems.

Let's say we have a function f(x, y), where x and y are both functions of some independent variable t. We can express the derivative of f with respect to t using the chain rule as follows:

        d/dt f(x(t), y(t)) = (∂f/∂x) * (dx/dt) + (∂f/∂y) * (dy/dt)

The key idea is that the derivative of the composite function f(x(t), y(t)) with respect to t can be expressed as the sum of the products of the partial derivatives of f with respect to x and y, multiplied by the derivatives of x and y with respect to t, respectively.

In the context of the hyperparameter optimization problem, the chain rule allows us to break down the gradient computation as follows:

Compute the gradients of the output f with respect to the model parameters θ using backpropagation: ∇_θ f(x, θ, λ).
Compute the gradients of the output f with respect to the hyperparameters λ using the chain rule:

        ∇_λ f(x, θ, λ) = Σ (∇_θ f(x, θ, λ))_i * (∂θ_i / ∂λ)

Here, the partial derivatives ∂θ_i / ∂λ represent how the model parameters θ_i change with respect to the hyperparameters λ.
By using the chain rule, we can efficiently compute the gradients of the output with respect to the hyperparameters without the need for additional forward passes through the model. This can lead to significant computational savings and faster convergence during the hyperparameter optimization process.
