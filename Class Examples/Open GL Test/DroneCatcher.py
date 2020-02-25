import numpy as np

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL_2D_class import gl2D, gl2DText, gl2DCircle


class   DroneCatcher():

    def __init__(self):
        # define any data (including object variables) your program might need

        #canon data
        self.cannon_x = 0
        self.cannon_y = 0
        self.barrel_angle = 45 * np.pi / 180
        self.barrel_length = 30
        self.barrel_x = self.cannon_x + self.barrel_length * np.cos(self.barrel_angle)
        self.barrel_y = self.cannon_y + self.barrel_length * np.sin(self.barrel_angle)

        #ball (projectile) data
        self.ball_x = self.barrel_x
        self.ball_y = self.barrel_y
        self.ball_speed = 110
        self.ball_v0x = self.ball_speed * np.cos(self.barrel_angle)
        self.ball_v0y = self.ball_speed * np.sin(self.barrel_angle)

        self.drone_x = 400
        self.drone_y = 100
        self.drone_speed = 25
        self.gc = 32.2

        #data for animation
        self.nframes = 121
        self.dronepath = np.zeros([self.nframes, 2])
        self.ballpath = np.zeros([self.nframes, 2])
        self.tmax = 1.5 * self.ball_speed/self.gc
        self.CalculateFlightPaths()


    def CalculateFlightPaths(self):
        # This to draw the picture and during animation!
        for frame in range(self.nframes):
            time = self.tmax * frame / self.nframes

            dronex = self.drone_x - self.drone_speed * time

            ballx = self.barrel_x + self.ball_v0x * time
            bally = self.barrel_y + self.ball_v0y * time - self.gc / 2 * time ** 2

            self.dronepath[frame, :] = [dronex, self.drone_y]
            self.ballpath[frame, :] = [ballx, bally]
     #end  def

    def DrawDronePicture(self):
        # this is what actually draws the picture
        # using data to control what is drawn

        # Draw cannon base
        glColor3f(0, 1, 0)  #
        glLineWidth(1.5)
        gl2DCircle(self.cannon_x, self.cannon_y, 10, fill=True)

        # Draw the barrel
        glColor3f(0.9, 0.9, 0.25)
        glLineWidth(6)
        glBegin(GL_LINE_STRIP)  # begin drawing connected lines
        # use GL_LINE for drawing a series of disconnected lines
        glVertex2f(self.cannon_x, self.cannon_y)
        glVertex2f(self.barrel_x, self.barrel_y)
        glEnd()

        # Draw the drone
        glColor3f(0.8, 1, 0.8)
        glLineWidth(1.5)
        gl2DCircle(self.drone_x, self.drone_y, 10, fill=True)

        # Draw the ball - projectile
        glColor3f(1, 1, 0)
        glLineWidth(1.5)
        gl2DCircle(self.ball_x, self.ball_y, 6, fill=True)

        # draw the drone flight path

        glColor3f(0.9, 0.9, 0.25)
        glLineWidth(2)
        glEnable(GL_LINE_STIPPLE)  # enable a dashed line
        glLineStipple(1, 0x00FF)  # the value for dashed lines
        glBegin(GL_LINE_STRIP)  # begin drawing connected lines
        # use GL_LINE for drawing a series of disconnected lines
        for i in range(self.nframes):
            glVertex2f(self.dronepath[i, 0], self.dronepath[i, 1])
        glEnd()
        glDisable(GL_LINE_STIPPLE)  # disable the dashed line

        # draw the ball  path
        glColor3f(0.25, 0.9, 0.9)
        glLineWidth(2)
        glEnable(GL_LINE_STIPPLE)  # enable a dashed line
        glLineStipple(1, 0x00FF)  # the value for dashed lines
        glBegin(GL_LINE_STRIP)  # begin drawing connected lines
        for i in range(self.nframes):
            glVertex2f(self.ballpath[i, 0], self.ballpath[i, 1])
        glEnd()
        glDisable(GL_LINE_STIPPLE)  # enable a dashed line

    def ConfigureAnimationFrame(self, frame, nframes):
        self.drone_x = self.dronepath[frame, 0]
        self.ball_x = self.ballpath[frame, 0]
        self.ball_y = self.ballpath[frame, 1]

    def CreateDraggingList(self):
        # put locations of "draggable" things into a  list
        draglist = [[self.cannon_x, self.cannon_y],
                    [self.barrel_x, self.barrel_y],
                    [self.drone_x, self.drone_y]]
        return draglist


    def DraggingListItemChanged(self, x, y, draglist, index):
        #Change the data as necessary if an item is being dragged (repositioned).
        if index == 0:  # cannon base
            self.cannon_x = x  # move the cannon in the x direction only!

            #cannon position affects the barrel and ball positions (x only)
            self.barrel_x = self.cannon_x + self.barrel_length * np.cos(self.barrel_angle)
            self.ball_x = self.barrel_x

            #Required - the draglist must be modified for changes to be accepted!!!
            draglist[0][0] =self.cannon_x  # save only cannon_x back to the draglist
            draglist[1] = [self.barrel_x, self.barrel_y] #but the barrel changed as well!

        if index == 1:  # change the barrel angle only
            self.barrel_angle = np.arctan2(y, x - self.cannon_x)
            self.barrel_x = self.cannon_x + self.barrel_length * np.cos(self.barrel_angle)
            self.barrel_y = self.cannon_y + self.barrel_length * np.sin(self.barrel_angle)
            #barrel changes affect the ball starting point
            self.ball_x = self.barrel_x
            self.ball_y = self.barrel_y
            #and the ball initial velocity
            self.ball_v0x = self.ball_speed * np.cos(self.barrel_angle)
            self.ball_v0y = self.ball_speed * np.sin(self.barrel_angle)

            draglist[1] = [self.barrel_x, self.barrel_y]

        if index == 2:  # change the drone position
            self.drone_x, self.drone_y = [x, y]

            draglist[2] = [x, y]  # only save the x value to the draglist
        self.CalculateFlightPaths()
