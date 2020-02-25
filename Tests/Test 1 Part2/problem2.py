import math
import Functions

def Time(wspec):
    if wspec < 0.999999*wss:    # Ensure that the desired w is below the stady-state
        cv = (Kt*va)/(Ra*I)
        cw = (c*Ra+Kt**2)/(Ra*I)
        t = lambda w: 1/(cv - cw*w)
        T = Functions.Integrate(t,0,wspec)  # Integrate to find t for given omega
        return T
    
    return -1

def Speed(tspec):
    s = lambda w: Time(w) - tspec
    S = Functions.Secant(s,1,250) # Root finding for omega at time t
    return S

def main():
    print('The steady-state motor speed is - {:.2f} [rad/s]'.format(wss))
    print('{:.3f} seconds are required to reach {:.0f} [rad/s]'.format(Time(290),290))
    print('At {:.2f} seconds, the motor has reached a speed of {:.1f}'.format(0.25,Speed(0.25)))

# System Parameters
va = 115
Kt = 0.366
Ra = 2.11
I = 0.0113
c = 0.002792
wss = (Kt*va)/(Kt**2+Ra*c)

# Main Function
main()