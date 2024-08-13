Gradient descent with momentum is an optimization algorithm used to speed up the convergence of the standard gradient descent method. It helps navigate the loss surface more effectively by incorporating a memory of past gradients.

### Standard Gradient Descent

In standard gradient descent, we update the parameters **theta** using the formula:

**theta** = **theta** - learning_rate * J(**theta**)

where:
- J(**theta**) is the gradient of the cost function **J** with respect to the parameters.

### Momentum

Momentum introduces an additional term to the update rule, which helps smooth out the updates and can lead to faster convergence. The key idea is to accumulate an exponentially decaying moving average of past gradients and use this information to update the parameters.

#### Momentum Update Rule

1. **Initialize Velocity**: Start with an initial velocity **V** (usually set to zero at start).

2. **Update Velocity**:

   v = momentum_parameter * **v** + (1 - momentum_parameter) * J(**theta**)
   
   - momentum_parameter is typically between 0.8 and 0.99.
   - **v** accumulates the gradients exponentially.

4. **Update Parameters**:

   **theta** = **theta** - learning_rate * v

### Intuition

- **Smoothing**: By considering the past gradients, momentum helps smooth the trajectory of the parameter updates. This can prevent oscillations, especially in ravines or regions where the surface curves more steeply in one dimension than another.
  
- **Acceleration**: In directions where the gradient consistently points, the velocity builds up, allowing faster movement across flat regions.

### Visualizing Momentum

Imagine a ball rolling down a hill. Standard gradient descent is like a ball on a rough surface, stopping frequently. Momentum is like adding weight to the ball, helping it roll smoother and faster down the hill.

### Conclusion

Gradient descent with momentum is a powerful optimization technique that enhances the basic gradient descent by using past gradients to smooth and accelerate the path to the minimum. By tuning the momentum parameter, you can significantly improve the performance of your learning algorithm.

![image](https://github.com/user-attachments/assets/c583f2f1-5789-4d72-94eb-43ece17e1632)

![image](https://github.com/user-attachments/assets/8dddba64-c03e-43b8-9819-cc56db9d3fdf)


