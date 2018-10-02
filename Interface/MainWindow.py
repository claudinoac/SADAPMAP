# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PressCalib import PressCalib
from TempCalib import TempCalib
from Process import Process
from SystemEngine import SystemEngine

class Ui_MainWindow(object):

    def __init__(self):

        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QMainWindow()
        self.setupUi(self.dialog)
        self.dialog.show()

        self.pressButton.pressed.connect(self.startPress)


    def startPress(self):
        self.dialog.close()
        self.ui = PressCalib()
        self.ui.setupUi(self.dialog)

        self.dialog.showMaximized()
        engine = SystemEngine(0,self.ui)



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(0, 0, 0);\n"
"color: rgb(255,255,255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 130, 741, 71))
        self.label.setStyleSheet("background-color:rgb(0,0,0);\n"
"font: 15pt \"Noto Serif\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 30, 141, 81))
        self.label_2.setStyleSheet("background-color:rgb(0,0,0);\n"
"font: 22pt \"Noto Serif\";")
        self.label_2.setObjectName("label_2")
        self.pressButton = QtWidgets.QToolButton(self.centralwidget)
        self.pressButton.setGeometry(QtCore.QRect(50, 300, 171, 51))
        self.pressButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"")
        self.pressButton.setObjectName("pressButton")
        self.tempButton = QtWidgets.QToolButton(self.centralwidget)
        self.tempButton.setGeometry(QtCore.QRect(310, 300, 181, 51))
        self.tempButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"")
        self.tempButton.setObjectName("tempButton")
        self.procButton = QtWidgets.QToolButton(self.centralwidget)
        self.procButton.setGeometry(QtCore.QRect(570, 300, 181, 51))
        self.procButton.setStyleSheet("background-color:rgb(53, 53, 53);")
        self.procButton.setObjectName("procButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 420, 151, 141))
        self.label_3.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"font: 15pt \"Noto Serif\";")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Resources/logo_pt.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(590, 420, 171, 141))
        self.label_4.setStyleSheet("background-color:rgb(0,0,0);\n"
"font: 15pt \"Noto Serif\";")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Resources/750px-Ufrgs.svg.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(260, 420, 281, 151))
        self.label_5.setStyleSheet("")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Resources/LogoCTA_2015_vetorial_cor.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADAPMAP"))
        self.label.setText(_translate("MainWindow", "   Sistema de Aquisição de Dados para Análise de Materiais em Altas Pressões"))
        self.label_2.setText(_translate("MainWindow", "SADAMAP"))
        self.pressButton.setText(_translate("MainWindow", "Calibração de Pressão"))
        self.tempButton.setText(_translate("MainWindow", "Calibração de Temperatura"))
        self.procButton.setText(_translate("MainWindow", "Processamento"))

