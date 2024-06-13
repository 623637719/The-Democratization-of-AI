# Timeline of Machine Learning
## Early Foundations
### 1936: Alan Turing <img width="40" alt="SCR-20240325-nmsz" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/a779ecb7-ce58-43d4-a1c1-2f0c719c2345">
Turing, often considered the father of artificial intelligence, proposes the concept of a machine capable of computation, laying the groundwork for AI. His 1936 paper on the "Turing machine" provided a mathematical model for computation that is considered the foundation of computer science. This work helped establish the theoretical limits and capabilities of intelligent machines.

- A Turing machine is an idealised model of a central processing unit (CPU) that controls all data manipulation done by a computer

### 1943: The McCulloch and Pitts Model
Warren McCulloch and Walter Pitts develop a mathematical model for neural networks, using a combination of mathematics and algorithms to mimic how neurons in the brain might work. This introduces weights, biases, and an activation function. The McCulloch and Pitts Model laid the groundwork for the development of more advanced artificial neural network models, such as the perceptron and multilayer feedforward neural networks. But, the original McCulloch and Pitts Model does not have a built-in learning mechanism, meaning that the weights and connections must be manually set or determined through other means.

<img width="1000" alt="SCR-20240325-nmsz" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/a6f243cb-657e-479d-9859-883c0bb11d1e">

### 1950: The Turing Test
Turing proposed the "Turing test" as a way to evaluate the intelligence of a machine. The test involves a human evaluator interacting with a machine through text exchanges, trying to determine whether the "respondent" is a human or a machine. Turing's idea that a machine could potentially pass as indistinguishable from a human was groundbreaking and laid the foundations for the field of AI.
## Mid-20th Century Developments
### 1962: Frank Rosenblatt
Frank Rosenblatt introduces the Perceptron, an early type of artificial neural network that can learn and make decisions. However, it is later criticized for being unable to solve the XOR problem, highlighting the limitations of early neural networks. The XOR problem is a simple example of a nonlinear problem, but it highlights the limitations of single-layer, linear models like the perception. More complex, real-world problems often exhibit similar nonlinearities, which cannot be effectively solved by perception-based models alone. The perceptron is a simple linear classifier that can only learn to separate data that is linearly separable. The XOR function is a nonlinear problem, where the decision boundary required to separate the classes is not a straight line.
### AI winter #1:
The first AI winter spanned the 1970s and early 1980s. During this time, AI research failed to live up to the inflated expectations and promises made in the 1960s. Funding dried up as AI systems were unable to achieve human-level performance on many tasks as quickly as had been predicted. The inability to solve fundamental problems in areas like natural language processing and computer vision contributed to the loss of enthusiasm. THe search space grew exponentially for algorithms, outpacing primitive hardware at the time.
## Late 20th Century Advancements
### 1986: Backpropagation Algorithm
David Rumelhart, Geoffrey Hinton, and Ronald Williams developed the backpropagation training algorithm, which significantly enhances the training of neural networks by efficiently calculating gradients.
### Late 1980s - 1990s:
Yann LeCun develops CNN structure
Convolutional Neural Networks (CNNs) are introduced by Yann LeCun, revolutionizing image recognition and computer vision tasks. 

CNNs use convolutional layers that apply a set of learnable filters to the input image. These filters are designed to detect low-level features like edges, shapes, and textures. The convolutional layers then combine these local features to identify higher-level patterns in the image. CNNs are well-suited for image recognition tasks because they exploit the spatial relationship of pixels in an image. The convolutional layers allow the network to learn features that are invariant to the position of the object in the image, making CNNs robust to translation, scaling, and other transformations.

Hinton's Contributions Geoffrey Hinton pioneers deep neural networks (DNNs) with multiple layers and develops unsupervised learning methods to initialize DNNs, followed by fine-tuning weights using backpropagation.
### AI winter #2:
The second AI winter occurred in the early 2000s. After a period of renewed optimism and investment in the 1990s, a series of high-profile failures, such as the collapse of companies like Webvan that had promised to use AI for logistics, led to another backlash against AI. Funding and interest waned once again as the technology failed to deliver on ambitious claims.
## Early 21st Century
### 2005+: CNN Variants
Various CNN architectures emerge, including:
VGG-19: A deep CNN known for its simplicity and depth.
Plain Network and Residual Neural Network (ResNet): Introduced by Kaiming He et al., ResNet addresses the vanishing gradient problem through skip connections.
### 2012: AlexNet
Alex Krizhevsky, Ilya Sutskever, and Geoffrey Hinton develop AlexNet, which wins the ImageNet competition and popularizes deep learning.
### 2014: Generative Adversarial Networks (GANs)
Ian Goodfellow introduces GANs, which consist of two neural networks (a generator and a discriminator) competing against each other, leading to impressive results in generating realistic data.
### 2018: BERT Language Model
Google introduces BERT (Bidirectional Encoder Representations from Transformers), a transformer-based model that achieves state-of-the-art results in natural language understanding tasks.
## Recurrent Neural Networks and Beyond
### Recurrent Neural Networks (RNNs)
RNNs, designed for sequential data, are applied to text generation, classification, sentiment prediction, and estimation.
### Long Short-Term Memory (LSTM)
LSTM networks, a type of RNN, are developed to address the vanishing gradient problem and are widely used for tasks requiring long-term dependencies.
### Transformer Model
The Transformer model, introduced by Vaswani et al., revolutionizes NLP with its encoder-decoder architecture and self-attention mechanism, leading to superior performance in sequence-to-sequence tasks.
## Key Concepts and Technologies
### Neurons and Neural Networks
The human brain consists of approximately 100 billion neurons, inspiring the development of artificial neural networks.
### Dimensionality and Classification
Concepts such as linear separability, dimensionality reduction, and classifiers are crucial in understanding the mechanics of neural networks.
### Matrix Operations
Matrix operations are fundamental in neural network computations, with FLOPs (Floating Point Operations per Second) being a key metric for performance.
### Shallow to Deep Networks
The transition from shallow neural networks to deep neural networks (DNNs) marks a significant advancement in the field, enabling more complex and accurate models.
## Applications and Impact
### Sequential Data Applications
RNNs and LSTMs are employed in various applications like text generation, sentiment analysis, and other sequential data tasks.
### Encoder-Decoder and Seq2Seq Models
These models are pivotal in machine translation and other sequence-to-sequence tasks, leveraging the power of transformers and attention mechanisms.
