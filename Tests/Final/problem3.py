class Matrix():
    def __init__(self,m):
        self.m = m
    
    def rowSum(self,rowIndex):
        try:
            sum = 0
            for i in range(len(self.m[rowIndex])):
                sum += self.m[rowIndex][i]
            return sum
        except:
            print('Select row in matrix')

        
    
    def colSum(self,colIndex):
        try:
            sum = 0
            for i in range(len(self.m)):
                sum += self.m[i][colIndex]
            return sum
        except:
            print('Select column in matrix')



    def transpose(self):
        m = len(self.m)
        n = len(self.m[0])

        m_trans = [[0 for i in range(m)] for j in range(n)]

        for i in range(m):
            for j in range(n):
                m_trans[j][i] = self.m[i][j]
        
        mat_tran = Matrix(m_trans)
        return mat_tran


    def show(self):
        for i in range(len(self.m)):
            print(self.m[i])
        
def main():
    m = [[1,2,3],[4,5,6],[7,8,9],[1,3,5]]
    mat = Matrix(m)
    mat.show()
    print('sum in row 1 = ',mat.rowSum(1))
    print('sum in column 2 = ',mat.colSum(2))
    tpmat = mat.transpose()
    tpmat.show()

main()