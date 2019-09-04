def MatrixSumSmall(vals,small):
    
    sum = 0 

    for i in range(len(vals)):
        for j in range(len(vals[i])):
            if abs(vals[i][j]) <= small:
                sum = sum + abs(vals[i][j])

    return sum


def IntArrayMaxDuplicates(vals):

    size = max(vals)
    freq = [0]*size
    mode = 0

    for i in range(len(vals)):
        index = vals[i]
        freq[index-1] = freq[index-1] + 1
    
    for i in range(size-1,-1,-1):
        if freq[i] > mode:
            mode = freq[i]
            index = i

    return (index+1), freq[index]

def Horner(x,coeffs):
    
    deg = len(coeffs)
    value = coeffs[deg-1]*x +coeffs[deg-2]

    for i in range(3,deg+1,1):
        value = value*x + coeffs[deg-i]

    return value

def interp1D(x,xvals, yvals):

    for i in range(len(xvals)):
        if (x - xvals[i] > 0):
            start = i

    inter = yvals[start] + (x - xvals[start]) * (yvals[start + 1] - yvals[start])/(xvals[start + 1] - xvals[start])

    return inter

def main(): # define the variables needed to test the required functions
    myvals = [1,5,2,3,5,5,3,5,2,5,3,3,1,5]  
    mymatrix = [[1, 3.7 , -7, 4],                 
                [-8, 9, 2, -1.8 ],                 
                [-12, 7.9, 3.2, 13]]    
    a = [3, 1, -2, -4]     
    xvals = [1, 2, 4, 5, 7]     
    yvals = [2, 4, -2, 4, 5]     
    x1 = 1.3    
    x2 = 6.4
    mysmall = 4.9

    # for part a)
    mysum2 = MatrixSumSmall(mymatrix, mysmall) 
    print('a)  Sum of small values = {:.1f}'.format(mysum2))
    
    # for part b)
    val, count = IntArrayMaxDuplicates(myvals)
    print('b)  The value {:d} appears {:d} times in '.format(val, count) , myvals)
    
    # for part c)
    poly = Horner(x1, a) 
    print('c)  Polynomial value for (x1= {:.2f}) = {:.1f}'.format(x1, poly))
    
    # for part d)
    y = interp1D(x2, xvals, yvals)
    print('d)  Interpolated value for (x2= {:.2f}) = {:.3f}'.format(x2, y))

main()