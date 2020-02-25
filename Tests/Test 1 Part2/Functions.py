import math
import copy

def interpolate(x,xvals, yvals):

    for i in range(len(xvals)):
        if (x - xvals[i] > 0):
            start = i

    inter = yvals[start] + (x - xvals[start]) * (yvals[start + 1] - yvals[start])/(xvals[start + 1] - xvals[start])

    return inter

def Integrate(fcn, a, b, npoints=100):

    if a > b:
        print(" Incorrect bounds")
        return None

    if math.remainder(npoints,2) == 0:
        npoints += 1

    dt = (b-a)/(npoints-1)
    x = [0]*npoints

    for i in range(len(x)):
        x[i] = a + i*dt

    I = 0

    for i in range(0,npoints):
        if i == 0:
            I += fcn(x[i])
        elif i == npoints-1:
            I += fcn(x[i])
            break
        elif i % 2 == 0:
            I += 2*fcn(x[i])
        elif i % 2 == 1:
            I += 4*fcn(x[i])

    I = dt*I/3

    return I

def Secant(fcn, x0, x1, maxiter=1000,  xtol=1e-5):

    running = True
    it = 0
    x_new = x1
    x_prev = x0

    while running == True:

        if abs(x_new-x_prev)<= xtol or it > maxiter:
            running = False

        else:
            storage = x_new
            x_new = x_new - fcn(x_new)*((x_new-x_prev)/(fcn(x_new) - fcn(x_prev)))
            x_prev = storage
            it +=1

    return x_new

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

    return x
