import math
import copy

def GaussElim(Aaug):
    
    # Read augmented matrix dimensions
    m = len(Aaug)
    n = len(Aaug[0])

    # Check dimensions of Data
    if n-m !=1:
        print("Dimensions are not valid")
        return None
    
    # Create A and b from Augmented Matrix
    A = [[0 for i in range(m)] for j in range(n-1)]
    b = [0]*m

    for i in range(m):
        b[i] = Aaug[i][-1]

    for i in range(m):
        for j in range(n-1):
            A[i][j] = Aaug[i][j]

    # Upper Triangular Form
    for i in range(m):
        for j in range(i+1,m):
            f = (A[j][i]/A[i][i])
            b[j] = b[j] - (f*b[i])
            for k in range(n-1):
                A[j][k] = A[j][k] - f*A[i][k]
    
    # Reverse Substitution
    x = [0]*len(b)

    x[m-1] = b[m-1]/A[m-1][m-1]

    for i in range(m-2,-1,-1):
        suma = 0
        for j in range(n-1):
            suma += A[i][j]*x[j]
        x[i] = (b[i]-suma)/A[i][i]

    print(A)
    print(b)
    print(x)

    return x
def main():

    

    A = [[4,-1,1,3],[2,-3,1,9],[-1,1,7,-6]]
    X = GaussElim(A)
    #print(X)

    C = [[4,3,1,-1,2],[2,-5,0,-2,-3],[-3,3,-6,1,5,],[0,1,4,8,-2]]
    X = GaussElim(C)
    #print(X)


main()