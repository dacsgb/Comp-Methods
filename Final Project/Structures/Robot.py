# Code that containts the kinematics and configuration of the robot
# Diego

import numpy as np

class Robot(object):
    def __init__(self,pos_i):
        print('Robot')
        self.X = np.array([pos_i]) # [x,y,theta,v,omega]
        self.u = np.array([0.0,0.0]) # [v,omega]

        self.v = np.array([-0.5,5.0])
        self.a = np.array([-0.25,0.5])
        self.omega_max = 1
        self.alpha_max = 0.5

        self.dt = 0.1
        self.horizon = 1.5
        self.margin = 1.0
        self.clearance = 1.5

        print('Robot Initialized \n')

    def closest_input(self,x,theta):
        dtheta = theta-x[2]
        dtheta_max = self.omega_max*self.dt

        if dtheta > dtheta_max:
            omega = self.omega_max

        if dtheta < -dtheta_max:
            omega = -self.omega_max

        else:
            omega = dtheta/self.dt
            if abs(omega) > self.omega_max:
                omega = self.omega_max * (omega/abs(omega))

        return omega

    def kinematic(self,x,u): # x = [x,y,theta,v,omega], u = [v,omega]

        x[2] += u[1]*self.dt
        x[0] += u[0]*np.cos(x[2])*self.dt
        x[1] += u[0]*np.sin(x[2])*self.dt

        x[3] =  u[0]   
        x[4] =  u[1]

        state = np.array([x])
        return state
