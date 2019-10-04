import numpy as np
import scipy.optimize as opt

def vel(Q):
    # Calculate velocities for every pipe
    v = np.zeros(len(Q)-1)
    for i in range(len(Q)-1):
        v[i] = 4*Q[i]/(np.pi*D[i]**2)
    return v

def ReNum(v):
    # Calculate Reynolds number for each pipe
    Re= (rho*abs(v)*D)/mu
    return Re

def del_p(f,L,v):
    # Calculate pressure drop for each pipe
    dp = (f*L*abs(v)*v*rho)/(2*D)
    return dp

def fric(Re):
    # Calculate friction factor
    f = (-2.0*np.log10( eps/(3.7065*D) - 5.0452/Re*np.log10( ((eps/D)**1.1098)/2.57 ) + 5.5506/(Re**0.8981)    ))**-2
    return f

def err(Q):

    E = np.zeros(1)
    v = vel(Q)
    Re = ReNum(v)
    f = fric(Re)
    p = del_p(f,L,v)

    E[0] = Qin[0] -Q[0] -Q[1]
    E = np.append(E,Q[0]-Q[2])
    E = np.append(E,Q[1]-Q[3]-Q[5])
    E = np.append(E,Q[3]-Q[4]-Q[6]-Qin[1])
    E = np.append(E,Q[2]+Q[4]-Q[7])
    E = np.append(E,Q[5]-Q[8]-Qin[2])
    E = np.append(E,Q[6]+Q[8]-Q[9])
    E = np.append(E,Q[7]+Q[9]-Q[10])
    E = np.append(E,p[1]+p[3]+p[4]-p[2]-p[0])
    E = np.append(E,p[5]+p[8]-p[6]-p[3])
    E = np.append(E,p[6]+p[9]-p[7]-p[4])

    return E

def Sol_print(Qsol):
    print("The flow in semgemnt  a-b=",Qsol[0]*1000,"L/s")
    print("The flow in semgemnt  a-c=",Qsol[1]*1000,"L/s")
    print("The flow in semgemnt  b-e=",Qsol[2]*1000,"L/s")
    print("The flow in semgemnt  c-d=",Qsol[3]*1000,"L/s")
    print("The flow in semgemnt  d-e=",Qsol[4]*1000,"L/s")
    print("The flow in semgemnt  c-f=",Qsol[5]*1000,"L/s")
    print("The flow in semgemnt  d-g=",Qsol[6]*1000,"L/s")
    print("The flow in semgemnt  e-h=",Qsol[7]*1000,"L/s")
    print("The flow in semgemnt  f-g=",Qsol[8]*1000,"L/s")
    print("The flow in semgemnt  g-h=",Qsol[9]*1000,"L/s")

rho = 1000 # density in kg/m^3
mu =  0.00089 # viscosity in Ns/m^2
eps = 0.00025   # roughness of pipe in m
D = np.array([300,200,200,200,200,150,150,150,250,250])*10**-3 # diameter of pipes in m
L = np.array([300,100,100,125,125,100,100,100,125,125]) # length of pipes in m

Q = np.array([1,1,1,1,1,1,1,1,1,1,1]) # flow in pipes and Qh in m^3/s
Qin = np.array([60,30,15])/1000 # flow entering and leaving in m^3/s

Qsol = opt.fsolve(err,[Q])
Sol_print(Qsol)

