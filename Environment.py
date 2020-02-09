import gym
import numpy as np

from gym.wrappers import TimeLimit

env = gym.make('FrozenLake-v0')


#STAP 1: maak classe MDP aan
class MDP:
    def __init__(self, env: TimeLimit) -> None:
        super().__init__()
        #verzameling acties = 4


        #verzameling states = 16


        #reward = tabel R(s,a,s')


        #transitionmodel = kans dat hij in een bepaalde state komt gegeven dat hij een state en actie heeft gekozen
        #P(s'|s,a)
        self.n_actions = env.action_space.n
        self.n_states = env.observation_space.n
        self.transition_model = np.zeros(self.n_actions, self.n_states, self.n_states)

        #discount factor gamma




#methode update(percept : Percept)

class Percept:
    def __init__(self, state, reward, action, nextState):
        self.state = state
        self.reward = reward
        self.action = action
        self.nextState = nextState


class Percept:
    #waar was ik, wat heb ik gedaan, waar ben ik nu, is het spel gedaan? = episode
    def __init__(self, percept: tuple):
        self._state, self._action, self._next_state, self._reward, self._done = percept

        @property
        def state(self):
            return self._state

        @property
        def action(self):
            return self._action

        @property
        def next_state(self):
            return self._next_state

        @property
        def reward(self):
            return self._reward

        @property
        def done(self):
            return self._done



#methode UPDATE definiëren waarin je een PERCEPT(= State + Reward + Action + volgende State') gaat binnenkrijgen waardoor die vanalles gaat updaten
#Elke keer wanneer de agent een actie onderneemt, wordt de classe MDP aangeroepen
#Wanneer het spel afgelopen is, komt er naar de input (SARS'), ook 'done' bij



##OPDRACHT 1 : schrijf een agent die kan rondwandelen met classe MDP
#class Agent
    #waar bevind ik mij
    #welke actie kies volgens de kansverdeling (= functie np.random(probabilities))
    #welke mogelijke reward krijg ik
#per episode bijhouden wat de reward was



#model policy

