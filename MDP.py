import numpy as np

from gym.wrappers import TimeLimit

#STAP 1: maak classe MDP aan
class MDP:
    def __init__(self, env: TimeLimit) -> None:
        super().__init__()
        self.n_actions = env.action_space.n
        self.n_states = env.observation_space
        self.transition_model = np.zeros(self.n_actions, self.n_states, self.n_states)

#methode update(percept : Percept)
