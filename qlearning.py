# coding=utf-8
from __future__ import print_function
import copy
import numpy as np

MAP = '''
.........
.     .
.    o . 
.     . 
.........
'''

MAP = MAP.strip().split('\n')
MAP = [[c for c in line] for line in MAP]
DX = [-1, 1, 0, 0] # 左， 右， 上， 下
DY = [0, 0, -1, 1]


class Env(object):

    def __init__(self):
        self.map = copy.deepcopy(MAP)
        self.x = 1
        self.y = 1
        self.step = 0
        self.total_reward = 0
        self.is_end = False

    def interact(self, action):
        assert self.is_end is False
        new_x = self.x + DX[action]
        new_y = self.y + DY[action]
        new_pos_char = self.map[new_x][new_y]
        self.step += 1
        reward = 0
        if new_pos_char == '.':
            reward = 0
        elif new_pos_char == 'o':
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '
            self.is_end = True
            reward = 100
        elif new_pos_char == 'x':
            self.x = new_x
            self.y = new_y
            self.map[new_x][new_y] = ' '
            reward = -5
        self.total_reward += reward
        return reward

    @property
    def state_num(self):
        rows = len(self.map)
        cols = len(self.map[0])
        return rows * cols

    @property
    def present_state(self):
        cols = len(self.map[0])
        return self.x * cols + self.y

    def print_map(self):
        printed_map = copy.deepcopy(self.map)
        printed_map[self.x][self.y] = 'A'
        print('\n'.join([''.join([c for c in line]) for line in printed_map]))


e = Env()
Q = np.zeros((e.state_num, 4))

for i in range(200):
    while (e.is_end is False) and (e.step < MAX_STEP):
        action = epsilon_greedy(Q, e.present_state)

