from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt



def myfunc(x):
    return 3*np.exp(-np.abs(x/10)) * np.sin(x)

def plotfunc(f,x0,x1):
    x=np.linspace(x0,x1,1000)
    y=np.zeros_like(x)
    for i in range(1000):
        y[i]=f(x[i])
    plt.plot(x,y)
    plt.show()

def myfuncconstrained(x):
    f=myfunc(x)
    penalties = 0
    if x > 6:
        penalties += (x-6)*10**6
    if x < -1:
        penalties += (-1 - x)*10**6
    return f + penalties

def myfunc2D(vals, maxR, maxThetaDeg):
    x,y=vals
    f= y**2 - y + x**2 - 3*x
    Rsquared = x**2 + y**2
    thetaDeg=np.abs(np.arctan2(y,x)*180/np.pi)
    penalty = 0
    if Rsquared > maxR**2:
        penalty += (np.sqrt(Rsquared) - maxR) * 10e6
    if thetaDeg > maxThetaDeg:
        penalty += (thetaDeg - maxThetaDeg) * 10e6
    return f + penalty





def main():
    plotfunc(myfunc, -5, 10)

# 1d minimization


    guess = 0
    # unconstrained
    answer = minimize(myfunc, guess, method='Nelder-Mead')
    #print(answer)
    print(answer.x, answer.fun)

    # constrained
    answer = minimize(myfuncconstrained, guess, method='Nelder-Mead')
    print(answer.x,answer.fun)

    guess = 3
    # unconstrained
    answer = minimize(myfunc, guess, method='Nelder-Mead')
    #print(answer)
    print(answer.x, answer.fun)

    # constrained
    answer = minimize(myfuncconstrained, guess, method='Nelder-Mead')
    print(answer.x,answer.fun,'\n\n')

    # 2D optimization - constrained
    answer = minimize(myfunc2D, [1,1], args = (6,45), method='Nelder-Mead')
    #print('\n',answer)
    print(answer.x,answer.fun)



    answer = minimize(myfunc2D, [1,1], args = (1,45), method='Nelder-Mead')
    #print('\n',answer)
    print(answer.x,answer.fun)




    answer = minimize(myfunc2D, [1, 1], args=(1, 15), method='Nelder-Mead')
    #print('\n', answer)
    print(answer.x, answer.fun)
    x=answer.x[0]
    y=answer.x[1]

    print(x,y)

    print('\n',answer)

main()