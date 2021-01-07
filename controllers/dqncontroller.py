import random
from controllers.racecontroller import Action, RaceController
from models.dqn import DQNAgent

TRAIN_COUNT = 2000
BATCH_SIZE = 64

class DQNController(RaceController):
    def __init__(self):
        super().__init__()
        self._act = self._start

    def act(self, state):
        return self._act(state)

    def loopback(self, reward, new_state):
        self._model.remember(self._state, self._recomendation, reward, new_state, False)
        if len(self._model.memory) > BATCH_SIZE == 0:
            self._model.train(BATCH_SIZE)

    def _start(self, state):
        self._act = self._accumulate
        snapshot = state.snapshot()
        self._model = DQNAgent(len(snapshot), len(list(Action)))
        return self._accumulate(state)

    def _accumulate(self, state):
        self._state = state.snapshot()
        if len(self._model.memory) == TRAIN_COUNT - 1:
            self._act = self._real_act
        self._recomendation = random.sample(list(Action), 1)[0]
        return self._recomendation

    def _real_act(self, state):
        self._state = state.snapshot()
        self._recomendation = self._model.act(state)
        return self._recomendation
