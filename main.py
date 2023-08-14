import numpy as np

from simulator.InputBlocks import *
from simulator.DModels import *
from simulator.Environment import *
from simulator.Blocks import Connection
from matplotlib import pyplot as plt

blocks = [DelayBlock(x0=np.array([[1]]), name="delay0"),
          DelayBlock(x0=np.array([[2]]), name="delay1"),
          DelayBlock(x0=np.array([[3]]), name="delay2")]


connections = [Connection(blocks[0], blocks[1]),
               Connection(blocks[1], blocks[2]),
               Connection(blocks[2], blocks[0])]

env = Environment(blocks, connections, 1)

results = env.simulation(10)



print("Número total de nodos:", "no sé")
