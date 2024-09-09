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

Next lets look into LSTM or Long short term memory.
