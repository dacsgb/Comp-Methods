import math
import copy

def GaussElim(Aaug):
    m = len(Aaug)
    n = len(Aaug[0])
    x = [0]*m

    if n-m !=1:
        print("Dimensions are not valid")
        return None

    return x
def main():

    

    A = [[4,-1,1,3],[2,-3,1,9],[-1,1,7,-6]]
    X = GaussSeidel(A)
    print(X)

    C = [[4,3,1,-1,2],[2,-5,0,-2,-3],[-3,3,-6,1,5,],[0,1,4,8,-2]]
    X = GaussSeidel(C)
    print(X)


main()