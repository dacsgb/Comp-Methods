import math
import copy

def GaussSeidel(Aaug, x, Niter = 15):
    x_old = copy.deepcopy(x)
    x_new = copy.deepcopy(x)

    m = len(Aaug)
    n = len(Aaug[0])

    if n-m !=1:
        print("Dimensions are not valid")
        return None

    for i in range(Niter):
        for j in range(m):
            x_old[j] = x_new[j]
            x_new[j] = Aaug[j][-1]/Aaug[j][j]
            for k in range(n-1):
                x_new[j] += -(Aaug[j][k]*x_old[k])/Aaug[j][j]
            x_new[j] += x_old[j]

    return x_new
 

def main():

    A = [[4,3,1,-1,2],[2,-5,0,-2,-3],[-3,3,-6,1,5,],[0,1,4,8,-2]]
    x = [0,0,0,0]
    iterations = 3
    X = GaussSeidel(A,x,iterations)
    print("System:")
    print(A)
    print("Solution")
    print(X)

main()