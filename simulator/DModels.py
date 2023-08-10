from .Block import IOBlock
import numpy as np


class DelayBlock(IOBlock):
    def __init__(self, x0, name: str = "delay", ts: int = 1,
                 prev_block=None, next_block=None, save_states=False):
        super().__init__(name, prev_block, next_block, save_states)
        self.ts = ts
        self.x0 = x0

    def get_response(self, sim_time: float, u):
        outcome = self.x0
        self.x0 = u
        return outcome

    def get_x0(self):
        return self.x0


class LinearDModel(IOBlock):
    """ Discrete model of a state space system in the matrix representation, such as:
        x_{k+1} = A*x_{k} + B*u_{k}
        y_{k} = C*x_{k} + D*u_{k}

        Attributes:
            A:   matrix that describes the evolution of the state variables in function of his previous values.
                It has to be a square matrix

            B:   matrix that describes the impact of an external input in the evolution of the system

            C:   Transformation over the state variables to generate the output

            D:   feed-forward matrix

            ts:  Sampling time of the system

    """

    def __init__(self, A: np.ndarray, B: np.ndarray, C: np.ndarray, D: np.ndarray, x0: np.ndarray, ts=1,
                 name: str = "lin_d_sys", prev_block=None, next_block=None, save_states=False) -> None:

        super().__init__(name, prev_block, next_block, save_states)

        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.x0 = x0
        self.ts = ts

        if self.A.shape[0] == self.B.shape[0]:
            pass
        else:
            raise Exception(f'A and B matrix dimensions does not match')

        if self.B.shape[1] == self.D.shape[1]:
            pass
        else:
            raise Exception(f'B and D matrix dimensions does not match')
        if self.C.shape[0] == self.D.shape[0]:
            pass
        else:
            raise Exception(f'C and D matrix dimensions does not match')

    def get_response(self, sim_time: float, u: np.ndarray):
        if type(u) == float or type(u) == int:
            u = np.array([[u]])
        x_next = self.A @ self.x0 + self.B @ u
        y_next = self.C @ x_next + self.D @ u

        return y_next

    def get_x0(self):
        return self.x0

"""class DModel(IOBlock):
    def __init__(self, name: str, dynamics_func: function, x0, ts: int = 1,
                 prev_block=None, next_block=None, save_states=False):
        super().__init__(name, prev_block, next_block, save_states)
        self.dynamics_fun = dynamics_func
        self.ts = ts
        self.x0 = x0

    def next_state(self, x0, u):
        return self.dynamics_fun(x0, u)

    def get_response(self, sim_time: float, u):
        outcome = self.dynamics_func(x0, u)
        return"""
