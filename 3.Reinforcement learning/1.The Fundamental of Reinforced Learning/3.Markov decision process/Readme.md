## Stage 3: Markov decision process

The main objective of agent in this stage: learn optimal behaviour in a complex environment by repeatedly taking actions and receiving rewards.

The agent can now interact with the environment through a set of actions called the action space. Actions can be discrete (e.g., moving left or right) or continuous (e.g., turning the steering wheel to a certain degree).

The transition matrix now includes an additional action dimension, becoming a 3D cube. The probabilities in this cube represent the likelihood of transitioning from state i to state j given action k. The reward function also changes, as the reward received depends on both the resulting state and the action taken.

The 3D transition matrix now for an agent:

<img width="1287" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/1b0a1342-c849-4fc6-be3e-e5093ff31f92">

*In all the small cubes in the big cube are probabilities and reward values

The reward function now influences the agent's action selection. Consider a scenario where a mouse (the agent) is in the center square of a 1x3 cage, with a piece of cheese on the left side. The mouse is initially facing upwards and has three possible actions: turn left, turn right, or move forward.

The state space in this environment can be calculated as the number of possible positions (3) multiplied by the number of possible orientations (4), resulting in 3 x 4 = 12 distinct states. 

<img width="539" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/c6351d9a-58ea-4b78-9687-8c4ac4e0dccc">

But here is a part of the transition graph for the mouse:

<img width="1297" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/95e91e44-5496-4b2a-aa94-c8c1886a9174">

*The 1-3 represents the three squares from the left to the right and the direction on the bottom represents which direction the mouse is facing. The text on the arrows represents the action that it takes to get to the next state. The mouse starts at 2 facing the direction up and has two different choices, turning left and turning right and so on and so forth.

A policy is a set of rules that determines the agent's behaviour in a reinforcement learning environment. The agent's objective is to maximize the expected return, which is the cumulative discounted rewards obtained over time. 

After exploring the environment and filling out the transition matrix (exploration phase), the agent can exploit its learned knowledge to follow the most rewarding sequence of actions (exploitation phase). During exploitation, the agent uses the transition matrix to identify and follow the path that maximises the expected return.

Consider the following three policies for the mouse-in-cage scenario:

1. Turn left and move forward if possible.
2. Always turn left.
3. Randomly choose an action and execute if possible.

*All three policies eventually transition to an exploitation phase

The third policy, which randomly selects actions, is the best for exploring all possible states in the environment. The first two deterministic policies cannot reach certain states due to their fixed rules.

With the random policy, the agent will eventually visit all reachable squares while facing all possible directions, allowing it to explore the entire state space.

Once the transition matrix is sufficiently filled during exploration, the agent can calculate the expected returns for each state-action pair with discount factor (γ < 1). The optimal action is turning left and moving forward, as it yields the highest return: γ * 10. Although there are multiple paths to reach the cheese, the most direct path maximises the return due to the discounting of future rewards.

### Summary

- The addition of action causes the transition matrix to turn into a cube
- Action space includes all the actions the agent can do
- The reward function now serves its intended purpose to influence the agent’s actions
- Policy is what governs the agent’s actions, whether it is to explore and in what way or whether it is to go for the most optimised action or series of actions it has discovered

[Next](https://github.com/623637719/The-Democratization-of-AI/tree/main/3.Reinforcement%20learning/1.The%20Fundamental%20of%20Reinforced%20Learning/4.Conclusion)
