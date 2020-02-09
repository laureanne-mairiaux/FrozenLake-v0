import gym
import numpy as np

from gym.wrappers import TimeLimit

class FrozenLake(env):
    def __init__(self) -> None:
        self.env = gym.make('FrozenLake-v0')

    def reset(self):
        return self.env.reset()

    def step(self, _action: int):
        return self.env.step(_action)

    def n_actions(self):
        return env.action_space.n

    def n_actions(self):
        return env.observation_space.n

    

class Percept:
    #waar was ik, wat heb ik gedaan, waar ben ik nu, welke reward heb ik gekregen, is het spel gedaan? = episode
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


#STAP 1: maak classe MDP aan
class MDP:
    def __init__(self, env: TimeLimit) -> None:
        super().__init__()
        self.env = env
        self.y = y #discount gamma
        self.n_actions = env.action_space.n
        self.n_states = env.observation_space.n

        #reward = tabel R(s,a,s')
        self._reward_model = np.zeros((self.n_states, self.n_actions))

        #sa_model = frequentie van state en actie is voorgekomen
        self.n_sa = np.zeros((self.n_states, self.n_actions))

        #tsa_model = frequentie state t is voorgekomen na een state s NA een actie a
        self.n_tsa = np.zeros((self.n_states, self.n_states, self.n_actions))

        #transitionmodel = kans dat hij in een bepaalde state komt gegeven dat hij een state en actie heeft gekozen
        #P(s'|s,a)
        self.transition_model = np.zeros(self.n_actions, self.n_states, self.n_states)

        self.n = 0

#methode update(percept : Percept)
    def update(self, percept: Percept) -> None:
        self.n += 1
        self.update_reward(percept)
        self.update_counts(percept)
        self.update_transition_model(percept)

    #################   WEEK 5 : 11 min 59 sec
    def update_reward(self, percept: Percept) -> None:
        self._reward_model[(percept._state, percept._action)] = np.average(self._reward_model[percept._state, percept._action], ... )

    def update_counts(self, percept : Percept) -> None:
        self.n_sa[percept._state, percept._action] += 1
        self.n_tsa[percept._next_state, percept._state, percept._action] += 1

    def update_transition_model(self, percept: Percept) -> None:
        for t in range(self.n_states):
            p = self.n_tsa[t, percept._state, percept._action] / self.n_sa[percept._state, percept._action]
            self.transition_model[t, percept._state, percept._action] = p

    def p(self, tsa) -> float:
        return self.transition_model[tsa]

    def reward(self, _state: int, _action : int) -> float:
        return self._reward_model[_state, _action]

    @property
    def reward_model(self):
        return self._reward_model

    def counts(self) -> tuple:
        return np.count_nonzero(self.n_sa), np.count_nonzero(self.n_tsa), np.count_nonzero(self.transition_model) ...





















#methode UPDATE definiëren waarin je een PERCEPT(= State + Reward + Action + volgende State') gaat binnenkrijgen waardoor die vanalles gaat updaten
#Elke keer wanneer de agent een actie onderneemt, wordt de classe MDP aangeroepen
#Wanneer het spel afgelopen is, komt er naar de input (SARS'), ook 'done' bij



##OPDRACHT 1 : schrijf een agent die kan rondwandelen met classe MDP

    #waar bevind ik mij
    #welke actie kies volgens de kansverdeling (= functie np.random(probabilities))
    #welke mogelijke reward krijg ik
#per episode bijhouden wat de reward was
#class Agent




#model policy

