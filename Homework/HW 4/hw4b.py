import numpy as np
import matplotlib.pyplot as plt

def CubicSpline(x,y,slope1=0,slope2=0):
    A = np.zeros((len(x),len(x)))
    B = np.zeros(len(x))
    a = np.zeros((len(x),4))

    A[0][0] = 1
    for i in range(1,len(x)-1):
        A[i][i-1]   =   1
        A[i][i]     =   4
        A[i][i+1]   =   1
    A[-1][-1] = 1

    B[0] = slope1
    for i in range(1,len(x)-1):
        B[i] = 3*(y[i+1]-y[i-1])/(x[i+1]-x[i])
    B[-1] = slope2

    K = np.linalg.solve(A,B)
    
    for i in range(len(x)-1):
        a[i][0] = y[i]
        a[i][1] = K[i]
        a[i][2] = 3*(y[i+1]-y[i])/(x[i+1]-x[i])**2 - (K[i+1]+2*K[i])/(x[i+1]-x[i])
        a[i][3] = 2*(y[i]-y[i+1])/(x[i+1]-x[i])**3 + (K[i+1]+K[i])/(x[i+1]-x[i])**2
        print()
    print(a)
    return a

def PlotCubicSpline(x, y, slope1 = 0, slope2 = 0, showpoints = True, npoints= 500):
    A = CubicSpline(x,y,slope1,slope2)
    
    for i in range(len(x)-1):
        xcalc= np.linspace(x[i],x[i+1],npoints)
        fcn = lambda u : A[i][0] + A[i][1]*(u-x[i]) + A[i][2]*(u-x[i])**2 + A[i][3]*(u-x[i])**3
        ycalc = fcn(xcalc)
        plt.plot(xcalc,ycalc)

    if showpoints == True:
        plt.plot(x,y,'o')

    plt.show()

def main():
    x = np.array([0.05,0.11,0.15,0.31,0.46,0.52,0.7,0.74,0.82,0.98,1.17])
    y = np.array([0.956,1.09,1.332,0.717,0.771,0.539,0.378,0.370,0.306,0.242,0.104])

    a = CubicSpline(x,y)
    PlotCubicSpline(x,y)

    print("The coefficients of the splines are")
    print(a)

main()