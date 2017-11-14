from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import serial
import serial.tools.list_ports
import time
import sys
from SerialManager import SerialManager
from CalibracaoP import Ui_MainWindow
from Graph import Graph

class SystemEngine(object):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QMainWindow()
        self.ser1 = SerialManager()
        print(self.ser1.portList[0])
        self.ser1.startPort(str(self.ser1.portList[1].device),115200)
        self.uiCalibra1 = Ui_MainWindow()
        self.uiCalibra1.setupUi(self.dialog)
        self.uiCalibra1.serialListPanel(self.ser1.portList)
        self.layout = Graph(100, 37500, 900, 600, 'r','g')
        self.scene = QtGui.QGraphicsScene()
        self.scene.addItem(self.layout)
        self.uiCalibra1.sceneSelector(self.scene)
        self.dialog.showMaximized()
        self.prev_x_scale=100
        self.x_scale=100


    def updateData(self):

        readData = self.ser1.read()  # Lê o dado da serial
        readData = readData.decode('utf8')
        dado = readData.split(' ', 8)
        self.x_scale=int(self.uiCalibra1.t_max.text())
        if(self.x_scale != self.prev_x_scale):
            self.layout.setGraphScale(int(self.x_scale),32700)
        self.prev_x_scale = self.x_scale
        self.layout.updateGraph(float(dado[0]),float(dado[1]))