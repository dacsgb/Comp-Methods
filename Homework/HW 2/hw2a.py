import math
import copy

def Simpson(fcn, a, b, npoints=21):

    if a > b:
        print(" Incorrect bounds")
        return None

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

def main():

    f1 = lambda x: x-3*math.cos(x)
    a1 , b1, n1 = 1, 3, 10
    I1 = Simpson(f1,a1,b1,n1)
    print("The value of the integration is: ",I1)
    
    f2 = lambda x: x**3 * math.cos(2*x)
    a2, b2, n2 = 2, 3, 23
    I2 = Simpson(f2,a2,b2,n2)
    print("The value of the integration is: ",I2)

main()