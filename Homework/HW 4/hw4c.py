import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sp

def FourierCoeff(fcn,L,nterms):
    a = np.zeros(nterms)
    b = np.zeros(nterms)
    f = lambda x: fcn(x)
    fc = lambda x: fcn(x)*np.cos((i*np.pi*x)/L)
    fs = lambda x: fcn(x)*np.sin((i*np.pi*x)/L)

    value , error = sp.quad(f,-L,L)
    a[0] = value/(2*L)

    for i in range(1,nterms):
        value, error    =   sp.quad(fc,-L,L)
        a[i]    =   value/L
        value, error =   sp.quad(fs,-L,L)
        b[i]    =   value/L
    b[0] = 0

    return a, b

def PlotFourier(a,b,L,xmin,xmax,npoints = 5000):
    x = np.linspace(xmin,xmax,npoints)
    y = np.zeros_like(x)

    f = lambda x: a[i]*np.cos((i*x*np.pi)/L) + b[i]*np.sin((i*x*np.pi)/L)

    for i in range(len(a)):
        y += f(x)
    
    plt.plot(x,y)
    plt.show()


def main():
    def sharkfin(x):
        if x<0:
            return (x+1)**3
        else:
            return 1 - x**3
    
    def Squarewave(x):
        if x < 0:
            return 1
        else:
            return -1

    L = 1
    a, b = FourierCoeff(sharkfin,L,50)
    print(a,"\n",b,"\n")
    PlotFourier(a,b,L,-3*L,3*L)

    L = 0.75
    a, b = FourierCoeff(Squarewave,L,50)
    print(a,"\n",b,"\n")
    PlotFourier(a,b,L,-3*L,3*L)

    L = np.pi
    a, b = FourierCoeff(lambda x: -x ,L,10)
    print(a,"\n",b,"\n")
    PlotFourier(a,b,L,-4*L,4*L,npoints=10000)

main()