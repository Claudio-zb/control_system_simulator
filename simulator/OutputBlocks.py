from simulator.Blocks import IBlock, Block
import numpy as np


class ScopeBlock(IBlock):

    def __init__(self, name: str, prev_block: Block, save_states: bool = True):
        super().__init__(name, prev_block, save_states)

        self.input = np.zeros((prev_block.dim_output, 1))

    def get_initial_condition(self) -> np.ndarray:
        return self.input

    def get_next_state(self) -> np.ndarray:
        return self.input

    def get_state(self) -> np.ndarray:
        return self.input

    def get_response(self, sim_time: float):
        return self.input

    def set_u_k(self, u):
        self.input = u