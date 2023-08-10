import numpy as np

from simulator.InputBlocks import *
from simulator.DModels import *
from simulator.Environment import *
from matplotlib import pyplot as plt

env = Environment(StepBlock(), [DelayBlock(0), DelayBlock(0)])
trajectory = env.simulation(10)
# plt.stem(trajectory)
# plt.show()
A = np.eye(1) * 0.5
B = np.eye(1)
C = np.eye(1)
D = np.zeros_like(C)
x0 = np.array([[1]])
sys = LinearDModel(A, B, C, D, x0)
y = sys.get_response(0, np.array([[1]]))
print(y)
print("simulation finished")
