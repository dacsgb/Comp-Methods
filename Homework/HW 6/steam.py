import numpy as np
from scipy.interpolate import griddata

class steam():

    def __init__(self, pressure, T = None, x = None, v = None, h = None, s = None, name = None):
        self.pressure = pressure
        self.T = T
        self.x = x
        self.v = v
        self.h = h
        self.s = s
        self.name = name
        self.region = None
        if T == None and x == None, v == None, h == None, s == None, name == None:
            return
        else:
            self.calc()
    
    def calc(self):
        pass

    def print(self)
        print("Name:",self.name)
        print('Region:', self.region)
        print("p", self.p)
        print("T", self.T)
        print("h",self.h)
        print("s",self.s)
        print("v",self.v)
        print("x",self.x)

def main():
    inlet = steam(7330, name = 'Turbine Inlet')
    inlet.x = 0.9
    inlet.calc()
    inlet.print()
    h1 = inlet.h
    s1 = inlet.s
    print(h1,s1,'\n')

    outlet = steam(100, s = inlet.s, name='Turbine Exit')
    outlet.print()

    another = steam(8575, h = 2050, name = 'State 3')
    another.print()

    yetanother = steam(8575, h = 3125, name='State 4')
    yetanother.print()



if __name__ = "__main__"
    main()