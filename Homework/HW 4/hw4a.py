import numpy as np
import matplotlib.pyplot as plt

def LeastSquares(x,y,power):
    A = np.zeros((power+1,power+1))
    B = np.zeros(power+1)
    T = np.zeros((power+1,power+1))

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j]= sum(x**(i+j))
    
    for i in range(power+1):
        B[i] = sum(y*x**i)

    C = np.dot(np.linalg.inv(A),B)
    z = np.polyfit(x, y, power)

    return C[::-1]

def PlotLeastSquares(x,y,power,showpoints= True, npoints = 500):
    C = LeastSquares(x,y,power)

    xcalc= np.linspace(x[0],x[-1], num= npoints)
    y_eq = np.poly1d(C)
    ycalc = y_eq(xcalc)

    if showpoints == True:
        plt.plot(xcalc,ycalc, label ='Least Square Fit')
        plt.plot(x,y,'o', label='Data')
        plt.legend()
    else:
        plt.plot(xcalc,ycalc, label='Least Square Fit')
        plt.legend()
    plt.xlabel('X-Data')
    plt.ylabel('Y-Data')
    plt.title('Least Square Fit Curve')
    plt.show()

def main():
    x = np.array([0.05,0.11,0.15,0.31,0.46,0.52,0.7,0.74,0.82,0.98,1.17])
    y = np.array([0.956,1.09,1.332,0.717,0.771,0.539,0.378,0.370,0.306,0.242,0.104])
    
    power = 1
    Coeff_1 = LeastSquares(x,y,power)
    PlotLeastSquares(x,y,power)

    power = 3
    Coeff_3 = LeastSquares(x,y,power)
    PlotLeastSquares(x,y,power)

    xcalc= np.linspace(x[0],x[-1],500)

    LSF_1 = np.poly1d(Coeff_1)
    LSF_3 = np.poly1d(Coeff_3)

    y_1 = LSF_1(xcalc)
    y_3 = LSF_3(xcalc)

    plt.plot(xcalc,y_1,label='First Order Poly')
    plt.plot(xcalc,y_3,label='Third Order Poly')
    plt.plot(x,y,'o',label='Data')
    plt.legend()
    plt.xlabel('X-Data')
    plt.ylabel('Y-Data')
    plt.title('Least Square Fit Comparison')
    plt.show()

main()