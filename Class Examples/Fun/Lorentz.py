import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class Lorenz():
    def __init__(self,x,y,z,dt=0.001,t_final =100):
        self.State = np.array([[x,y,z]])
        self.dt = dt
        self.max_iter = int(t_final/dt)
        print('Initialized')
        self.sim()
        self.graph()

    def deriv(self):
        self.sigma = 10
        self.rho =28
        self.beta =8/3

        self.State_dot = np.zeros(3)

        self.State_dot[0] = self.sigma*(self.State[-1][1]-self.State[-1][0])
        self.State_dot[1] = self.State[-1][0]*(self.rho - self.State[-1][2]) - self.State[-1][1]
        self.State_dot[2] = self.State[-1][0]*self.State[-1][1] - self.beta*self.State[-1][2]
        
        return self.State_dot
    
    def integrate(self):
        self.deriv()
        self.State = np.append(self.State, [self.State[-1]+ self.State_dot*self.dt], axis = 0)
    
    def sim(self):
        for i in range(self.max_iter):
            self.integrate()
            print(i)
    def graph(self):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot(self.State[:,0], self.State[:,1], self.State[:,2])

        ax.set_xlabel('X position - [m]')
        ax.set_ylabel('Y position - [m]')
        ax.set_zlabel('Z position - [m]')

        plt.show()
    
        
if __name__ == '__main__':
    sys = Lorenz(2,1,1)
    

