# Code that generates a map for the robot to traverse
# Diego

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt


class Map():
    def __init__(self, obstacles,pos_fin,clearance,margin):
        self.obstacles = obstacles
        self.pos_fin = pos_fin
        self.margin = margin
        self.clearance = clearance
        self.map = None
        self.name = 'Maze'
        self.generate()
        self.calc_field()


    def generate(self):
        self.size = np.max(self.obstacles)
        self.map = np.zeros((self.size + 1,self.size + 1))
        for i in range(np.shape(self.obstacles)[1]):
            self.map[self.obstacles[0][i]][self.obstacles[1][i]] = 1
    
    def calc_field(self):
        print(self.name)
        print('Calculating Field')

        Ripples = 0
        x = sp.Symbol('x') 
        y = sp.Symbol('y')  
        for i in range(0,np.shape(self.obstacles)[1]):
            #termtoadd += self.margin*sp.exp( -((x - self.obstacles[0][i])** 2 + (y - self.obstacles[1][i])** 2)/self.margin)
            Ripples += sp.exp( self.clearance/((x - self.obstacles[0][i])** 2 + (y - self.obstacles[1][i])** 2))
        Shape = ((x - self.pos_fin[0])** 2 + (y - self.pos_fin[1])** 2)
        Field = Shape + Ripples


        Fieldx = sp.diff(Field, x)
        Fieldy = sp.diff(Field, y)

        self.F = sp.lambdify((x, y), Field)
        self.Fx = sp.lambdify((x, y), Fieldx)
        self.Fy = sp.lambdify((x, y), Fieldy)
        self.R = sp.lambdify((x, y), Ripples)

        print('Field Calculated \n')


    def graph(self):
        pointsx, pointsy = np.nonzero(self.map)
        plt.scatter(pointsx,pointsy)
        plt.title('Map Generated')
        plt.xlabel('X Position - [m]')
        plt.ylabel('Y Position - [m]')
        plt.show()