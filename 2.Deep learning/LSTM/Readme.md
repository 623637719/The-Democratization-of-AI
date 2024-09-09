# LSTM (Long-Short-Term-Memory)

Long Short-Term Memory (LSTM), a type of recurrent neural network (RNN) designed to address the exploding and vanishing gradient problem that arises with traditional RNNs as mentioned befrre. These issues occur when the feedback loop weights are either too large (causing gradients to explode) or too small (causing them to vanish), making training difficult. LSTM overcomes this by using two separate memory pathways: long-term memory and short-term memory, instead of a single feedback loop.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/5cc40432-2fbc-4538-ad83-05792c037958">

<sup>Image from ResearchGate</sup>

LSTMs work by passing inputs through multiple stages. First, the forget gate determines how much of the long-term memory to retain, using a sigmoid activation function. The next step is the input gate, which decides how much of the new input to store in long-term memory, using a tan-h activation function. Lastly, the output gate updates the short-term memory, determining how much of the long-term memory is passed forward.

**Summary:**
- **Short-Term Memory:** Hidden State  h(t)
- **Long-Term Memory**: Cell State C(t)

**h(t-1)**
- **Definition:** This represents the hidden state of the LSTM at the previous time step (t-1)
- **Role:** It contains information from the previous time step that helps the LSTM make predictions at the current time step. The hidden state acts as a memory, capturing past information.

**h(t)**
- **Definition:** The hidden state at the current time step
- **Role:** This state is computed based on the previous hidden state and the current input. It serves as the output of the LSTM cell for the current time step and will be used in the next time step (t+1).

**x(t)**
- **Definition:** The input feature vector at the current time step 
- **Role:** It provides the LSTM with the current input data to process. Each input can represent various types of data, such as text, audio features, or time series data.

**c(t-1)**
- **Definition:** This represents the cell state of the LSTM at the last time step (t-1).
- **Role:** The cell state c(t) carries long-term information that is updated at each time step. It is influenced by the forget gate and input gate.

**c(t)**
- **Definition:** This represents the cell state of the LSTM at the current time step (t).

### Gates:
- Forget Gate: Takes h(t−1) and x(t) as inputs to decide what to forget from the previous cell state C(t−1).
- Input Gate: Accepts the current input and previous hidden state to determine what new information to add to the cell state.
- Output Gate: Computes the new hidden state h(t) based on the updated cell state. 

