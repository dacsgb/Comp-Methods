import numpy as np
from scipy.interpolate import griddata, interp1d

class steam():

    def __init__(self, pressure, T = None, x = None, v = None, h = None, s = None, name = None):
        self.load_data()
        print("Data Loaded")
        self.p = pressure/100 # pressure in bars
        self.T = T  # temperature in C
        self.x = x  # quality
        self.v = v  # specific volume in 
        self.h = h
        self.s = s
        self.name = name
        self.region = None
        if T == None and x == None and v == None and h == None and s == None:
            return
        else:
            self.calc()

    def load_data(self):
        self.Tsat, self.psat, self.hfsat, self.hgsat, self.sfsat, self.sgsat, self.vfsat, self.vgsat = np.loadtxt('Homework\HW 6\sat.txt',unpack=True)
        #self.Tsat, self.psat, self.hfsat, self.hgsat, self.sfsat, self.sgsat, self.vfsat, self.vgsat = np.loadtxt('Homework\HW 6\sat.txt',unpack=True)

    def calc(self):

        # Saturated System
        if self.x == None:
            if   self.v != None:
                self.x = 0.5
            elif self.h != None:
                self.x = 1
            elif self.s != None:
                self.x = 4

        if type(self.p) != None and type(self.x) != None:  # Known T and quality and steam is saturared
            # For Saturated water
            self.T_int     = interp1d(self.psat,self.Tsat)
            self.hgsat_int = interp1d(self.psat,self.hgsat)
            self.hfsat_int = interp1d(self.psat,self.hfsat)
            self.sfsat_int = interp1d(self.psat,self.sfsat)
            self.sgsat_int = interp1d(self.psat,self.sgsat)
            self.vgsat_int = interp1d(self.psat,self.vgsat)
            self.vfsat_int = interp1d(self.psat,self.vfsat)

            self.T = self.T_int(self.p)
            self.h = self.x*self.hgsat_int(self.p) + (1-self.x)*self.hfsat_int(self.p)
            self.s = self.x*self.sgsat_int(self.p) + (1-self.x)*self.sfsat_int(self.p)
            self.v = self.x*self.vgsat_int(self.p) + (1-self.x)*self.vfsat_int(self.p)
            self.region = "Saturated"
        
        if type(self.T) != None and type(self.x) != None:
            
            self.p_int     = interp1d(self.Tsat,self.Tsat)
            self.hgsat_int = interp1d(self.Tsat,self.hgsat)
            self.hfsat_int = interp1d(self.Tsat,self.hfsat)
            self.sfsat_int = interp1d(self.Tsat,self.sfsat)
            self.sgsat_int = interp1d(self.Tsat,self.sgsat)
            self.vgsat_int = interp1d(self.Tsat,self.vgsat)
            self.vfsat_int = interp1d(self.Tsat,self.vfsat)

            self.p = self.p_int(self.T)
            self.h = self.x*self.hgsat_int(self.T) + (1-self.x)*self.hfsat_int(self.T)
            self.s = self.x*self.sgsat_int(self.T) + (1-self.x)*self.sfsat_int(self.T)
            self.v = self.x*self.vgsat_int(self.T) + (1-self.x)*self.vfsat_int(self.T)
            self.region = "Saturated"

        
        # For Superheater water
        #self.h = float(griddata((self.Tsh, self.psh), self.hsh, (self.T, self.p)))
        #self.s = float(griddata((self.tsh, self.psh), self.ssh, (self.T, self.p)))    
        #self.T = float(griddata((self.hsh, self.psh), self.Tsh, (self.h+500, self.p)))
        #self.region = "Superheated"

    def print(self):
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

    #another = steam(8575, h = 2050, name = 'State 3')
    #another.print()

    #yetanother = steam(8575, h = 3125, name='State 4')
    #yetanother.print()



if __name__ == "__main__":
    main()