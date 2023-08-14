import numpy as np

from simulator.InputBlocks import *
from simulator.DModels import *
from simulator.Environment import *
from simulator.Blocks import Connection, ScopeBlock
from matplotlib import pyplot as plt

A = np.array([[.8]])
B = np.array([[1]])
C = np.array([[1]])
D = np.array([[0]])
x0 = np.array([[1]])

block_1 = StepBlock(save_states=True)
block_2 = LinearDModel(A, B, C, D, x0=x0, save_states=True)
blocks = [block_1,
          block_2,
          ScopeBlock("scope1", block_2)]

connections = [Connection(blocks[0], blocks[1]),
               Connection(blocks[1], blocks[2])]

env = Environment(blocks, connections, 1)

results = env.simulation(10)

print("Número total de nodos:", "no sé")
