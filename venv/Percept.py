
class Percept:
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
