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
        self.ser1.startPort(str(self.ser1.portList[0].device), 115200)
        self.uiCalibra1 = Ui_MainWindow()
        self.uiCalibra1.setupUi(self.dialog)
        self.uiCalibra1.serialListPanel(self.ser1.portList)
        self.layout = Graph(100, 30000, 900, 500, 'r','g',"Força","Tensão no Calibrante")
        self.scene = QtGui.QGraphicsScene()
        self.scene.addItem(self.layout)
        self.uiCalibra1.sceneSelector(self.scene)
        self.dialog.showMaximized()
        self.prev_x_scale=100
        self.x_scale=100



    def updateData(self):

        if(self.uiCalibra1.usb[0].isChecked()==True):
            readData = self.ser1.read()  # Lê o dado da serial
            readData = readData.decode('utf8')
            dado = readData.split(' ', 3)
            try:
                self.x_scale=int(self.uiCalibra1.t_max.text())
            except ValueError:
                 self.x_scale=100

            if(self.x_scale != self.prev_x_scale):
                self.layout.setGraphScale(int(self.x_scale),32700)

            self.prev_x_scale = self.x_scale
            self.uiCalibra1.forcaLabel.setText(str(dado[0])+" Tonf")
            self.uiCalibra1.calibranteLabel.setText(str(dado[1].split()[0])+" mV")
            self.layout.updateGraph(float(dado[0]),float(dado[1]))

        else:
            pass