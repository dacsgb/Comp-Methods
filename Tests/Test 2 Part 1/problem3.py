import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def derriv(X,t):
    K = 0.05
    c = 10**(-4)
    R = 0.5
    L = 2*10**(-3)
    I = 9*10**(-5)
    T = 0
    v =10

    i = X[0]
    w = X[1]

    idot = (v-K*w -R*i)/L
    wdot = (K*i -c*w -T)/I

    Xd = np.array([idot,wdot])

    return Xd

def graph(X):
    plt.figure()
    plt.plot(t,X[:,0],label='Current')
    plt.xlabel('Time - [s]')
    plt.ylabel('Current - [A]')
    plt.legend()

    plt.figure()
    plt.plot(t,X[:,1],label='Omega')
    plt.xlabel('Time - [s]')
    plt.ylabel('Angular Velocity - [rad/s]')
    plt.legend()

    plt.show()

IC = np.array([0,0])
t = np.linspace(0,0.1,100)
X = odeint(derriv,IC,t)

graph(X)
