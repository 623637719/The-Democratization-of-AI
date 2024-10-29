# Q learning and Sarsa

In reinforcement learning (RL), there are two primary approaches: model-free and model-based.

## Model-Free RL
- Definition: This approach learns policies or value functions directly from interactions with the environment, without building a model of the environment's dynamics.

Characteristics:
- Generally simpler but may require more data and time to converge.

Examples:
- Q-learning
- policy gradient

## Model-Based RL
- Definition: This approach involves learning a model of the environment's dynamics and using it to make decisions or plan actions.
  
Characteristics:
- Can simulate future states and outcomes, allowing for more efficient learning.
- Typically requires less data but is more complex due to the need to accurately model the environment.
