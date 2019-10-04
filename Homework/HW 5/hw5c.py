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
    plt.figure(1)
    plt.title('System State Response')

    plt.subplot(2,2,1)
    plt.title('Mass Position')
    plt.plot(t,sol[:,0])
    plt.xlabel('Time - [s]')
    plt.ylabel('Postion - [m]')

    plt.subplot(2,2,2)
    plt.title('Mass Velocity')
    plt.plot(t,sol[:,1])
    plt.xlabel('Time - [s]')
    plt.ylabel('Velocity - [m/s]')

    plt.subplot(2,2,3)
    plt.title('Pressure 1')
    plt.plot(t,sol[:,2])
    plt.xlabel('Time - [s]')
    plt.ylabel('Pressure - [Pa]')

    plt.subplot(2,2,4)
    plt.title('Pressure 2')
    plt.plot(t,sol[:,3])
    plt.xlabel('Time - [s]')
    plt.ylabel('Pressure - [Pa]')

    plt.figure(2)
    plt.title('Pressures in Pistions')
    plt.plot(t,sol[:,2],label = 'Pressure 1')
    plt.plot(t,sol[:,3],label = 'Pressure 2')
    plt.xlabel('Time - [s]')
    plt.ylabel('Pressure - [Pa]')
    plt.legend()

    plt.figure(3)
    plt.title('Mass Velocity')
    plt.plot(t,sol[:,1])
    plt.xlabel('Time - [s]')
    plt.ylabel('Velocity - [m/s]')
    
    plt.show()

A = 4.909*10**-4
ps = 1.4*10**7
pa = 1*10**5
V = 1.473*10**-4
b =2*10**9
rho = 850
Kv = 2*10**-5
m = 30

y = 0.002 # System input
ic = np.array([0,0,pa,pa]) # (position, velocity, pressure 1, pressure 2)
t = np.linspace(0,0.05,500) # time vector

X = integrate.odeint(deriv,ic,t) # solve system
graph(X,t) # graph system response