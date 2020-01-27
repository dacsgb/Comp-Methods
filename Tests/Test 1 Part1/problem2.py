def LargestFromEither(matrix1, matrix2):

    # Create New Matrix
    m = len(matrix1)
    n = len(matrix1[0])
    A = [[0 for i in range (n)] for i in range(m)]
    
    # Iterate through matries given
    for i in range(m):
        for j in range(n):
            # Logic to choose largest abs and fill matrix A with proper signed number
            if abs(matrix1[i][j]) > abs(matrix2[i][j]):
                A[i][j] =  matrix1[i][j]
            elif abs(matrix1[i][j]) < abs(matrix2[i][j]):
                A[i][j] = matrix2[i][j]
            elif abs(matrix1[i][j]) == abs(matrix2[i][j]):
                A[i][j] =  matrix1[i][j]

    # Return created matrix
    return A

def main():
    mat1 = [[1,-5,3,-7],[2,5,11,-2],[13,-1,0,4]]
    mat2 = [[5,2,1,5],[4,3,7,1],[7,2,3,4]]

    answer = LargestFromEither(mat1,mat2)
    print(answer)

main()