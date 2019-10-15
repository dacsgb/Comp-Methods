import numpy as np
from scipy.interpolate import griddata, interp1d

class steam():

    def __init__(self, pressure, T = None, x = None, v = None, h = None, s = None, name = None):
        self.load_data()
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
        self.Tsh,  self.hsh,  self.ssh, self.psh = np.loadtxt('Homework\HW 6\sh.txt',unpack=True)

    def calc(self):

        # calculate quality assuming

        if self.x == None:
            if self.h != None:
                self.hf = float(griddata(self.psat,self.hfsat,self.p))
                self.hg = float(griddata(self.psat,self.hgsat,self.p))
                self.x = (self.h - self.hf)/(self.hg-self.hf)
                self.region = 'Saturated'
            elif self.s != None:
                self.sf = float(griddata(self.psat,self.sfsat,self.p))
                self.sg = float(griddata(self.psat,self.sgsat,self.p))
                self.x = (self.s - self.sf)/(self.sg-self.sf)
                self.region = 'Saturated'
            elif self.v != None:
                self.vf = float(griddata(self.psat,self.vfsat,self.p))
                self.vg = float(griddata(self.psat,self.vgsat,self.p))
                self.x = (self.v - self.vf)/(self.vg-self.vf)
                self.region = 'Saturated'

        if self.region == 'Saturated':
            self.hf = float(griddata(self.psat,self.hfsat,self.p))
            self.hg = float(griddata(self.psat,self.hgsat,self.p))
            self.sf = float(griddata(self.psat,self.sfsat,self.p))
            self.sg = float(griddata(self.psat,self.sgsat,self.p))
            self.vf = float(griddata(self.psat,self.vfsat,self.p))
            self.vg = float(griddata(self.psat,self.vgsat,self.p))
            self.T = float(griddata(self.psat,self.Tsat,self.p))
            self.h = self.x*self.hg + (1-self.x)*self.hf
            self.s = self.x*self.sg + (1-self.x)*self.sf
            self.v = self.x*self.vg + (1-self.x)*self.vf
            
        
        elif self.region == 'Superheated':
            self.p*= 100
            if self.T != None:
                self.h = float(griddata((self.psh,self.Tsh),self.hsh,(self.p,self.T)))
                self.s = float(griddata((self.psh,self.Tsh),self.ssh,(self.p,self.T)))
            if self.h != None:
                self.T = float(griddata((self.psh,self.hsh),self.Tsh,(self.p,self.h)))
                self.s = float(griddata((self.psh,self.hsh),self.ssh,(self.p,self.h)))
            if self.s != None:
                self.T =float(griddata((self.psh,self.ssh),self.Tsh,(self.p,self.s)))
                self.h =float(griddata((self.psh,self.ssh),self.hsh,(self.p,self.s)))
            

        
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

    another = steam(8575, h = 2050, name = 'State 3')
    another.print()

    yetanother = steam(8575, h = 3125, name='State 4')
    yetanother.print()

if __name__ == "__main__":
    main()