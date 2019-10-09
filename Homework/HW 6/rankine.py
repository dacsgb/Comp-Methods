import numpy as np
from scipy.interpolate import griddata
from steam import steam

class rankine():

    def __init__(self,p_low,p_high,t_high = None, name = 'Rankine Cycle')
        self.p_low = p_low
        self.p_high = p_high
        self.t_high = t_high
        self.name = name
        self.eff = None
        self.turb_work = 0
        self.pump_work= 0
        self.heat_added = 0
        self.state1 = None
        self.state2 = None
        self.state3 = None
        self.state4 = None

    def calc_eff(self):
        pass

    def print_summary(self):
        if self.eff == None:
            self.calc_eff()
        print('\n Cycle Summary for:',self.name)
        print('\n Efficiency: {:.3f}%'.format(self.eff))
        print('Turbine Work: {:.3f}%'.format(self.turb_work))
        print('Pump Work: {:.3f}%'.format(self.pump_work))
        print('Heat Added: {:.3f}%'.format(self.heat_added))
        self.state1.print()
        self.state2.print()
        self.state3.print()
        self.state4.print()

def main():
    rakine1 = rankine(8,8000, t_high = 500, name='Rankine Cycle - Superheated at Turbine Inlet')
    eff = rankine1.calc_eff()
    print(eff)

    rankine1.state3.print()
    rankine1.print_summary()

if __name__=="__main__"
    main()
