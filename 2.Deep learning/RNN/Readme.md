# Recurrent Neural Networks

NOTE: This assumes that you are already familiar with the main ideas behind neural networks, backpropagation and the ReLU activation function.  Although vanilla recurrent neural networks are awesome, they are usually thought of as a stepping stone to understanding fancier things like Long Short-Term Memory Networks and Transformers, which you can read about next. In other words, this is the first step out of three to understand transformers. 

## Stock market problem

The problem with using a basic NN for stock market data is that the input is fixed, but the longer a company has been traded on the stock market, the more data there will be for it, it would be bad if we can't take advantage of more data. 

For example, 

<img width="1036" alt="image" src="https://github.com/user-attachments/assets/06c7f6b7-af54-4dd7-9f06-9a34b36a1bab">
<sup>Image from Statquest </sup>

If you have exaimined the simple sample code for a NN you would have seen only 2 values as inputs, for the two boolean values. However, now we need a neural network that can make a prediction using the nine values we have for the blue company and make a prediction using the five values we have for the red company.

We can use Recurrent Neural Network to deal with this. Just like the other neural networks that we've seen before, recurrent neural networks have weights, biases, layers and activation functions. The big difference is that recurrent neural networks has a feedback loop. You can plug in sequential values for in the input such as stock market prices.

<img width="984" alt="image" src="https://github.com/user-attachments/assets/52f844b5-4b71-4e64-8521-67f044610c1d">

This is a simple RNN, to expand an RNN it is the same as NN but the output of the previous hidden state influences all neurons in the current hidden layer because it gets multiplied by the weight matrix, so each neuron in the current hidden layer receives a weighted sum of all the units from the previous hidden state.

## The Problem (Vanishing and Exploding Gradients)

As mentioned earlier, RNN is simply a stepping stone to understanding LSTM and finally Transformer models in humanities quest to develop a NN for sequential data. RNN faces a huge problem, the exploding and vanishing graident problem. Let's say we have 1000 days of stock market information for a RNN and the recurrent weight is 0.9, after 100 sequential values is passed through it, the effect of the first data value will be it times 0.99^(1000) which is 0.00004317, if the recurrent weight was 0.9 the result will be simply 0. That is the vanishing gradient problem. Oppositely, if the weight is 1.1 after 1000 days the effect of the first data value would be  1.1^(1000) or 2.4699329e+41 which is 2 followed by 41 zeros. That is the exploding graident problem.

To resolve this issue, people have created the [LSTM (Long Short Term Memory)](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/LSTM) model to mitigate this problem.
