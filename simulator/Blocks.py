from abc import ABC, abstractmethod
import numpy as np
import networkx as nx


class Block(ABC):
    """
    represents a block in the environment. A block can be connected to others Blocks acting
    as the input of the next block.
    """

    def __init__(self, name: str, dim_input: int, dim_output: int,
                 prev_block=None, next_block=None, save_states=False):
        self.name = name
        self.dim_input = dim_input
        self.dim_output = dim_output
        self.prev_block = prev_block
        self.next_block = next_block
        self.saveStates = save_states

    @abstractmethod
    def get_initial_condition(self):
        pass

    @abstractmethod
    def get_next_state(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


def connect(block1: Block, block2: Block):
    block1.next_block = block2
    block2.prev_block = block1
    return


class OBlock(Block, ABC):
    def __int__(self, name: str, dim_output: int, next_block=None, save_states=False):
        super().__init__(name, dim_input=0, dim_output=dim_output,
                         prev_block=None, next_block=next_block, save_states=save_states)

    @abstractmethod
    def get_output(self, sim_time: float):
        pass

    @abstractmethod
    def get_initial_condition(self):
        pass

    @abstractmethod
    def get_next_state(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class IOBlock(Block, ABC):
    def __init__(self, name: str, dim_input: int, dim_output: int, initial_state,
                 prev_block: Block = None, next_block: Block = None, save_states=False):

        super().__init__(name, dim_input, dim_output, prev_block, next_block, save_states)

        self.initial_state = initial_state
        if prev_block is not None:
            self.initial_input = prev_block.get_initial_condition()
        else:
            self.initial_input = np.array([[0]])

    @abstractmethod
    def get_response(self, sim_time: float):
        pass

    @abstractmethod
    def get_initial_condition(self):
        pass

    @abstractmethod
    def set_u_k(self, u):
        pass

    @abstractmethod
    def get_next_state(self):
        pass

    @abstractmethod
    def get_state(self):
        pass


class Connection:
    def __init__(self, block1: Block, block2: Block):
        self.source = block1
        self.target = block2
