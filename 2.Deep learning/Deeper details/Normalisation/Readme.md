# Benefits of normalisation:
1. Accelerate Training: Normalization helps to speed up the training process by ensuring that the inputs to each layer have a similar range of values. This can help the optimization algorithms, such as gradient descent, converge more quickly.
2. Improve Numerical Stability: Without normalization, the values in the network can become too large or too small, leading to numerical instability and potentially causing the training process to diverge or produce unreliable results.
3. Reduce Overfitting: Normalization can help reduce overfitting by making the network less sensitive to the scale of the inputs, allowing it to focus on learning more meaningful features.
There are several types of normalization techniques used in neural networks:

Batch Normalization: This technique normalizes the inputs to a layer by subtracting the mean and dividing by the standard deviation of the current batch of data. This helps to reduce the internal covariate shift, which is a change in the distribution of the inputs to a layer during training.
Layer Normalization: Instead of normalizing across the batch dimension, layer normalization normalizes the inputs to a layer across the feature dimension. This can be more effective than batch normalization in certain situations, such as when the batch size is small or when the network has recurrent connections.
Instance Normalization: This technique normalizes the inputs to a layer for each individual sample, rather than across the batch or feature dimensions. It is particularly useful for tasks like image style transfer, where the scale of the input features can vary significantly.
Group Normalization: This is a generalization of layer normalization, where the features are divided into groups before normalization is applied. This can provide a balance between the benefits of batch and layer normalization.
Weight Normalization: Instead of normalizing the inputs to a layer, weight normalization normalizes the weights of the layer. This can help improve the conditioning of the optimization problem and speed up the training process.
