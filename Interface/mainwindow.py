from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 460)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.CentralGraph = QtWidgets.QGraphicsView(self.centralWidget)
        self.CentralGraph.setGeometry(QtCore.QRect(160, 20, 481, 361))
        self.CentralGraph.setObjectName("CentralGraph")
        self.ForceDisp = QtWidgets.QLabel(self.centralWidget)
        self.ForceDisp.setGeometry(QtCore.QRect(60, 200, 57, 17))
        self.ForceDisp.setObjectName("ForceDisp")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 703, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuXuxuzinho = QtWidgets.QMenu(self.menuBar)
        self.menuXuxuzinho.setObjectName("menuXuxuzinho")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menuXuxuzinho.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADAM - Análise de Dados"))
        self.ForceDisp.setText(_translate("MainWindow", "TextLabel"))
        self.menuXuxuzinho.setTitle(_translate("MainWindow", "Arquivo"))

    def sceneSelector(self,scene):
        self.CentralGraph.setScene(scene)
