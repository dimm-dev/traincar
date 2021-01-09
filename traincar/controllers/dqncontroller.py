import random
import numpy as np
from traincar.controllers.racecontroller import Action, RaceController
from traincar.models.dqn import DQNAgent
from traincar.utils.arrays import list_to_nparray

LEARN_COUNT = 1024
TRAIN_COUNT = 512
BATCH_SIZE = 64

class DQNController(RaceController):
    def __init__(self):
        super().__init__()
        self._act = self._start
        self._iteration = 0

    def act(self, state):
        self._iteration = self._iteration + 1
        return self._act(state)

    def loopback(self, reward, new_state):
        self._model.remember(self._state, self._recomendation.value, reward, list_to_nparray(new_state.snapshot()), False)

    def restart(self):
        if self._iteration > TRAIN_COUNT:
            self._model.train(len(self._model.memory))

    def _start(self, state):
        self._act = self._accumulate
        snapshot = state.snapshot()
        self._model = DQNAgent(len(snapshot), len(list(Action)))
        return self._accumulate(state)

    def _accumulate(self, state):
        self._state = list_to_nparray(state.snapshot())
        if len(self._model.memory) == LEARN_COUNT:
            self._act = self._real_act
        self._recomendation = random.sample(list(Action), 1)[0]
        return self._recomendation

    def _real_act(self, state):
        self._state = list_to_nparray(state.snapshot())
        self._recomendation = Action(self._model.act(list_to_nparray(state.snapshot())))
        return self._recomendation
