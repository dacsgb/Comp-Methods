import numpy as np
import scipy.integrate.quadpack as quad
import scipy.optimize as opt

import matplotlib.pyplot as plt

def sys(t,C):
    return C[0] + ( C[1]*np.exp(-C[2]*t)*np.sin(C[3]*t + C[4]))

def deriv(t,C):
    return C[1]*np.exp(-C[2]*t)*( C[3]*np.cos(C[3]*t + C[4]) - C[2]*np.sin(C[3]*t+C[4]))

def integral(t,C):
    return abs(( C[1]*np.exp(-C[2]*t)*np.sin(C[3]*t + C[4])))

def secondOrderSys(C,t_span):
    t_deriv = np.zeros(1)
    for i in range(t_span[1]):
        sol = opt.fsolve(deriv,i,args=(C))
        t_deriv = np.append(t_deriv,sol[0])
    sys_t_deriv = sys(t_deriv,C)
    sys_max = np.max(sys_t_deriv)
    sys_min = np.min(sys_t_deriv)
    if abs(sys_max) > abs(sys_min):
        t_sol = sys_max
    else:
        t_sol = sys_min

    err = quad.quad(integral,t_span[0],t_span[1],args=(C))
    print('Peak location: t = {:.3f}'.format(t_sol))
    print('Peak value: x = {:.3f}'.format(sys(t_sol,C)))
    print('Error integral: err = {:.3f}'.format(err[0]))


C = [-0.5, -4, 0.55, 0.85, 0.1]
t = [0,15]

secondOrderSys(C,t)


