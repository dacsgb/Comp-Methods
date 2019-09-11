# Spring 2019 Part 1 Problem 2 

def MagVectorDiff(vector1,vector2):

    n = len(vector1)
    diff = [0]*n
    square = [0]*n

    for i in range(n):
        diff[i] = vector1[i]-vector2[i]
        square[i] = diff[i]**2

    Mag = sum(square)**(1/2)
    
    return Mag

def main():
    A = [2,1,5,9]
    B = [1,2,7,5]
    Diff = MagVectorDiff(A,B)
    print("Magnitude Difference =",Diff)

    C = [1.5,3,4,7,3]
    D = [2,4.2,4,6,3]
    Diff = MagVectorDiff(C,D)
    print("Magnitude Difference =",Diff)

main()