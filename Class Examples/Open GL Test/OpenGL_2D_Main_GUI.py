# standard PyQt5 imports
import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QEvent

# standard OpenGL imports
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from OpenGL_2D_class import gl2D, gl2DText, gl2DCircle

# the ui created by Designer and pyuic
from OpenGL_2D_ui import Ui_Dialog

# import the Problem Specific class
from DroneCatcher import DroneCatcher


class main_window(QDialog):
    def __init__(self):
        super(main_window, self).__init__()
        self.ui = Ui_Dialog()
        # setup the GUI
        self.ui.setupUi(self)

        # define any data (including object variables) your program might need
        self.mydrone = DroneCatcher()

        # create and setup the GL window object
        self.setupGLWindows()

        # and define any Widget callbacks (buttons, etc) or other necessary setup
        self.assign_widgets()

        # show the GUI
        self.show()

    def assign_widgets(self):  # callbacks for Widgets on your GUI
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_Animate.clicked.connect(self.StartAnimation)
        self.ui.pushButton_StopAnimation.clicked.connect(self.StopAnimation)
        self.ui.pushButton_PauseResumeAnimation.clicked.connect(self.PauseResumeAnimation)
        self.ui.horizontalSlider_zoom.valueChanged.connect(self.glZoomSlider)
        self.ui.checkBox_Dragging.stateChanged.connect(self.DraggingOnOff)

    # Widget callbacks start here

    def glZoomSlider(self):  # I used a slider to control GL zooming
        zoomval = float((self.ui.horizontalSlider_zoom.value()) / 200 + 0.25)
        self.glwindow1.glZoom(zoomval)  # set the zoom value
        self.glwindow1.glUpdate()  # update the GL image

    def DraggingOnOff(self):  # used a checkbox to Enable GL Dragging
        if self.ui.checkBox_Dragging.isChecked():  # start dragging
            self.StartStopDragging(True)  # StartStopDragging is defined below
        else:  # stop dragging
            self.StartStopDragging(False)

    def StartAnimation(self):  # a button to start GL Animation
        self.glwindow1.glStartAnimation(self.AnimationCallback, self.mydrone.nframes,
                                    reverse=False, repeat=False, reset=True,
                                    RestartDraggingCallback=self.StartStopDragging)

    def StopAnimation(self):  # a button to Stop GL Animati0n
        self.glwindow1.glStopAnimation()

    def PauseResumeAnimation(self):  # a button to Resume GL Animation
        self.glwindow1.glPauseResumeAnimation()

    def ExitApp(self):
        app.exit()

    # Essential, but only if using mouse information with GL
    def eventFilter(self, source, event):  # allow GL to handle Mouse Events
        self.glwindow1.glHandleMouseEvents(event)  # let GL handle the event
        return super(QDialog, self).eventFilter(source, event)

    # Setup OpenGL Drawing and Viewing
    def setupGLWindows(self):  # setup all GL windows
        # send it the   GL Widget     and the drawing Callback function
        self.glwindow1 = gl2D(self.ui.openGLWidget, self.DrawingCallback)

        # set the drawing space:    xmin  xmax  ymin   ymax
        self.glwindow1.setViewSize(-10, 500, -10, 200, allowDistortion=False)

        # Optional: Setup GL Mouse Functionality
        self.ui.openGLWidget.installEventFilter(self)  # to read mouse events
        self.ui.openGLWidget.setMouseTracking(True)  # to enable mouse events

        # OPTIONAL: to display the mouse location  - the name of the TextBox
        self.glwindow1.glMouseDisplayTextBox(self.ui.MouseLocation)

    def DrawingCallback(self):
        # this is what actually draws the picture
        self.mydrone.DrawDronePicture()  # drawing is done by the DroneCatcher object

        # if using dragging, let GL show dragging handles
        self.glwindow1.glDraggingShowHandles()

    def AnimationCallback(self, frame, nframes):
        # calculations handled by DroneCapture class
        self.mydrone.ConfigureAnimationFrame(frame, nframes)
        # the next line is absolutely required for pause, resume, stop, etc !!!
        app.processEvents()

    def draggingCallback(self, x, y, draglist, index):
        # calculations handled by DroneCapture class
        self.mydrone.DraggingListItemChanged(x, y, draglist, index)
        return

    def StartStopDragging(self, start):  # needs problem specific customization!
        if start is True:
            draglist = self.mydrone.CreateDraggingList()
            near = 15  # define an acceptable mouse distance for dragging
            self.glwindow1.glStartDragging(self.draggingCallback, draglist, near,
                                           handlesize=4, handlewidth=1, handlecolor=[1, 0, 0])
            self.ui.checkBox_Dragging.setChecked(True)
        elif start is False:
            self.glwindow1.glStopDragging()
            self.ui.checkBox_Dragging.setChecked(False)


if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
