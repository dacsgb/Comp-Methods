import numpy as np
import matplotlib.pyplot as plt
    
class LS():
    def __init__(self,file_path,power,show_points):
        self.file = file_path
        self.power = power
        self.showpoints = show_points
        self.Coeff()

    def Coeff(self):
        self.x, self.y = np.loadtxt(self.file,unpack = True, skiprows =1)
        self.A = np.zeros((self.power+1,self.power+1))
        self.B = np.zeros(self.power+1)
        self.T = np.zeros((self.power+1,self.power+1))

        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                self.A[i][j]= sum(self.x**(i+j))
        
        for i in range(self.power+1):
            self.B[i] = sum(self.y*self.x**i)

        self.int = np.dot(np.linalg.inv(self.A),self.B)
        self.C = self.int[::-1]
        return self.C

    def Plot(self):
        self.C = self.Coeff()

        self.xcalc= np.linspace(self.x[0],self.x[-1], num= 500)
        self.y_eq = np.poly1d(self.C)
        self.ycalc = self.y_eq(self.xcalc)

        if self.showpoints == True:
            plt.plot(self.xcalc,self.ycalc, label ='Least Square Fit')
            plt.plot(self.x,self.y,'o', label='Data')
            plt.legend()
        else:
            plt.plot(self.xcalc,self.ycalc, label='Least Square Fit')
            plt.legend()
        plt.xlabel('X-Data')
        plt.ylabel('Y-Data')
        plt.title('Least Square Fit Curve')
        plt.show()

if __name__ == '__main__':
    test = LS('Homework\HW 7\Data UI\Data File 1.txt',1,True)
    print(test.x)