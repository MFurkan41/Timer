# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frame.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(389, 456)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.BMO = QtWidgets.QLabel(self.centralwidget)
        self.BMO.setGeometry(QtCore.QRect(10, 0, 371, 451))
        self.BMO.setText("")
        self.BMO.setPixmap(QtGui.QPixmap(":/img/images/timer50resized.png"))
        self.BMO.setObjectName("BMO")
        self.blueLB = QtWidgets.QPushButton(self.centralwidget)
        self.blueLB.setGeometry(QtCore.QRect(133, 355, 25, 10))
        self.blueLB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.blueLB.setText("")
        self.blueLB.setDefault(False)
        self.blueLB.setFlat(True)
        self.blueLB.setObjectName("blueLB")
        self.blueRB = QtWidgets.QPushButton(self.centralwidget)
        self.blueRB.setGeometry(QtCore.QRect(167, 355, 25, 10))
        self.blueRB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.blueRB.setText("")
        self.blueRB.setFlat(True)
        self.blueRB.setObjectName("blueRB")
        self.minutesSpinBox = QtWidgets.QSpinBox()
        self.minutesSpinBox.setSingleStep(5)
        self.minutesSpinBox.setRange(0, 10**9)
        self.redB = QtWidgets.QPushButton(self.centralwidget)
        self.redB.setGeometry(QtCore.QRect(245, 325, 55, 45))
        self.redB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.redB.setText("")
        self.redB.setFlat(True)
        self.redB.setObjectName("redB")
        self.triB = QtWidgets.QPushButton(self.centralwidget)
        self.triB.setGeometry(QtCore.QRect(253, 280, 27, 25))
        self.triB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.triB.setText("")
        self.triB.setFlat(True)
        self.triB.setObjectName("triB")
        self.rightTB = QtWidgets.QPushButton(self.centralwidget)
        self.rightTB.setGeometry(QtCore.QRect(275, 226, 16, 16))
        self.rightTB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.rightTB.setText("")
        self.rightTB.setFlat(True)
        self.rightTB.setObjectName("rightTB")
        self.rightMB = QtWidgets.QPushButton(self.centralwidget)
        self.rightMB.setGeometry(QtCore.QRect(307, 297, 21, 16))
        self.rightMB.setStyleSheet("QPushButton { background-color: transparent; border: 0px }")
        self.rightMB.setText("")
        self.rightMB.setFlat(True)
        self.rightMB.setObjectName("rightMB")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(147, 80, 161, 81))
        QtGui.QFontDatabase.addApplicationFont("font.ttf")
        self.font = QtGui.QFont("Let's go Digital")
        self.font.setPointSize(50)
        self.label.setFont(self.font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "25:00"))
from gui import resources_rc