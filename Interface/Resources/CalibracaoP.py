# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalibracaoP.ui'
#
# Created: Mon Oct 30 15:48:28 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 695)
        MainWindow.setMinimumSize(QtCore.QSize(817, 0))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setAutoFillBackground(True)
        self.centralWidget.setObjectName("centralWidget")
        self.CentralGraph = QtWidgets.QGraphicsView(self.centralWidget)
        self.CentralGraph.setGeometry(QtCore.QRect(410, 30, 921, 571))
        self.CentralGraph.setObjectName("CentralGraph")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 30, 161, 121))
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setStyleSheet("QLabel { color: green}")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 57, 17))
        self.label.setObjectName("label")

        self.ForceDisp = QtWidgets.QLabel(self.centralWidget)
        self.ForceDisp.setGeometry(QtCore.QRect(60, 210, 57, 17))
        self.ForceDisp.setObjectName("ForceDisp")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 25))
        self.menuBar.setObjectName("menuBar")
        self.Menuzinho = QtWidgets.QMenu(self.menuBar)
        self.Menuzinho.setObjectName("Menuzinho")
        self.menuEtapa = QtWidgets.QMenu(self.menuBar)
        self.menuEtapa.setObjectName("menuEtapa")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.actionCalibra_o_P = QtWidgets.QAction(MainWindow)
        self.actionCalibra_o_P.setObjectName("actionCalibra_o_P")
        self.actionCalibra_o_T = QtWidgets.QAction(MainWindow)
        self.actionCalibra_o_T.setObjectName("actionCalibra_o_T")
        self.actionProcessamento = QtWidgets.QAction(MainWindow)
        self.actionProcessamento.setObjectName("actionProcessamento")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_Como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Como.setObjectName("actionSalvar_Como")
        self.actionSalvar_2 = QtWidgets.QAction(MainWindow)
        self.actionSalvar_2.setObjectName("actionSalvar_2")
        self.actionSalvar_Como_2 = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Como_2.setObjectName("actionSalvar_Como_2")
        self.Menuzinho.addAction(self.actionAbrir)
        self.Menuzinho.addAction(self.actionSalvar_2)
        self.Menuzinho.addAction(self.actionSalvar_Como_2)
        self.menuEtapa.addAction(self.actionCalibra_o_P)
        self.menuEtapa.addAction(self.actionCalibra_o_T)
        self.menuEtapa.addAction(self.actionProcessamento)
        self.menuBar.addAction(self.Menuzinho.menuAction())
        self.menuBar.addAction(self.menuEtapa.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADAMAP - Análise de Dados "))
        self.groupBox.setTitle(_translate("MainWindow", "Escalas"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.ForceDisp.setText(_translate("MainWindow", "TextLabel"))
        self.Menuzinho.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuEtapa.setTitle(_translate("MainWindow", "Etapa"))
        self.actionCalibra_o_P.setText(_translate("MainWindow", "Calibração P"))
        self.actionCalibra_o_T.setText(_translate("MainWindow", "Calibração T"))
        self.actionProcessamento.setText(_translate("MainWindow", "Processamento"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como"))
        self.actionSalvar_2.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_Como_2.setText(_translate("MainWindow", "Salvar Como"))

    def sceneSelector(self, scene):
        self.CentralGraph.setScene(scene)
        self.CentralGraph.setBackgroundBrush(QtCore.Qt.black)

