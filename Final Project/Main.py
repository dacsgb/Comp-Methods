import numpy as np

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from Algorithms import Potential, DWA
from Structures import Robot, Map

from GUI.GUI import Ui_dialog

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width=None, height=None, dpi=75):
        if width == None: 
            width = parent.width()/dpi
        if height == None: 
            height = parent.height()/dpi
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def plotit(self,maze,algorithm):

        self.figure.clf()

        ax = self.figure.add_subplot(111)
        for algs in algorithm:
            ax.plot(algs.X[:,0],algs.X[:,1],label=algs.name)
        ax.plot(maze.obstacles[0,:],maze.obstacles[1,:],'bx',label= 'Obstscles')
        ax.plot(maze.pos_fin[0],maze.pos_fin[1],'bo',label = 'Goal Position')
        ax.plot
        ax.legend()

        self.draw()

class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()
        
        #back to standard code
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.assign_widgets()


        plotwin=self.ui.graphicsView
        self.m = PlotCanvas(plotwin)
        print()
        self.show()

    def assign_widgets(self):
        self.ui.Start_but.clicked.connect(self.run)
        self.ui.end_but.clicked.connect(self.ExitApp)
        self.ui.map_but.clicked.connect(self.map_load)

        self.ui.maze1.clicked.connect(self.maze_file)
        self.ui.maze2.clicked.connect(self.maze_file)
        self.ui.maze3.clicked.connect(self.maze_file)
        self.ui.maze4.clicked.connect(self.maze_file)
        self.ui.maze5.clicked.connect(self.maze_file)
        self.ui.maze6.clicked.connect(self.maze_file)
    
    def maze_file(self):
        if self.ui.maze1.isChecked():
            self.file = 'Mazes\maze1'
        if self.ui.maze2.isChecked():
            self.file = 'Mazes\maze2'
        if self.ui.maze3.isChecked():
            self.file = 'Mazes\maze3'
        if self.ui.maze4.isChecked():
            self.file = 'Mazes\maze4'
        if self.ui.maze5.isChecked():
            self.file = 'Mazes\maze5'
        if self.ui.maze6.isChecked():
            self.file = 'Mazes\maze6'
    
    def map_load(self):
        self.alg = []
        xf = float(self.ui.Xf.text())
        yf = float(self.ui.Yf.text())
        obs = np.loadtxt(self.file, delimiter= ',' ,unpack= True, ndmin=2)
        self.maze = Map.Map(obs.astype(int),[xf,yf],1,1)
        self.graphit()
        
    def graphit(self):
        self.m.plotit(self.maze,self.alg)
        
    def run(self):
        self.ui.rep_area.clear()

        xi = float(self.ui.Xi.text())
        yi = float(self.ui.Yi.text())
        ti = float(self.ui.Ti.text())
        xf = float(self.ui.Xf.text())
        yf = float(self.ui.Yf.text())
        
        self.cart = Robot.Robot([xi,yi,ti,0.0,0])

        obs = np.loadtxt(self.file, delimiter= ',' ,unpack= True, ndmin=2)

        self.maze = Map.Map(obs.astype(int),[xf,yf],self.cart.clearance,self.cart.margin)

        self.alg = [Potential.Potential(self.cart,self.maze),DWA.DWA(self.cart,self.maze)]

        self.report = ''
        self.dist_opt = None
        dist = np.inf
        self.time_opt = None
        time = np.inf

        for algorithm in self.alg:
            algorithm.pathplanning()
            self.report += algorithm.stats()
            if algorithm.distance < dist:
                self.dist_opt = algorithm
                dist = algorithm.distance
            if algorithm.dt < time:
                self.time_opt = algorithm
                time = algorithm.dt
        
        self.report += 'Computation Time Optiomal: {} \n'.format(self.time_opt.name)
        self.report += 'Distance Optimal: {} \n'.format(self.dist_opt.name)

        self.graphit()

        self.ui.rep_area.setText(self.report)


    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())