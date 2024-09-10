# LSTM (Long-Short-Term-Memory)

Long Short-Term Memory (LSTM), a type of recurrent neural network (RNN) designed to address the exploding and vanishing gradient problem that arises with traditional RNNs as mentioned befrre. These issues occur when the feedback loop weights are either too large (causing gradients to explode) or too small (causing them to vanish), making training difficult. LSTM overcomes this by using two separate memory pathways: long-term memory and short-term memory, instead of a single feedback loop.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/7460adbf-5190-4d32-b3a2-f1e87cba8511">

<sup>Image from ResearchGate</sup>

LSTMs work by passing inputs through multiple stages. First, the forget gate determines how much of the long-term memory to retain, using a sigmoid activation function. The next step is the input gate, which decides how much of the new input to store in long-term memory, using a tan-h activation function. Lastly, the output gate updates the short-term memory, determining how much of the long-term memory is passed forward.

**Summary of Functions**
- **Tanh:**
    - Used for normalizing cell states and candidate values.
    - Outputs between -1 and 1, aiding in stable learning and gradient flow.
- **Sigmoid:**
    - Used in gates to control the flow of information.
    - Outputs between 0 and 1, allowing for selective retention or discarding of information.

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

# Problems:

## 1. Complexity and Computational Cost
High Resource Demand: LSTMs require significant computational resources due to their complex architecture, making them slower to train compared to simpler models.
Long Training Time: The multiple gates and memory cells can lead to longer training cycles, especially with large datasets.

## 2. Exploding and Vanishing Gradients
Still a Concern: Although LSTMs mitigate these issues compared to vanilla RNNs, they are not entirely immune. In very deep networks or with very long sequences, gradients can still explode or vanish.

## 3. Limited Memory Capacity
Fixed Memory Size: The memory capacity of LSTMs is fixed, which can limit their performance on tasks requiring long-term dependencies beyond the model’s memory.
Inability to Retain Information Indefinitely: Important information can still be lost over extended sequences.

## 4. Alternative Architectures
Emergence of Better Models: The rise of models like Transformers has led to a preference for architectures that can handle long-range dependencies more effectively without recurrent connections.
Task-Specific Limitations: Some tasks work better with attention mechanisms rather than sequential processing.

## Learn about the final stage(transformers [here](https://github.com/623637719/The-Democratization-of-AI/tree/main/2.Deep%20learning/Transformers))
