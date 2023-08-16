import gymnasium as gym
import math
import random
import matplotlib
import matplotlib.pyplot as plt
from collections import namedtuple, deque
from itertools import count

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from simulator.DModels import LinearDModel
A = np.array([[1.1]])
B = np.array([[1.]])
C = np.array([[1.]])
D = np.array([[0.]])
x0 = np.array([[.5]])

mdl = LinearDModel(A, B, C, D, x0)

env = gym.make("CartPole-v1")




plt.ion()



Transition = namedtuple('Transition',
                        ('state', 'action', 'next_state', 'reward'))



# Get number of actions from gym action space
n_actions = env.action_space.n
# Get the number of state observations
state, info = env.reset()
n_observations = len(state)

policy_net = DQN(n_observations, n_actions).to(device)
target_net = DQN(n_observations, n_actions).to(device)
target_net.load_state_dict(policy_net.state_dict())

optimizer = optim.AdamW(policy_net.parameters(), lr=LR, amsgrad=True)
memory = ReplayMemory(10000)

steps_done = 0





