from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import numpy as np

class Drawing():
    def __init__(self):
        self.window = 0                                             # glut window number
        self.width, self.height = 500, 400                               # window size
        # initialization
        glutInit()                                             # initialize glut
        glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)                      # set window size
        glutInitWindowPosition(0, 0)                           # set window position
        #window = glutCreateWindow("noobtuts.com")              # create window with title
        glutDisplayFunc(self.draw())                                  # set draw function callback
        glutIdleFunc(self.draw())                                     # draw all the time
        glutMainLoop()                                         # start everything

        def draw():                                            # ondraw is called all the time
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
            glLoadIdentity()                                   # reset position
        
            # ToDo draw rectangle
        
            glutSwapBuffers()                                  # important for double buffering
        
        def gl2DText(text, x, y, font=GLUT_BITMAP_HELVETICA_18):
            glRasterPos2d(x, y)
            for ch in text:
                glutBitmapCharacter(font, ord(ch))


        def gl2DCircle(xcenter, ycenter, radius, fill=False, faces=24):
            theta = 0

            if fill:
                glBegin(GL_POLYGON)
            else:
                glBegin(GL_LINE_STRIP)

            glVertex2f(xcenter + np.cos(theta) * radius, ycenter + np.sin(theta) * radius)
            for i in range(1, faces + 1):
                theta = i / faces * 2 * np.pi
                glVertex2f(xcenter + np.cos(theta) * radius, ycenter + np.sin(theta) * radius)
            glEnd()

        def draw_rect(x, y, width, height):
            glBegin(GL_QUADS)                                  # start drawing a rectangle
            glVertex2f(x, y)                                   # bottom left point
            glVertex2f(x + width, y)                           # bottom right point
            glVertex2f(x + width, y + height)                  # top right point
            glVertex2f(x, y + height)                          # top left point
            glEnd()                                            # done drawing a rectangle

        def refresh2d(width, height):
            glViewport(0, 0, width, height)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
            glMatrixMode (GL_MODELVIEW)
            glLoadIdentity()

if __name__ == '__main__':
    Disp = Drawing()