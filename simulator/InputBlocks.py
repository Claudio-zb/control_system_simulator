from math import sin
import numpy as np

from .Blocks import Block


class StepBlock(Block):

    def __init__(self, initial_value=np.array([[0]]), final_value=np.array([[1]]), time_step=1,
                 name="stepBlock", save_states=False, next_block: Block = None):
        self.initial_value = initial_value
        self.final_value = final_value
        self.time_step = time_step
        super().__init__(name=name, dim_input=0, dim_output=1,
                         prev_block=None, next_block=next_block, save_states=save_states)

    def get_output(self, sim_time: float) -> np.ndarray:
        if sim_time >= self.time_step:
            return self.final_value
        else:
            return self.initial_value

    def get_initial_condition(self) -> np.ndarray:
        return self.get_output(0)

    def get_state(self) -> np.ndarray:
        return self.get_output(0)

    def get_next_state(self) -> np.ndarray:
        return self.get_output(1)


class SineWave(Block):
    def __init__(self, amplitude: float = 1, freq: float = 1, phase: float = 0,
                 save_states=False, name: str = 'SineWave', next_block: Block = None):
        self.freq = freq
        self.amplitude = amplitude
        self.phase = phase
        super().__init__(name=name, dim_input=0, dim_output=1,
                         prev_block=None, next_block=next_block, save_states=save_states)

    def get_output(self, sim_time: float):
        return self.amplitude * sin(self.freq * sim_time + self.phase)

    def get_initial_condition(self) -> np.ndarray:
        return np.array([[self.get_output(0)]])

    def get_state(self) -> np.ndarray:
        return np.array([[self.get_output(0)]])

    def get_next_state(self) -> np.ndarray:
        return np.array([[self.get_output(0)]])
