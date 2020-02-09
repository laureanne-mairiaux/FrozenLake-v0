import gym

env = gym.make('FrozenLake-v0')




class Percept:
    def __init__(self, state, reward, action, nextState):
        self.state = state
        self.reward = reward
        self.action = action
        self.nextState = nextState



#methode UPDATE definiëren waarin je een PERCEPT(= State + Reward + Action + volgende State') gaat binnenkrijgen waardoor die vanalles gaat updaten
#Elke keer wanneer de agent een actie onderneemt, wordt de classe MDP aangeroepen
#Wanneer het spel afgelopen is, komt er naar de input (SARS'), ook 'done' bij



##STAP 2 : maak class PERCEPT (= SARS')


##OPDRACHT 1 : schrijf een agent die kan rondwandelen met classe MDP


#uitglijden = 1/3 kans dat je effectief naar de richting gaat die je hebt gekozen. 2/3 kans dat je uitglijdt 
