from .Block import Block, OBlock, IOBlock
import numpy as np


class Environment:
    def __init__(self, root: OBlock, sequence: list[IOBlock], ts=1):
        self.sequence = sequence
        self.ts = ts
        self.root = root

    def simulation(self, final_time):
        sim_time = 0
        response = []
        while sim_time <= final_time:
            temp_output = self.root.get_output(sim_time)
            for item in self.sequence:
                temp_output = item.get_response(sim_time, temp_output)
            response.append(temp_output)
            sim_time += self.ts
        return response

    def pre_simulation(self, final_time):

        """Prepares the environment before running a simulation and
        creates a dictionary which will collect the trajectory of the desired blocks """

        n_steps = np.ceil(final_time / self.ts)
        outputs = {}
        if self.root.saveStates:
            outputs.update({self.root.name: self.root.get_output(0)})
        for item in self.sequence:
            if item.saveStates:
                outputs.update({item.name: item.get_x0()})
