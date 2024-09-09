
# Progression thus far

1. LSTMs and RNNs
- Recurrent Neural Networks (RNNs) were the first attempt to model sequences, relying on their internal state to capture information about previous inputs.
- LSTMs were developed to address RNNs' limitations, particularly the vanishing gradient problem. They use a gating mechanism to manage the flow of information, allowing them to retain information over longer sequences.
2. Limitations of LSTMs
- Sequential Processing: LSTMs process data sequentially, which can lead to longer training times and difficulties in parallelization (can't utilise GPUs).
- Long-distance Dependencies: Although LSTMs are better at handling long-range dependencies than vanilla RNNs, they still struggle with very long sequences.
3. Introduction of Transformers
- Attention Mechanism: Transformers introduced a self-attention mechanism that allows the model to weigh the importance of different words in a sequence, regardless of their position. This enables capturing relationships between distant elements more effectively.
- Parallelization: Unlike LSTMs, Transformers can process entire sequences simultaneously, significantly speeding up training times.

# Transformer:
The evolution to Transformer actually came from CNNs or Convolution Neuro Networks, used for image processing.

Here's a comprehensive step-by-step breakdown of how transformers evolved from CNNs:

### **1. The Rise of CNNs and their Application to NLP**
   - **CNNs were highly successful in image processing**: Convolutional Neural Networks (CNNs) revolutionized computer vision tasks like object detection, image classification, and more. They were ideal for processing images due to the local relationships between neighboring pixels.
   - **Attempt to apply CNNs to Natural Language Processing (NLP)**: With their success in vision tasks, researchers attempted to adapt CNNs for NLP tasks like translation, sentiment analysis, and text classification.

### **2. CNN Struggles with Textual Data**
   - **Difference between images and text**: CNNs worked well with images because adjacent pixels are usually related. But for text, **neural networks need numbers** as inputs, which leads to using **one-hot encoding** to convert words into vectors.
   - **One-hot encoding for text**: Words were transformed into unique vectors with a large number of dimensions (based on vocabulary size). However, CNNs still struggled with text even after this encoding because the relationship between words in a sentence differs from pixel relationships in images.

### **3. Why CNNs Fail at Long-Range Dependencies in Text**
   - **Locality in images vs. distant relations in text**: CNNs work by combining information from small neighboring chunks of data (e.g., pixels or words). While this works for images, where nearby pixels are related, text often requires modeling long-distance relationships (e.g., in the sentence "the dog caught its own tail", the words "dog" and "tail" are far apart but strongly related).
   - **CNNs confuse unrelated words**: CNNs struggle with text because they only combine local groups of word, leading to confusion when unrelated words are processed together.

### **4. The Key Idea of Transformers: Self-Attention**
   - **Replacing convolutional layers with self-attention**: To solve CNN's limitations, transformers introduced **self-attention** layers, which allow the model to consider **every pair of words** in a sentence, regardless of their distance.
   - **Pairwise relationships**: Instead of working with neighboring groups of words, the self-attention mechanism combines pairs of words, allowing even distant words to interact in the early layers, addressing the CNN's limitation.

### **5. Transformers Solve the Context Problem**
   - **Context-sensitive importance**: Unlike CNNs, transformers compute how important a word pair is by calculating a **score** for each word pair based on their context. This score (importance weight) determines how much influence one word should have on another.
   - **Self-attention operation**: In each self-attention layer, vectors (word representations) are computed by combining information from all word pairs, weighted by their relevance (importance).

### **6. Tackling the Problem of Order Sensitivity**
   - **Word order matters**: The model must understand that changing the order of words changes meaning ("the fat cat" vs. "the cat fat"). To preserve word order, transformers introduced **positional encodings**—additional information attached to each word vector indicating its position in the sentence.

### **7. Managing Model Complexity**
   - **Scaling problems with pairwise comparisons**: The self-attention mechanism computes pairwise relationships between words, but this leads to a large number of comparisons, especially for long sentences.
   - **Reducing complexity**: To manage the size of the model, the output vectors from self-attention layers are reduced using techniques like weighted sums. This ensures the number of vectors does not grow too large.

### **8. Adding Non-Linearity for Richer Representations**
   - **Linear functions for efficiency**: To reduce computational load, transformers replaced large neural networks in each self-attention layer with simpler **linear functions** for generating representations.
   - **Restoring non-linearity**: After applying self-attention, a neural network is used to add non-linearity back into the process, ensuring the model can still capture complex relationships between words.

### **9. Multi-Head Self-Attention for Better Representation**
   - **Multiple attention heads**: To capture more than one type of relationship between words, transformers use **multi-head self-attention**. Each head focuses on different aspects of the input and then their results are concatenated to produce a richer final representation.

### **Summary of the Evolution from CNNs to Transformers**:
1. CNNs were effective for image tasks but failed at capturing long-range dependencies in text.
2. Transformers replaced CNN’s local convolutional layers with self-attention mechanisms, enabling modeling of long-distance word relations.
3. They introduced pairwise attention scores to determine the relevance of words across sentences, solving the issue of context.
4. Positional encodings and multi-head attention allowed transformers to handle the order and complexity of text.
5. Optimizations like linear functions and multi-head attention made transformers scalable and efficient.

These advancements helped transform the way NLP tasks were approached, leading to the success of models like GPT and ChatGPT.
