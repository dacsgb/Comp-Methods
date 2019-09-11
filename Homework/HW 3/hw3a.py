# Fall 2018 Part 1 Problem 2 

def MatrixTermProduct(Amatrix,Bmatrix):
    Am = len(Amatrix)
    An = len(Amatrix[0])

    Bm = len(Bmatrix)
    Bn = len(Bmatrix[0])

    Cmatrix = [[0 for i in range(An)] for j in range(Am)]

    for i in range(Am):
        for j in range(An):
            Cmatrix[i][j] = Amatrix[i][j]*Bmatrix[i][j]
    
    return Cmatrix
    
def main():
    matrix1 = [[1,-5,3,-7],[2,5,11,-2],[13,-1,0,4]]
    matrix2 = [[5,0,1,4],[4,3,2,1],[1,2,3,4]]
    answer = MatrixTermProduct(matrix1,matrix2)
    print(answer)

main()