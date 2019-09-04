# demonstrate x = g(x) method and functions passed to functions

from math import cos, exp, sqrt

def g1(x):
    # solving exp(-x)*cos(x) - x^2 = 0
    # rearranging as  x = sqrt(exp(-x)*cos(x))
    newx = sqrt(exp(-x) * cos(x))
    return newx

def xeqgx(func,xstart,ntimes):
    x = xstart
    for i in range(ntimes):
        x = func(x)
    return x

def main():
    solution = xeqgx(g1,0,10)
    print(solution)
    print(g1(solution))

    solution = xeqgx(lambda x:sqrt(exp(-x)*cos(x))  ,0,40)
    print(solution)
    print(g1(solution))



main()
