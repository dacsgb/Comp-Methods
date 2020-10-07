# Dynamic Window Approach 
# Diego

import numpy as np
from scipy.optimize import minimize, rosen, rosen_der
import sympy as sp
import matplotlib.pyplot as plt
import time


class DWA():
    def __init__(self,platform,maze):
        self.robot = platform # x = [x,y,theta,v,phi], u = [v,phi]
        

        self.map = maze
        self.F = None
        self.Fx = None
        self.Fy = None

        self.X = np.array(self.robot.X)
        self.displacement = np.hypot( (self.map.pos_fin[0]-self.robot.X[0][0]), (self.map.pos_fin[1] - self.robot.X[0][1]))
        self.distance = 0
        self.eff = None

        self.W = np.array([3,4,1,0.5])

        self.name = 'Dynamic Window Approach'
        

    
    def window(self):
        Vs = np.array([self.robot.v[0],self.robot.v[1],-self.robot.omega_max,self.robot.omega_max])

        a = self.X[-1][3]+self.robot.a[0]*self.robot.dt
        b = self.X[-1][3]+self.robot.a[1]*self.robot.dt
        c = self.X[-1][4]-self.robot.alpha_max*self.robot.dt
        d = self.X[-1][4]+self.robot.alpha_max*self.robot.dt

        Vd = np.array([a,b,c,d])

        win = np.array([max(Vs[0],a), min(Vs[1],b), max(Vs[2],c), min(Vs[3],d)])

        return win

    def mini(self):
        win = self.window()
        u0 = [(win[0]+win[1])/2,(win[2]+win[3])/2]
        limits = [[win[0],win[1]],[win[2],win[3]]]
        sol = minimize(self.trajectory,u0,method='SLSQP', bounds=limits)
        u = sol.x
        return u

    def trajectory(self,u):
        traj = np.array([self.X[-1]])
        t = np.linspace(0,self.robot.horizon,num=self.robot.horizon//self.robot.dt)
        for i in t:
            state = self.robot.kinematic(traj[-1],u)
            trajectory = np.append(traj,state,axis = 0)
        
        obs_cost = (self.map.R(traj[-1][0],traj[-1][1]))**2 

        dist_cost = np.hypot( (self.map.pos_fin[0]-traj[-1][0]) ,(self.map.pos_fin[1]-traj[-1][1]) )**2

        dx = self.map.pos_fin[0] - traj[-1][0]
        dy = self.map.pos_fin[1] - traj[-1][1]
        heading_cost = (traj[-1][2] - np.arctan2(dy,dx))**2

        velocity_cost = (traj[-1][3] - self.robot.v[1])**2

        obj =  self.W[0]*heading_cost
        obj += self.W[1]*dist_cost
        obj += self.W[2]*obs_cost
        obj += self.W[3]*velocity_cost

        return obj
    
    def pathplanning(self):
        print(self.name)
        print('Finding Path')
        t0 = time.time()
        left = self.displacement
        while left >= self.robot.margin:
            u = self.mini()
            nex = self.robot.kinematic(self.X[-1],u)
            self.X = np.append(self.X,nex,axis=0)
            left = np.hypot((self.X[-1][0]-self.map.pos_fin[0]),(self.X[-1][1]-self.map.pos_fin[1]))
            #print('Dynamic Window: Distance left = {:.3f}'.format(left))
        tf = time.time()
        self.dt = tf - t0
        print('Path Found \n')
    
    def stats(self):
        for i in range(1,np.shape(self.X)[0]):
            self.distance += np.hypot( (self.X[i-1][0] - self.X[i][0]) , (self.X[i-1][1] - self.X[i][1]))
        self.eff = self.distance/self.displacement 
        
        rep = self.name + '\n \n' 
        rep += 'Total Distance Travelled = {:.3f}'.format(self.distance) + '\n'
        rep +='Total Displacement = {:.3f}'.format(self.displacement)+ '\n'
        rep +='Path efficiency = {:.3f}'.format(self.eff)+ '\n'
        rep +='Time Taken to Calculate = {:.4f} [s]'.format(self.dt)+ '\n'
        rep += '\n \n'
        return rep

    def graph(self):

        plt.plot(self.X[:,0], self.X[:,1], 'b-')
        plt.show()