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
