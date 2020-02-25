import numpy as np
import sys

from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from user import Ui_dialog

from classes import Truss

class main_window(QDialog):
    def __init__(self):
        super(main_window,self).__init__()
        self.ui = Ui_dialog()
        self.ui.setupUi(self)
        self.assign_widgets()

        self.truss = None
        self.file = None
        self.show()

    def assign_widgets(self):
        self.ui.Start_butt.clicked.connect(self.Create_Truss)
        self.ui.Exit_butt.clicked.connect(self.ExitApp)
    
    def Create_Truss(self):
        self.file = QFileDialog.getOpenFileName()[0]
        
        self.ui.File_out.setText(self.file)
        app.processEvents()

        f1 = open(self.file, 'r')
        data = f1.readlines()
        f1.close()

        self.truss = Truss()
        t = self.truss

        t.Read(data)

        self.ui.num_links.setText('{:8f}'.format(len(t.links)))
        self.ui.ave_link.setText('{:8.2f}'.format(t.averageLength))
        self.ui.Length_out.setText('{:8.2f}'.format(t.shortest))

    def ExitApp(self):
        app.exit()

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    app.aboutToQuit.connect(app.deleteLater)
    main_win = main_window()
    sys.exit(app.exec_())