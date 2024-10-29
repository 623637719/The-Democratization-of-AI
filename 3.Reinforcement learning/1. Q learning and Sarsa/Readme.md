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

Agents can also be policy-based or value based

## Policy-Based Methods
- Definition: These methods directly optimize the policy, which is a mapping from states to actions.
- Representation: Policies can be deterministic (one state will always map to 1 action) or stochastic (1 state has chances to map to any of the actions).
- Learning: Uses techniques like policy gradients to adjust the policy parameters based on the expected return.

Advantages:
- Effective in high-dimensional action spaces.
- Can learn stochastic policies, which are useful in environments with uncertainty.

## Value-Based Methods
- Definition: These methods focus on estimating the value function, which predicts the expected return from each state or state-action pair.
- Learning: Uses algorithms that update value estimates, such as Q-learning, which derives a policy indirectly from the value function.
Advantages:
- Simpler to implement in many environments.
- Examples: Q-learning, Deep Q-Networks (DQN).

## On policy and off on-policy
- On policy means that you are able to interact with the environment and get rewards
- Off policy means that you aren't able to interact with the environment but could still learn by watching others play and adjusting your value based or policy based decision making

![image](https://github.com/user-attachments/assets/74bbdcd7-64e1-4e12-8a67-077e8ba392a0)

Q-learning is a reinforcement learning algorithm used to find the optimal action-selection policy for an agent interacting with an environment.

# Q-learning Algorithm Overview:

1. Initialization:
   - Learning rate (a): Determines how much the new information overrides the old information
   - Discount factor(y): Determines how much the agent values future rewards
   - Reward matrix (R): Contains the rewards for taking specific action in specific states
   - Q-values (Q(s,a)): Initialised to zero for all states-action pairs, this representates the expected rewards the agent is going to get if it is in state s and takes action a 

2. Episode loop:
   - For each episode (a complete sequence of states and action until a terminal state is reached):

3. Action selection:
  - For each step within the episode
    - Choose an action based on exploration strategy, such as:
      - E-greedy Policy: With probability e, choose a random action (exploration); otherwise, choose the action with the highest Q-value(exploitation)
      
4. Updating the Q table:
  - Q(s,a) -> Q(s,a) + a * (r + y*Q(s(t+1),max(a)) - Q(s,a))
  - This Q(s,a) algorithm updates the expect reward when the agent is on state s and does action a is updated by the learning rate (a) times the r actually gotten from the environment plus the maximum reward on the next state minus the expected reward.

