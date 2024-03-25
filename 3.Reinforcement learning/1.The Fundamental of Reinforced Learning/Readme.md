
# The Fundamental of Reinforced Learning

### Expected learnings:

1. Understanding the concepts of reinforcement learning, including agents, environments, states, actions, observations, rewards, and policies.
2. Learning about the three stages of Markov processes and how the final process connects with reinforced learning
3. Grasping the concept of states, state transitions, and transition probabilities in Markov processes.
4. Understanding the role of rewards in Markov Reward Processes and how to calculate state values and returns.
5. Learning about the discount factor (gamma) and its impact on calculating returns and state values.
6. Understanding the addition of actions in Markov Decision Processes and the concept of action spaces.
7. Learning about policies and their role in governing an agent's behaviour.
8. Visualising and interpreting transition matrices, state transition graphs, and the 3D transition matrix for Markov Decision Processes.
9. Understanding the relationship between policies, actions, and rewards in Markov Decision Processes, and how they contribute to finding optimal behaviour and maximising returns.

# What are the Markov Processes?

The Markov Processes are fundamental to Reinforced Learning, with the Markov Decision Process representing modern Reinforced Learning, although the first two stages have seemingly nothing to do with reinforced learning, it is vital to build on your understanding by following the stages.

There are 3 Markov process stages, all expanding on the previous process:

Markov Process(Observation only) → Markov Reward Process(added rewards) → Markov decision processes(added actions)

## Common difficulties:

You can continue reading to Stage 1 by clicking the blue links or press next, if you encounter difficulties understanding refer back to this:

### What is a State?

A unique set of information the agent has about the environment, encapsulating all the observable variables that are relevant to the problem being solved(sometimes in relation to itself, like the direction it is facing in snake). 

- For example, in a chess game, the state could be the current positioning of all the pieces on the board, capturing all the essential information required to determine the next move.
- In a robot navigation task, the state could include the robot's position, orientation, and sensor readings about the surrounding environment.

### What is an Agent?

Interacts with the environment by doing actions(in the MDP), making observations, and receiving rewards(MDP).

- For example a mouse in a maze
- Or a weather sensor that can only observe
- Or just a computer

### What is the Environment?

Everything outside of an agent, an agent can make observations and take actions to change the environment

- For example for chess the mood, mental state, sweat level, and shakiness of your opponent.
- For a self-driving car: The roads, other vehicles, pedestrians, traffic signals, weather conditions.
- For a stock trading agent: The financial markets, stock prices, and news events affecting markets.

### What is Observations?

Every information the agent gets about the environment or itself.

1. For a self-driving car:
    - Camera images of the road and surroundings
    - LIDAR data for detecting obstacles
    - Speed and position data from GPS and sensors
    - Traffic signal information
2. For a robot vacuum cleaner:
    - Camera images of the room
    - Sensor readings for obstacle detection
    - Battery level
    - Location coordinates within the room

### Observation vs State

- In some environments, the agent may not have direct access to the complete state information(or the state information is too large like all atoms in the universe). Instead, the agent receives observations, which are partial or noisy representations of the state.

### What is action?

Things an agent can do

- Ability to move a piece forward in Chess
- Turn the wheel in a self-driving car

### What is Reward?

A reward is a scalar feedback signal that indicates how good or bad the current state of the agent is, based on the actions it has taken. 

- Winning a piece in Chess gets you a reward
- Killing an enemy in a game gets you a reward
- Crashing into a pedestrian for a self-driving car is a negative reward

### What is Policy?

It is a set of rules that controls the agent’s behaviour. The Final objective is to gather as much return as possible to form the most optimised path through a complex environment.

- Only moving the knight in Chess is a policy, although bad
- always turning left in snake is a policy, although bad
- Randomly moving around in tic tac toe, although seemingly bad is good because it explores all possible variations
