
import numpy as np

import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from QT_demo1_simple import Ui_Dialog


class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()

        # custom code for this example
        # define any variables you want in your GUI
        self.val=0

        #back to standard code
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.assign_widgets()
        self.show()

    def assign_widgets(self):
        # heavily customized!
        self.ui.pushButton_Exit.clicked.connect(self.ExitApp)
        self.ui.pushButton_Pythagorize.clicked.connect(self.Pythagorize)

    def Pythagorize(self):
        # Read x and y
        x = float(self.ui.lineEdit_x.text())
        y = float(self.ui.lineEdit_y.text())
        self.val = x * x + y * y
        self.val = np.sqrt(self.val)

        self.ui.lineEdit_Answer.setText('{:.3f}'.format(self.val))
        return


    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())
    
 





