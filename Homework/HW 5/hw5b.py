import numpy as np
import scipy.optimize as opt

def Err(state):
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
mu = 0.5
state = np.array([0,0,0,0,0])

X = opt.fsolve(Err,state)
print(np.rad2deg(X[4]))