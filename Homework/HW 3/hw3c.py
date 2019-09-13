# Fall 2018 Part 2 Problem 2 

import math

def Sto(Thrust):
    Weight = 56000
    S = 1000
    Cl = 2.4
    Cd = 0.0279
    rho = 0.002377
    gc = 32.2
    npoints = 1000

    A = gc*(Thrust/Weight)
    B = (gc/Weight)*(0.5*S*rho*Cd)
    fcn = lambda v: v/(A-B*v**2)

    a = 0
    b = 1.2*((Weight)/(0.5*rho*S*Cl))**(1/2)

    if math.remainder(npoints,2) == 0:
        npoints += 1

    dt = (b-a)/(npoints-1)
    x = [0]*npoints

    for i in range(len(x)):
        x[i] = a + i*dt

    I = 0

    for i in range(0,npoints):
        if i == 0:
            I += fcn(x[i])
        elif i == npoints-1:
            I += fcn(x[i])
            break
        elif i % 2 == 0:
            I += 2*fcn(x[i])
        elif i % 2 == 1:
            I += 4*fcn(x[i])

    I = dt*I/3
    
    return I


def ThrustNeededForTakeoff(distance):

    fcn = lambda s: Sto(s) - distance
    running = True
    it = 0
    x_new = 1
    x_prev = distance
    maxiter=1e4
    xtol=1e-5

    while running == True:

        if abs(x_new-x_prev)<= xtol or it > maxiter:
            running = False

        else:
            storage = x_new
            x_new = x_new - fcn(x_new)*((x_new-x_prev)/(fcn(x_new) - fcn(x_prev)))
            x_prev = storage
            it +=1

    return x_new

def main():
    Thrust = 13000
    print(Sto(Thrust))
    print(ThrustNeededForTakeoff(1500))
    print(ThrustNeededForTakeoff(1000))

main()

