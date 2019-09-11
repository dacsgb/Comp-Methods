# Spring 2019 Part 1 Problem 3

def ColumnWithLargestSum(matrix):

    m = len(matrix)
    n = len(matrix[0])
    sums = [0]*n
    mode = -9999999999
    index = 0

    for i in range(n):
        for j in range(m):
            sums[i] += matrix[j][i]

    for i in range(len(sums)):
        if sums[i]>mode:
            index = i
            mode = sums[i]

    return index+1, mode

def main():
    A = [[3,2,5,2,3],
        [2,-1,4,5,1],
        [1,8,3,1.3,2]]
    Col, Val = ColumnWithLargestSum(A)
    print("Column: ",Col,  "has a sum of: ", Val)

    B = [[2,1,4],
        [3,2,5],
        [4,2,1],
        [1,5,2],
        [3,1,1]]
    Col, Val = ColumnWithLargestSum(B)
    print("Column: ", Col,  "has a sum of: ", Val)
main()