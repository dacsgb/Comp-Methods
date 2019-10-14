# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QT_demo1_simple.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(299, 274)
        self.pushButton_Exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_Exit.setGeometry(QtCore.QRect(80, 190, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, -30, 231, 221))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_y = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_y.setGeometry(QtCore.QRect(110, 80, 41, 22))
        self.lineEdit_y.setObjectName("lineEdit_y")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 55, 16))
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.pushButton_Pythagorize = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_Pythagorize.setGeometry(QtCore.QRect(100, 170, 93, 28))
        self.pushButton_Pythagorize.setObjectName("pushButton_Pythagorize")
        self.lineEdit_x = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_x.setGeometry(QtCore.QRect(110, 40, 41, 22))
        self.lineEdit_x.setObjectName("lineEdit_x")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 55, 16))
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.lineEdit_Answer = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_Answer.setGeometry(QtCore.QRect(110, 120, 81, 22))
        self.lineEdit_Answer.setObjectName("lineEdit_Answer")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 55, 16))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")

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
        self.lineEdit_Answer.setText(_translate("Dialog", "5"))
        self.label_3.setText(_translate("Dialog", "Answer"))

