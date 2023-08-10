from abc import ABC, abstractmethod


class Block(ABC):
    """
    represents a block in the environment. A block can be connected to others Blocks acting
    as the input of the next block.
    """
    def __init__(self, name: str, prev_block=None, next_block=None, save_states=False):
        self.name = name
        self.prev_block = prev_block
        self.next_block = next_block
        self.saveStates = save_states


class OBlock(Block):
    def __int__(self, name: str, prev_block=None, next_block=None, save_states=False):
        super().__init__(name, prev_block, next_block, save_states)

    @abstractmethod
    def get_output(self, sim_time: float):
        pass


class IOBlock(Block):
    def __init__(self, name: str, initial_state,
                 prev_block=None, next_block=None, save_states=False):
        super().__init__(name, prev_block, next_block, save_states)
        self.initial_state = initial_state

    @abstractmethod
    def get_response(self, sim_time: float, u):
        pass
    @abstractmethod
    def get_x0(self):
        pass
