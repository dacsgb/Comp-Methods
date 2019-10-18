import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

def eq1(x):
    y = 3*x**3 -2*x -4
    return y

def eq2(x):
    y = -5*x**2 -3
    return y

def err(x):
    er = eq1(x) - eq2(x)
    return er

def plot(x1,x2):
    x = np.linspace(-1,1,100)
    y1 = eq1(x)
    y2 = eq2(x)

    plt.plot(x,y1,label='Equation 1')
    plt.plot(x,y2,label = 'Equation 2')
    plt.plot(x1,eq1(x1),'o')
    plt.plot(x2,eq1(x2),'o')

    plt.xlabel('X axis')
    plt.ylabel('Y Axis')
    plt.legend()
    plt.show()


def solve():
    Sol1 = fsolve(err,[0])
    Sol2 = fsolve(err,[1])

    print('Solution 1 to equations x = ',Sol1,'y = ',eq1(Sol1))
    print('Solution 2 to equations x = ',Sol2,'y =',eq1(Sol2))

    return Sol1, Sol2


Sol1,Sol2 = solve()
plot(Sol1,Sol2)


