# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_demo1_radiobuttons.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 315)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(160, 270, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, -30, 381, 281))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_y = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_y.setGeometry(QtCore.QRect(110, 80, 41, 22))
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_Pythagorize = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Pythagorize.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.pushButton_Pythagorize.setObjectName("pushButton_Pythagorize")
        self.lineEdit_x = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_x.setGeometry(QtCore.QRect(110, 40, 41, 22))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(70, 170, 121, 20))
        self.checkBox.setObjectName("checkBox")
        self.radioButton_x = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_x.setGeometry(QtCore.QRect(210, 40, 95, 20))
        self.radioButton_x.setChecked(True)
        self.radioButton_x.setObjectName("radioButton_x")
        self.radioButton_y = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_y.setGeometry(QtCore.QRect(210, 80, 95, 20))
        self.radioButton_y.setObjectName("radioButton_y")
        self.lineEdit_Answer = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Answer.setGeometry(QtCore.QRect(110, 120, 81, 22))
        self.lineEdit_Answer.setObjectName("lineEdit_Answer")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 55, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.radioButton_answer = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_answer.setGeometry(QtCore.QRect(210, 120, 121, 20))
        self.radioButton_answer.setObjectName("radioButton_answer")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(290, 170, 71, 16))
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_selected = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_selected.setGeometry(QtCore.QRect(230, 170, 51, 22))
        self.lineEdit_selected.setObjectName("lineEdit_selected")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "QT Demo 1"))
        self.pushButton_Exit.setText(_translate("Dialog", "Exit"))
        self.groupBox.setTitle(_translate("Dialog", "Input"))
        self.lineEdit_y.setText(_translate("Dialog", "4"))
        self.label.setText(_translate("Dialog", "X:"))
        self.pushButton_Pythagorize.setText(_translate("Dialog", "Pythagorize"))
        self.lineEdit_x.setText(_translate("Dialog", "3"))
        self.label_2.setText(_translate("Dialog", "Y:"))
        self.checkBox.setText(_translate("Dialog", "No Square Root"))
        self.radioButton_x.setText(_translate("Dialog", "X Selected"))
        self.radioButton_y.setText(_translate("Dialog", "Y Selected"))
        self.lineEdit_Answer.setText(_translate("Dialog", "5"))
        self.label_3.setText(_translate("Dialog", "Answer"))
        self.radioButton_answer.setText(_translate("Dialog", "Answer Selected"))
        self.label_4.setText(_translate("Dialog", "is selected"))
        self.lineEdit_selected.setText(_translate("Dialog", "X"))

