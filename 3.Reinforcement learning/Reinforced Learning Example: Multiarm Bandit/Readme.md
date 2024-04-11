# Multiarm bandit
Imagine a scene: in front of you are four slot machines, Each one has a certain chance to give you 100 dollars, you can only flip any one of them 100 times in total. As you approach them, you can't help but wonder if there's an optimised solution to get the most benefit from your limited tries.
<img width="1395" alt="image" src="https://github.com/623637719/The-Democratization-of-AI/assets/84779222/47d68fc9-8b6c-414c-8b6f-2534ef4db844">

You donʼt know the payout probabilities for any of the machines. Should you just keep playing the same machine, or should you try out different machines to see which ones are the most rewarding?
This is the exploration-exploitation dilemma. Exploration means trying out new things to learn more about them. Exploitation means sticking with what you know works. In the multi-armed bandit problem, you need to balance exploration and exploitation to maximize your rewards.

This problem is perfectly presented by Reinforced learning.

As you may remember, Reinforcement learning mimics the way humans learn through trial and error. It involves training an agent to make decisions based on a reward system, where the agent learns to maximize its reward by interacting with its environment. In this case, our environment is the slot machines, the agent is you, the states are the result after flipping the four slot machines, the action is flipping a slot machine, and the reward is the money received.

Now, let's break down how reinforced learning can be applied to solve the slot machine problem. The first step is to define our goal. In this scenario, our objective is to find the optimal strategy that maximises our winnings over a series of plays, why is another name for strategy? Policy.

Let us envision four slot machines with percentages to give out 100 dollars to equal 0.1, 0.9, and 0.5 and 0.2. Let our policy to be flip all the slot machines an equal number of times we will get an average amount of money equal to (0.1 * 100 + 0.9 * 100 + 0.5 * 100 + 0.2 * 100)*25 = 170 * 25 = 4250.

But if our policy is we first test each slot machine 10 times(exploration phase) and use the remaining 60 tries to only use the slot machine that gives us the best result(exploitation phase) we will get an expected winning of 4250 * 0.4 + (0.9 * 100) * 60 = 7100(sometimes if the luck is bad we would get inefficient outcomes)

First, we need to set up a function for the agent to interact with the environment: let's create a function that has three actions 0,1,2,3 for the three slot machines, different slot machines have different percentages of giving out the award, 10 per cent, 50 per cent, 60 per cent and 90 per cent, using a function from Numpy we can use the percentage from the actions to give awards accordingly, let's test it, action 0 should give a reward of 10, 50 per cent of times, action 2 should give a reward of 10, 90 per cent of times.

```
import numpy as np
# Function to interact with the environment (slot machines)
def play_slot_machine(action):
    # Define the payout probabilities for each slot machine
    probabilities = [0.1, 0.9, 0.5, 0.2]
    # Generate a random number to determine the reward
    if np.random.uniform(0,1) <= probabilities[action]:
        return 100
    else:
return 0
```
It starts with no prior knowledge of the machines' payout patterns or probabilities. So it will create two lists of Q and N, initialising with zeros, Q standing for how useful a given action is in achieving future rewards, Q can be updated each time as Q plus the reward received - Q divided by the number of Q actions taken before, and N is the number of times the action was chosen, ```epsilon``` is the percentage that the agent will explore, meaning choosing a random action, and the rest of the times it will choose the action with the biggest Q value, Num_step means how much times it will play the slot machine, 1000 so the results will be more consistent. 

```
# Initialize Q and N lists with zeros
num_actions = 4
Q = np.zeros(num_actions)
N = np.zeros(num_actions)
# Set the exploration rate (epsilon) and number of steps
epsilon = 0.4
num_steps = 1000
# Play the slot machines for the specified number of steps
for step in range(num_steps):
    # Determine whether to explore or exploit
    if np.random.rand() < epsilon:
        # Explore: choose a random action
        action = np.random.randint(num_actions)
    else:
        # Exploit: choose the action with the highest Q value
        action = np.argmax(Q)
    # Interact with the environment and get the reward
    reward = play_slot_machine(action)
    # Update the action count
    N[action] += 1
    # Update the Q value for the chosen action
    Q[action] += (reward - Q[action]) / N[action]
    # Print the final Q values
print("Q values for actions: 1:", round(Q[0]), "2:", round(Q[1]),"3:",round(Q[2]),"4:",round(Q[3]) )
```
At the beginning, the agent's actions will be random, exploring the different possibilities and gathering information about the slot machines' behaviour. However, as the agent receives feedback in the form of rewards, it starts to refine its strategy. Through a process called "exploitation," the agent gradually selects actions that have proven to be more rewarding in the past.
Here is a sample output:
```
Q values for actions: 1: 20 2: 43 3: 45 4: 92
```
It's important to note that reinforced learning is not a guaranteed way to beat the slot machines every time. The outcome of each play is still subject to chance, and there will always be an element of uncertainty. However, by using reinforced learning, we can tilt the odds in our favour and improve our overall winnings over time.
