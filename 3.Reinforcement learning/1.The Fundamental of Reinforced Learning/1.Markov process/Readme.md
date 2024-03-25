## Stage 1: Markov process

The main objective of an agent in this stage: make accurate predictions of the probabilities of transitioning between two states(source state and target state)

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

[Next](https://github.com/623637719/The-Democratization-of-AI/tree/main/3.Reinforcement%20learning/1.The%20Fundamental%20of%20Reinforced%20Learning/2.Markov%20reward%20process)
