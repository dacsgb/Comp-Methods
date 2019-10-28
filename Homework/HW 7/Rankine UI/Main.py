import numpy as np

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from rankine import rankine

from Rankine_ui import Ui_Dialog

class main_window(QDialog):
    def __init__(self):
        
        super(main_window,self).__init__()

        self.p_low = None
        self.p_high = None
        self.t_high = None
        self.q = None

        #back to standard code
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        self.ui.Calculate_butt.clicked.connect(self.Calculate)
        self.ui.Temp.clicked.connect(self.temp_qual_check)
        self.ui.Quality.clicked.connect(self.temp_qual_check)

    def temp_qual_check(self):
        if self.ui.Temp.isChecked():
            self.q = False
        if self.ui.Quality.isChecked():
            self.q = True
        return

    def Calculate(self):
        self.p_low = float(self.ui.plow_in.text())
        self.p_high = float(self.ui.phigh_in.text())
        self.t_high = float(self.ui.thigh_in.text())

        if self.q == True:
            self.cycle = rankine(self.p_low,self.p_high)
        if self.q == False:
            self.cycle = rankine(self.p_low,self.p_low,self.t_high)
        self.cycle.print_summary()
        self.filling()
        return

    def filling(self):
        if self.cycle.state1.h != None:
            self.ui.h1_out.setText('{:.3f}'.format(self.cycle.state1.h))
        if self.cycle.state2.h != None:
            self.ui.h2_out.setText('{:.3f}'.format(self.cycle.state2.h))
        if self.cycle.state3.h != None:
            self.ui.h3_out.setText('{:.3f}'.format(self.cycle.state3.h))
        if self.cycle.state4.h != None:
            self.ui.h4_out.setText('{:.3f}'.format(self.cycle.state4.h))
        if self.cycle.t_high != None:
            self.ui.TW_out.setText('{:.3f}'.format(self.cycle.turb_work))
        if self.cycle.pump_work != None:
            self.ui.PW_out.setText('{:.3f}'.format(self.cycle.pump_work))
        if self.cycle.heat_added != None:
            self.ui.HA_out.setText('{:.3f}'.format(self.cycle.heat_added))
        if self.cycle.eff != None:
            self.ui.TE_out.setText('{:.3f}'.format(self.cycle.eff))


    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())