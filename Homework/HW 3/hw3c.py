# Fall 2018 Part 2 Problem 2 

import math
import Functions



def Sto(Thrust):
    Weight = 56000
    S = 1000
    Cl = 2.4
    Cd = 0.0279
    rho = 0.002377
    gc = 32.2

    A = gc*(Thrust/Weight)
    B = (gc/Weight)*(0.5*S*rho*Cd)
    fcn = lambda v: v/(A-B*v**2)

    a = 0
    b = 1.2*((Weight)/(0.5*rho*S*Cl))**(1/2)

    STO = Functions.Simpson(fcn,a,b,npoints = 1000)
    
    return STO


def ThrustNeededForTakeoff(distance):

    fcn = lambda T: Sto(T) - distance
    x_new = 10e3
    x_prev = 30e3

    T = Functions.Secant(fcn,x_prev,x_new)

    return T

def main():
    Thrust = 13000
    Distance1 = 1500
    Distance2 = 1000
    print("Diestance required to take of with", Thrust, "N of Thrust=",Sto(Thrust),"m")
    print("Trust Required to take of in", Distance1, "m =", ThrustNeededForTakeoff(Distance1),"N")
    print("Trust Required to take of in", Distance2, "m =",ThrustNeededForTakeoff(Distance2),"N")

main()

