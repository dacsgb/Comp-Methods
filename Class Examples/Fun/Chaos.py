import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class Chaos():
    def __init__(self,initial,dt=0.01,t_final =1e2,name = None):
        self.ic = initial
        self.dt = dt
        self.name = name
        N = int(t_final/dt)
        self.t = np.linspace(0,t_final,N)
        self.Solution = None
        if self.name != None:
            self.sim()
            self.graph()
        else:
            print('Give valid system')

    def lorenz(self,State,t):
        sigma = 10
        rho =28
        beta = 8/3

        x,y,z = State

        State_dot = np.zeros(3)

        State_dot[0] = sigma*(y-x)
        State_dot[1] = x*(rho - z) - y
        State_dot[2] = x*y - beta*z
        
        return State_dot
    
    def rossler(self,State,t):
        a = 0.2
        b =0.2
        c = 5.7

        x,y,z = State

        State_dot = np.zeros(3)
        State_dot[0] = -y -z
        State_dot[1] = x +a*y
        State_dot[2] = b + z*(x - c)
        
        return State_dot
    
    def aizawa(self,State,t):
        a = 0.95
        b = 0.7
        c = 0.6
        d = 3.5
        e = 0.25
        f = 0.1

        x,y,z = State

        State_dot = np.zeros(3)
        State_dot[0] = x*(z-b) - d*y
        State_dot[1] = d*x +y*(z-b)
        State_dot[2] = c + a*z -(z**3)/(3) - (x**2 + y**2)*(1+ e*z) + f*z*x**3

        return State_dot

    def thomas(self,State,t):
        b = 0.3

        x,y,z = State

        State_dot = np.zeros(3)
        State_dot[0] = np.sin(y) - b*x
        State_dot[1] = np.sin(z) - b*y
        State_dot[2] = np.sin(x) - b*z

        return State_dot

    def fun(self,State,t):
        b = 0.4
        x,y,z = State

        State_dot = np.zeros(3)
        State_dot[0] = np.cos(y) - b*(x)
        State_dot[1] = np.sin(z) - b*(y)
        State_dot[2] = np.cos(x) - b*(z)

        return State_dot

    def sim(self):
        if self.name == 'Lorenz':
            self.Solution = odeint(self.lorenz,self.ic,self.t)
        if self.name == 'Rossler':
            self.Solution = odeint(self.rossler,self.ic,self.t)
        if self.name == 'Aizawa':
            self.Solution = odeint(self.aizawa,self.ic,self.t)
        if self.name == 'Thomas':
            self.Solution = odeint(self.thomas,self.ic,self.t)
        if self.name == 'Fun':
            self.Solution = odeint(self.fun,self.ic,self.t)
            
    def graph(self):

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(self.Solution[:,0], self.Solution[:,1], self.Solution[:,2])
        ax.set_xlabel('X position - [m]')
        ax.set_ylabel('Y position - [m]')
        ax.set_zlabel('Z position - [m]')

         
if __name__ == '__main__':
    ic_aizawa = np.array([0.1,0,0])
    ic_rossler = np.array([1,1,1])
    ic_lorenz = np.array([1,1,1])
    ic_thomas = np.array([0,0,1])
    ic_fun = np.array([-1.175,2.06,0.965])

    # Available Names = Lorenz, Rossler, Aizawa, Thomas
    #Lorenz = Chaos(ic_lorenz,name='Lorenz')
    #Rossler = Chaos(ic_rossler,name='Rossler')
    #Aizawa = Chaos(ic_aizawa,name='Aizawa')
    #Thomas = Chaos(ic_thomas,name='Thomas')
    Fun = Chaos(ic_fun,name='Fun',t_final=1e4)
    plt.show()