# Recurrent Neural Networks

NOTE: This assumes that you are already familiar with the main ideas behind neural networks, backpropagation and the ReLU activation function.  Although vanilla recurrent neural networks are awesome, they are usually thought of as a stepping stone to understanding fancier things like Long Short-Term Memory Networks and Transformers, which you can read about next. In other words, this is the first step out of three to understand transformers. 

## Stock market problem

The problem with using a basic NN for stock market data is that the input is fixed, but the longer a company has been traded on the stock market, the more data there will be for it, it would be bad if we can't take advantage of more data. 

For example, 

<img width="1036" alt="image" src="https://github.com/user-attachments/assets/06c7f6b7-af54-4dd7-9f06-9a34b36a1bab">
<sup>Image from Statquest </sup>

This is a big difference compared to the other neural networks we've looked at in this series. For example, in Neural Networks Clearly Explained, we examined a neural network that made predictions using one input value, no more and no less. And if you saw the StatQuest on neural networks with multiple inputs and outputs, you saw this neural network that made predictions using two input values, no more and no less. And in the StatQuest on Deep Learning Image Classification, you saw a neural network that made a prediction using an image that was six pixels by six pixels, no bigger and no smaller. However, now we need a neural network that can make a prediction using the nine values we have for the blue company and make a prediction using the five values we have for the red company.

The good news is that one way to deal with the problem of having different amounts of input values is to use a Recurrent Neural Network. Just like the other neural networks that we've seen before, recurrent neural networks have weights, biases, layers and activation functions. The big difference is that recurrent neural networks also have feedback loops. And, although this neural network may look like it only takes a single input value, the feedback loop makes it possible to use sequential input values, like stock market prices collected over time, to make predictions.

To understand how, exactly, this recurrent neural network can make predictions with sequential input values, let's run some of StatLand's stock market data through it. In StatLand, if the price of a stock is low for two days in a row, then, more often than not, the price remains low on the next day. In other words, if yesterday and today’s stock price is low, then tomorrow's price should also be low. In contrast, if yesterday's price was low and today's price is medium, then tomorrow's price should be even higher. And when the price decreases from high to medium, then tomorrow's price will be even lower. Lastly, if the price stays high for two days in a row, then the price will be high tomorrow.

Now that we see the general trends in stock prices in StatLand, we can talk about how to run yesterday and today's data through a recurrent neural network to predict tomorrow's price. The first thing we'll do is scale the prices so that low equals 0, medium equals 0.5, and high equals 1. Now let's run the values for yesterday and today through this recurrent neural network and see if it can correctly predict tomorrow's value.

Now, because the recurrent neural network has a feedback loop, we can enter yesterday and today's values into the input sequentially. We'll start by plugging yesterday's value into the input. Now we can do the math just like we would for any other neural network. Beep. Boop. Beep. Boop. Boop. At this point, the output from the activation function, the y-axis coordinate that we will call Y sub 1, can go two places. First, Y sub 1 can go towards the output. And if we go that way and do the math beep, boop, boop, then the output is the predicted value for today. However, we're not interested in the predicted value for today because we already have the actual value for today. Instead, we want to use both yesterday and today's value to predict tomorrow's value.

So, for now, we'll ignore this output, and instead, focus on what happens with this feedback loop. The key to understanding how the feedback loop works is this summation. The summation allows us to add Y sub 1 times W sub 2, which is based on yesterday's value, to the value from today times W sub 1. In other words, the feedback loop allows both yesterday and today’s values to influence the prediction.

