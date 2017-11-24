  # importação de classes
import time
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from pyqtgraph import GraphicsLayout
from SerialManager import SerialManager
from CalibracaoP import Ui_MainWindow
from Graph import Graph
import numpy as np
from math import sin,log

class SystemEngine(object):

    def __init__(self):
        self.timer=QtCore.QTimer()
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QMainWindow()
        self.ser1 = SerialManager()
        self.ser1.startPort(str(self.ser1.portList[0].device), 115200)
        self.uiCalibra1 = Ui_MainWindow()
        self.uiCalibra1.setupUi(self.dialog)
        self.uiCalibra1.serialListPanel(self.ser1.portList)

        self.prev_x_scale=100
        self.x_scale=100
        self.y1_min=0
        self.y1_max=32700
        self.y2_min=0
        self.y2_max=10000
        self.layout=GraphicsLayout()

        self.updateTimer()
        self.graph = Graph(self.time[0]/1000,self.x_scale, self.y1_min, self.y1_max, self.y2_min, self.y2_max, 800, 500, 'r', 'g', "Força", "Tensão no Calibrante")

        self.layout.addItem(self.graph.axis2,row=1,col=3,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axis1,row=1,col=1,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axisTime,row=2,col=2,rowspan=1,colspan=1)
        self.layout.addItem(self.graph,row=1,col=2,rowspan=1,colspan=1)
        self.layout.setMinimumSize(500, 600)
        self.layout.setMaximumSize(500,600)





        self.scene = QtGui.QGraphicsScene()

        self.scene.addItem(self.layout)



        #self.layout.setMaximumSize(770,550)
        self.scene.focusItem()

        self.uiCalibra1.sceneSelector(self.scene)
        self.dialog.showMaximized()


        self.uiCalibra1.t_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.f_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.f_min.returnPressed.connect(self.updateScale)
        self.uiCalibra1.p_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.p_min.returnPressed.connect(self.updateScale)

        self.uiCalibra1.samplingCBox.currentIndexChanged.connect(self.updateTimer)
        self.timeant=time.time()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(100)


    def updateData(self):
        #print(time.time()-self.timeant)
        if(self.uiCalibra1.menuPlay_Pause.isChecked()==True):
            readData = self.ser1.read()  # Lê o dado da serial
            readData = readData.decode('utf8')
            dado = readData.split(' ', 3)
            try:
                self.uiCalibra1.forceLabel.setText(str(dado[0])+" Tonf")
                self.uiCalibra1.calibratorLabel.setText(str(dado[1].split()[0])+" mV")
            except IndexError:
                print("Erro no Indice do Array Enviado pela Serial")

            try:
                self.graph.updateGraph(float(dado[0]),float(dado[1]))
            except ValueError:
                print("Erro nos Valores do Array Enviado pela Serial")
            except IndexError:
                print("Erro: Array inválido")
                print(dado)

        else:
            pass
        self.timeant=time.time()

    def updateScale(self):
        try:
            self.x_scale = int(self.uiCalibra1.t_max.text())
            self.y1_min = int(self.uiCalibra1.f_min.text())
            self.y1_max   = int(self.uiCalibra1.f_max.text())
            self.y2_min = int(self.uiCalibra1.p_min.text())
            self.y2_max = int(self.uiCalibra1.p_max.text())
        except ValueError:
            self.x_scale = 100
            self.y1_min = 0
            self.y1_max = 32700
            self.y2_min = 0
            self.y2_max = 10000
            print("Erro!: Campos de Escala Vazios")

        if(self.x_scale=="0"):
            self.x_scale="1"

        self.layout.clear()
        self.graph = Graph(self.time[0]/1000,self.x_scale, self.y1_min, self.y1_max, self.y2_min, self.y2_max, 770, 550, 'r', 'g', "Força", "Tensão no Calibrante")
        self.layout.addItem(self.graph.axis2,row=1,col=3,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axis1,row=1,col=1,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axisTime,row=2,col=2,rowspan=1,colspan=1)
        self.layout.addItem(self.graph,row=1,col=2,rowspan=1,colspan=1)
        self.scene.focusItem()

    def updateTimer(self):
        self.time=self.uiCalibra1.samplingCBox.currentText().split(" ")
        self.time[0]=int(self.time[0])
        print(self.time[0])
        if(self.time[0]<100):
            self.time[0]=1000*self.time[0]

        self.timer.stop()
        self.timer.start(self.time[0])
