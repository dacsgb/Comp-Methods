# Potential Field Path Planning Algorithm
# Diego

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

import time

class Potential():
    def __init__(self,platform, maze):
        self.map = maze
        self.robot = platform
        self.X = np.array(self.robot.X)

        self.displacement = np.hypot( (self.map.pos_fin[0]-self.robot.X[0][0]), (self.map.pos_fin[1] - self.robot.X[0][1]))
        self.distance = 0
        self.eff = None

        self.name = None
        self.name = 'Kinematic Potential Field'

    def pathplanning(self):
        print(self.name)
        print('Started Path Planning')
        left = self.displacement
        ti = time.time()
        while left >= self.robot.margin:

            dx = -self.map.Fx(self.X[-1][0], self.X[-1][1])
            dy = -self.map.Fy(self.X[-1][0], self.X[-1][1])

            theta = np.arctan2(dy,dx)
            omega = self.robot.closest_input(self.X[-1],theta)
            model_out = self.robot.kinematic(self.X[-1],[3,omega])
            self.X = np.append(self.X, model_out, axis=0)
            left = np.hypot((self.X[-1][0]-self.map.pos_fin[0]),(self.X[-1][1]-self.map.pos_fin[1]))
            #print('Potential: Distance left = {:.3f}'.format(left))
        tf = time.time()
        self.dt = tf -ti
        print('Found Path \n')

    def stats(self):
        for i in range(1,np.shape(self.X)[0]):
            self.distance += np.hypot( (self.X[i-1][0] - self.X[i][0]) , (self.X[i-1][1] - self.X[i][1]))
        self.eff = self.distance/self.displacement

        rep = self.name + '\n \n' 
        rep += 'Total Distance Travelled = {:.3f}'.format(self.distance) + '\n'
        rep +='Total Displacement = {:.3f}'.format(self.displacement)+ '\n'
        rep +='Path efficiency = {:.3f}'.format(self.eff)+ '\n'
        rep +='Time Taken to Calculate = {:.4f} [s]'.format(self.dt)+ '\n'
        rep += '\n \n'
        return rep

    def graph(self):

        plt.plot(self.X[:,0], self.X[:,1], 'b-')
        plt.show()