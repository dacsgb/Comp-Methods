import numpy as np

def vel(Q):
    # Calculate velocities for every pipe
    v = 4*Q/(np.pi*D**2)
    return v

def ReNum(v):
    # Calculate Reynolds number for each pipe
    Re = (rho*abs(v)*D)/mu
    return Re

def del_p(f,L,v):
    # Calculate pressure drop for each pipe
    dp = (f*L*abs(v)*v*rho)/(2*D)
    return dp

def fric(Re):
    # Calculate friction factor
    f = (-2.0*np.log10( eps/(3.7065*D) - 5.0452/Re*np.log10( ((eps/D)**1.1098)/2.57 ) + 5.5506/(Re**0.8981)    ))**-2
    return f

def sys(Q,Qin):
    Qin[0]-Q[0]-Q[1]
    Q[0]

rho = 1000 # density in kg/m^3
mu =  0.00089 # viscosity in Ns/m^2
eps = 0.00025   # roughness of pipe in m
D = np.array([300,200,200,200,200,150,150,150,250,250])*10**-3 # diameter of pipes in m
L = np.array([300,100,100,125,125,100,100,100,125,125]) # length of pipes in m

Q = np.array([1,1,1,1,1,1,1,1,1,1,1]) # flow in pipes and Qh in m/s
Qin = np.array([60,30,15])*0.001 # flow entering and leaving in m/s




v = vel(Q)
Re = ReNum(v)
f = fric(Re)
dp = del_p(f,L,v)
Qsys = sys(Q,Qin)

print(dp)