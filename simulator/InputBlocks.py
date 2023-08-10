from math import sin

from .Block import Block


class StepBlock(Block):
    def __init__(self, initial_value=0, final_value=1, time_step=1,
                 name="stepBlock", save_states=False, next_block: Block = None):
        self.initial_value = initial_value
        self.final_value = final_value
        self.time_step = time_step
        super().__init__(name=name, prev_block=None, next_block=next_block, save_states=save_states)

    def get_output(self, sim_time: float):
        if sim_time >= self.time_step:
            return self.final_value
        else:
            return self.initial_value


class SineWave(Block):
    def __init__(self, amplitude: float = 1, freq: float = 1, phase: float = 0,
                 save_states=False, name: str = 'SineWave', next_block: Block = None):
        self.freq = freq
        self.amplitude = amplitude
        self.phase = phase
        super().__init__(name=name, prev_block=None, next_block=next_block, save_states=save_states)

    def get_output(self, sim_time: float):
        return self.amplitude * sin(self.freq * sim_time + self.phase)
