# Spring 2019 Part 2 Problem 2 
import math

def Zero(fcn, x0, x1, maxiter=1000,  xtol=1e-5):

    running = True
    it = 0
    x_new = x1
    x_prev = x0

    while running == True:

        if abs(x_new-x_prev)<= xtol or it > maxiter:
            running = False

        else:
            storage = x_new
            x_new = x_new - fcn(x_new)*((x_new-x_prev)/(fcn(x_new) - fcn(x_prev)))
            x_prev = storage
            it +=1

    return x_new

def Integrate(fcn, a, b, npoints=21):

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

def SigmaMax(z):
    Length = 320
    Fmoment = lambda x: x*(1.5*math.cos(x/Length))
    Moment = Integrate(Fmoment,0,Length,20)
    Smax = Moment/z
    return Smax 

def DesignTheSpar(DesignStress):
    DesEq = lambda x: SigmaMax(x) - DesignStress
    Modulus = Zero(DesEq,1,5)
    return Modulus

def main():
    A = SigmaMax(3.5)
    B = SigmaMax(1.5)
    C = DesignTheSpar(25000)

    print(A)
    print(B)
    print(C)

main()