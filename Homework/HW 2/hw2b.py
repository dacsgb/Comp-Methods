from math import *

def Secant(fcn, x0, x1, maxiter=10,  xtol=1e-5):

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

def main():

    f = lambda x: x-3*cos(x)
    lb , ub, maxiter, xtol = 1, 2, 5, 1e-4
    Root = Secant(f,lb,ub,maxiter,xtol)
    print("Root of example 1 =",Root)

    f = lambda x: cos(2*x)*x**3
    lb , ub, maxiter, xtol = 1, 2, 15, 1e-8
    Root = Secant(f,lb,ub,maxiter,xtol)
    print("Root of example 2 =",Root)

    f = lambda x: cos(2*x)*x**3
    lb , ub, maxiter, xtol = 1, 2, 3, 1e-8
    Root = Secant(f,lb,ub,maxiter,xtol)
    print("Root of example 3 =",Root)



main()