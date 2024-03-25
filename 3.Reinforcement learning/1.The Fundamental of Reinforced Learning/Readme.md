
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

# What is Reinforced Learning?

Reinforced learning(which is a subset of Machine learning) involves an agent that learns to interact with an environment by taking actions and receiving feedback in the form of rewards or penalties. The goal of reinforcement learning is to train an agent to maximize its cumulative rewards over time by trial-and-error exploration and exploitation to learn optimal policies. 

For example, a mouse exploring a dangerous maze and after countless trials and errors like being electrified and killed(and respawning) finds the most efficient way to get the cheese without setting off the electric traps.

It is ok if you don’t understand what this is talking about, just read on.

*It is important to distinguish deep learning and reinforced learning, while deep learning is to represent complex patterns and relationships in data, reinforcement learning, on the other hand, is a type of machine learning that deals with decision-making and probabilities.

# What are the Markov Processes?

The Markov Processes are fundamental to Reinforced Learning, with the Markov Decision Process representing modern Reinforced Learning, although the first two stages have seemingly nothing to do with reinforced learning, it is vital to build on your understanding by following the stages.

There are 3 Markov process stages, all expanding on the previous process:

Markov Process(Observation only) → Markov Reward Process(added rewards) → Markov decision processes(added actions)

You can continue reading to Stage 1 and if you encounter difficulties understanding refer back to this:

You can continue reading to Stage 1 and if you encounter difficulties understanding refer back to this:

## Common difficulties:

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

## Stage 1: Markov process

The main objective of an agent in this stage: make accurate predictions of the probabilities of transitioning between source state and target state

Markov processes are widely used in various fields, including mathematics, physics, computer science, finance, and biology. They are particularly useful in modelling systems that exhibit random but probabilistic behaviour, where the future states are influenced by the current state but not by any long-term memory or previous events.

In the Markov Process an agent can only observe and configure predictions(unlike in the later stages where an agent can receive rewards and do actions), an agent is the object that interacts with(later on in the Markov Decision Process) or observes the environment. For example, a weather sensor that can only observe the current weather and make predictions about future weather is an agent. 

The agent observes in episodes, for example, this is one episode: Sunny, Rainy, Sunny, Sunny. Because of this chain-like structure sometimes Markov Process is called the Markov chain. The agent also has a state space(finite), containing all possible observations the agent can make of its environment in relation to the condition of the agent. In this case, the possible state spaces are Rainy and Sunny. The probabilities from a state(source state) transitioning to another state(target state) form a transition matrix, of dimensions NxN, where N is the number of states.

Our model can easily adjust the probabilities as the observations come in, for example:

Observation: Rainy, Rainy, Rainy, Sunny, Rainy, Sunny, Sunny, Rainy.

|  | Rainy | Sunny |
| --- | --- | --- |
| Rainy | 2 out of 4 cases are Rainy after Rainy | 2 out of 4 are Sunny after Rainy |
| Sunny | 2 out of 3 cases are Rainy after Sunny | 1 out of 3 cases is Sunny after Sunny |

*The row represents the source states(i) and the column is the target state that it can transition to(j), the probabilities are the probability for i → j.

Calculated:

|  | Rainy | Sunny |
| --- | --- | --- |
| Rainy | 50% | 50% |
| Sunny | 67% | 33% |

So the agent can say that there is a 50 percent chance for Rainy weather to follow up with either Rainy again or Sunny, it could also say that after Sunny it is twice as likely to be sunny again rather than Rainy. So the more episodes it obverse the more accurate it is to representing the weather probabilities of the virtual environment(by the law of large numbers). 

You can also create a state transition graph:
<img width="900" alt="SCR-20240325-nmsz" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/765bf435-7e76-4055-ab19-c49c43ec200b">

*The circles are the states and the percentages are in blue.

You may be wondering, aren’t there many factors that influence the weather? It’s not just the probability that a weather occurs after another weather. You would be correct, this is just an oversimplified example. This example is assuming that weather is just probabilities because the Markov property states that for the Markov Process to produce effective results the future transitions from any state have to depend only on the current state.

### Summary

- Agent observes the environment in episodes
- State space includes all possible observations of the environment in relation to the agent
- Transition matrix is created(2D) with probabilities

## Stage 2: Markov reward process

The main objective of an agent in this stage: find the most optimised path

As the name implies, a reward or incentive system is expanded on the base Markov Process, now aside from storing the probability of transitioning between states there is a reward for transitioning from state to state, or sometimes getting to a state is a reward in itself.

You may be wondering if the agent can’t do any actions what is the point of rewards? Rewards now are not like rewards in the next evolution of the process, it is a measure of desirability, it can be big or small, negative or positive. With the addition of reward values which are added in manually, we can calculate how desirable a state is to be in(or the state value) for the agent and the return, which is the sum of all rewards that the agent expects to receive

For example, let us envision a student as an agent, the student is able to study, procrastinate, and chat with friends. Here is the transition matrix after observing the student over a couple of days in episodes:

|  | Study | Procrastinate | Chat |
| --- | --- | --- | --- |
| Study | 25% | 50% | 25% |
| Procrastinate | 10% | 70% | 20% |
| Chat | 10% | 30% | 60% |

Now let’s add rewards to each transition:

|  | Study | Procrastinate | Chat |
| --- | --- | --- | --- |
| Study | 25%, 10 | 50%, -3 | 25%, -1 |
| Procrastinate | 10%, 5 | 70%, -6 | 20%, -1 |
| Chat | 10%, 5 | 30%, -3  | 60%, -1 |

We can also make a state transition graph:
<img width="850" alt="SCR-20240325-nnzo" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/b0b0045c-db0d-4f4d-abae-ca5407f5c3cb">

*The reward is in red.

We can add reward values manually, so as you can see when you study you earn a positive reward of 5 because studying is good and studying again gives you 10 as it means the student is hard-working, chatting is bad but not as bad as procrastination so the reward is -1 and procrastination is -3(procrastinating again means you are lazy so -6). 

One possible return for study is

Study = 5(study again) + -3(procrastinate) +  -3(procrastinate again)…. until infinity

You may be wondering, since the calculation of return continues forever how could it possibly be calculated?

The solution is that rewards are multiplied by the discount factor raised to the power of the number of steps from the starting point where the agent starts calculating. Basically how far into the future it sees. If gamma(discount factor γ) equals 1, then return just equals a sum of all subsequent rewards(it will continue forever unless there are Sink states, which are states that you can’t get out of). If gamma(discount factor γ) equals 0, **will be just the immediate reward without calculating any subsequent states and will correspond to absolute short-sightedness.

The function to calculate the return or Gt is:
<img width="555" alt="coolsocks" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/15e1c619-1481-4933-a5cf-5da188a9fb2c">

*Gt is the return value, R is the reward and the subscript where k increases is the time or the next reward, gamma starts to come in after the first one and the power it is raised to is increased each step.

Extreme values like 1 or 0 are only useful in specific cases, like using gamma equal to 1 in tic tac toe as there can only be 9 moves per game. Most of the time, gamma is set to 0.9 or 0.99. Think of gamma as how far into the future we look to estimate the future return.

This return quantity is not very useful, as it was for every specific chain that could happen, and since it is all chance, the return could change quite easily. So value of state is used, it is the mathematical expectation of return for any state(probability * reward). 

So to calculate the value of state for Study with gamma of 0:

= 0.25*10 + 0.5*-3 * 0.25 * -1

= 2.5 - 1.5 - 0.25

= 0.75

And procrastination:

= 0.1 * 5 + 0.7 * -6 + 0.2 * -1

= 0.5 - 4.2 - 0.2

= -3.9

And chatting:

= 0.1 * 5 + 0.3 * -3 + 0.6 * -1

= 0.5 - 0.9 - 0.6

= -1

As shown Study is the most valuable state to be in. If the gamma was equal to 1 the value of state of all of them will be negative infinity, as you will go to each state an infinite number of times and the negative rewards have a higher (percentage * reward) output.

### Summary

- Reward is a measure of desirability
- Value of state can tell you how favourable it is to be in a state
- Return is the sum of all rewards that the agent expects to receive from its starting stage and going down a specific chain of stages
- Gamma γ is the discount factor between 0 and 1 that controls how far into the future the agent looks

## Stage 3: Markov decision process

The main objective of agent in this stage: learn optimal behaviour in a complex environment by repeatedly taking actions and receiving rewards.

The agent can now interact with the environment through a set of actions called the action space. Actions can be discrete (e.g., moving left or right) or continuous (e.g., turning the steering wheel to a certain degree).

The transition matrix now includes an additional action dimension, becoming a 3D cube. The probabilities in this cube represent the likelihood of transitioning from state i to state j given action k. The reward function also changes, as the reward received depends on both the resulting state and the action taken.

The 3D transition matrix now for an agent:
