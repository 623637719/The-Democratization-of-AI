# LSTM (Long-Short-Term-Memory)

Long Short-Term Memory (LSTM), a type of recurrent neural network (RNN) designed to address the exploding and vanishing gradient problem that arises with traditional RNNs as mentioned befrre. These issues occur when the feedback loop weights are either too large (causing gradients to explode) or too small (causing them to vanish), making training difficult. LSTM overcomes this by using two separate memory pathways: long-term memory and short-term memory, instead of a single feedback loop.

![image](https://github.com/user-attachments/assets/a9fbd31f-4c3d-4677-99ad-0966f02842db)
<sup>Image from ResearchGate</sup>

LSTMs work by passing inputs through multiple stages. First, the forget gate determines how much of the long-term memory to retain, using a sigmoid activation function. The next step is the input gate, which decides how much of the new input to store in long-term memory, using a tan-h activation function. Lastly, the output gate updates the short-term memory, determining how much of the long-term memory is passed forward.
