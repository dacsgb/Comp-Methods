import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt

def Err(state,W,r,Kg,mu):
    E = np.zeros(1)

    F = state[0] 
    N = state[1]
    aG = state[2]
    alpha = state[3]
    theta = state[4]

    E[0] = W*np.sin(theta) - F - (aG*W)/gc
    E  = np.append(E,N - W*np.cos(theta)) 
    E = np.append(E,F*r - (alpha*W*Kg**2)/gc)
    E = np.append(E,aG -r*alpha)
    E = np.append(E,F- mu*N)

    return E

W = 30
r = 1.5
Kg = 0.8
gc = 32.2
mu = np.empty(0)
th = np.empty(0)
ic = np.array([0,0,0,0,0])

for i in range(16):
    mu = np.append(mu, 0.1 + 0.05*i)
    X = opt.fsolve(Err,ic,args=(W,r,Kg,mu[-1]))
    th = np.append(th, X[4])

plt.figure(1)
plt.title("Angle of Impending Slip vs Coefficent of Friction")
plt.plot(mu,np.rad2deg(th))
plt.xlabel("Coefficent of Friction - [unitless]")
plt.ylabel("Angle of ramp - [deg]")
plt.show()