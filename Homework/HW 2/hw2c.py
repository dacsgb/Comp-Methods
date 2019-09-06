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
    
    if m-len(x) != 0:
        print("Initial guess dimensions and matrix dimensions do not match")
        return None

    for i in range(Niter):
        for j in range(m):
            x_old[j] = x_new[j]
            x_new[j] = Aaug[j][-1]/Aaug[j][j] +x_old[j]
            for k in range(n-1):
                x_new[j] += -(Aaug[j][k]*x_old[k])/Aaug[j][j]

    return x_new
 

def main():
    C = [[4,-1,1,3],[2,-3,1,9],[-1,1,7,-6]]
    Cx= [0,0,0]

    A = [[4,3,1,-1,2],[2,-5,0,-2,-3],[-3,3,-6,1,5,],[0,1,4,8,-2]]
    Ax = [0,0,0,0]

    iterations = 22
    X = GaussSeidel(C,Cx,iterations)
    print(X)

    iterations = 3
    X = GaussSeidel(A,Ax,iterations)
    print(X)

main()