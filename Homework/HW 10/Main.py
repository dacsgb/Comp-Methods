import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from LeastSquares import LS, EX

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from window import Ui_Dialog

class PlotCanvas(FigureCanvas):

    def __init__(self, parent, width=None, height=None, dpi=100):
        if width == None: width = parent.width()/11
        if height == None: height = parent.height()/11
        fig = Figure(figsize=(width, height), dpi=dpi)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

    def plotit(self,lin = None, quad = None, cub = None, ex = None):
        self.figure.clf()

        if ex!= None:
            xcalc= np.linspace(ex.x[0],ex.x[-1], num= 500)
            ycalc = ex.fitter(xcalc,ex.co)

            ax = self.figure.subplots()
            ax.plot(xcalc,ycalc, label ='Exponential Fit')
            ax.plot(ex.x,ex.y,'o', label='Data')
            ax.legend()
            self.draw()

        elif lin != None:
            lin.xcalc= np.linspace(lin.x[0],lin.x[-1], num= 500)
            lin.y_eq = np.poly1d(lin.C)
            lin.ycalc = lin.y_eq(lin.xcalc)

            ax = self.figure.subplots()
            ax.plot(lin.xcalc,lin.ycalc, label ='Least Square Fit')
            ax.plot(lin.x,lin.y,'o', label='Data')
            ax.legend()
            self.draw()

        elif quad != None:
            quad.xcalc= np.linspace(quad.x[0],quad.x[-1], num= 500)
            quad.y_eq = np.poly1d(quad.C)
            quad.ycalc = quad.y_eq(quad.xcalc)

            ax = self.figure.subplots()
            ax.plot(quad.xcalc,quad.ycalc, label ='Least Square Fit')
            ax.plot(quad.x,quad.y,'o', label='Data')
            ax.legend()
            self.draw()
        elif cub != None:
            cub.xcalc= np.linspace(cub.x[0],cub.x[-1], num= 500)
            cub.y_eq = np.poly1d(cub.C)
            cub.ycalc = cub.y_eq(cub.xcalc)
            ax = self.figure.subplots()
            ax.plot(cub.xcalc,cub.ycalc, label ='Least Square Fit')
            ax.plot(cub.x,cub.y,'o', label='Data')
            ax.legend()
            self.draw()

class main_window(QDialog):
    def __init__(self):
        
        super(main_window,self).__init__()

        self.data = None
        self.fit = None

        #back to standard code
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        plotwin = self.ui.graphicsView
        self.graph = PlotCanvas(plotwin)
        self.show()

    def assign_widgets(self):
        self.ui.calc_but.clicked.connect(self.Calculate)
        self.ui.lin_but.clicked.connect(self.fit_check)
        self.ui.quad_but.clicked.connect(self.fit_check)
        self.ui.cub_but.clicked.connect(self.fit_check)
        self.ui.ex_but.clicked.connect(self.fit_check)
        self.ui.Exit_but.clicked.connect(self.ExitApp)
    
    def fit_check(self):
        if self.ui.ex_but.isChecked():
            self.fit = 'ex'
        if self.ui.lin_but.isChecked():
            self.fit = 'lin'
        if self.ui.quad_but.isChecked():
            self.fit = 'quad'
        if self.ui.cub_but.isChecked():
            self.fit = 'cub'

    def Calculate(self):
        self.data = self.ui.file_line.text()

        if self.fit == 'lin':
            self.LSF_lin = LS(self.data,1,True)
            self.ui.EQ_out.setText('{:.3f}x + {:.3f}'.format(self.LSF_lin.C[0],self.LSF_lin.C[1]) )
            self.graph.plotit(lin=self.LSF_lin)
        elif self.fit == 'quad':
            self.LSF_quad = LS(self.data,2,True)
            self.ui.EQ_out.setText('{:.3f}x^2 + {:.3f}x + {:.3f}'.format(self.LSF_quad.C[0],self.LSF_quad.C[1],self.LSF_quad.C[2]) )
            self.graph.plotit(quad=self.LSF_quad)
        elif self.fit == 'cub':
            self.LSF_cub = LS(self.data,3,True)
            self.ui.EQ_out.setText('{:.3f}x^3 + {:.3f}x^2 + {:.3f}x + {:.3f}'.format(self.LSF_cub.C[0],self.LSF_cub.C[1],self.LSF_cub.C[2],self.LSF_cub.C[3]))
            self.graph.plotit(cub=self.LSF_cub)
        if self.fit == 'ex':
            self.LSF_ex = EX(self.data)
            self.graph.plotit(ex = self.LSF_ex)
            self.ui.EQ_out.setText('A = {:.3f}, B = {:.3f}, C = {:.3f}'.format(self.LSF_ex.co[0],self.LSF_ex.co[1],self.LSF_ex.co[2]))
        print('Done')


    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())

