import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt

def deriv(X,t):
    x = X[0]
    xd = X[1]
    p1 = X[2]
    p2 = X[3]

    xdd = (p1-p2)*(A/m)
    p1d = (b/(V*rho))*(y*Kv*(ps-p1) - rho*A*xd)
    p2d = -(b/(V*rho))*(y*Kv*(p2-pa) - rho*A*xd)

    Xd = np.array([xd,xdd,p1d,p2d])
    return Xd

def graph(sol,t):
    plt.subplot(2,2,1)
    plt.plot(t,sol[:,0])
    plt.xlabel('Time - [s]')
    plt.ylabel('Postion - [m]')

    plt.subplot(2,2,2)
    plt.plot(t,sol[:,1])
    plt.xlabel('Time - [s]')
    plt.ylabel('Velocity - [m/s]')

    plt.subplot(2,2,3)
    plt.plot(t,sol[:,2])
    plt.xlabel('Time - [s]')
    plt.ylabel('Pressure 1 - [Pa]')

    plt.subplot(2,2,4)
    plt.plot(t,sol[:,3])
    plt.xlabel('Time - [s]')
    plt.ylabel('Pressure 2 - [Pa]')
    
    plt.show()

b = 1
V = 1
rho = 1
Kv =5
pa = 6
ps = 4
A = 3
y = 5
m = 2

X = np.array([1,1,1,1]) # (position, velocity, pressure 1, pressure 2)
t = np.linspace(0,5,500)
sol = integrate.odeint(deriv,X,t)
graph(sol,t)