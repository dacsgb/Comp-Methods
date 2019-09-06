import math
import copy

def GaussElim(Aaug):
    m = len(Aaug)
    n = len(Aaug[0])
    x = [0]*m

    if n-m !=1:
        print("Dimensions are not valid")
        return None

    for i in range(0,m):
        for j in range(i+1,m):
            f = (Aaug[j][i]/Aaug[i][i])
            x[j] = x[j] - (f*x[i])

    return x
def main():

    

    A = [[4,-1,1,3],[2,-3,1,9],[-1,1,7,-6]]
    X = GaussElim(A)
    print(X)

    C = [[4,3,1,-1,2],[2,-5,0,-2,-3],[-3,3,-6,1,5,],[0,1,4,8,-2]]
    X = GaussElim(C)
    print(X)


main()