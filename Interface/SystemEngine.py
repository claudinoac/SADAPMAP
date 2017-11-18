from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import time
import sys
from SerialManager import SerialManager
from CalibracaoP import Ui_MainWindow
from Graph import Graph

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

        self.layout=pyqtgraph.GraphicsLayout()
        self.graph = Graph(100,0, 30000, 900, 600, 'r','g',"Força","Tensão no Calibrante")
        self.layout.addItem(self.graph)
        self.scene = QtGui.QGraphicsScene()
        self.scene.addItem(self.layout)
        self.uiCalibra1.sceneSelector(self.scene)
        self.dialog.showMaximized()
        self.prev_x_scale=100
        self.x_scale=100

        self.uiCalibra1.t_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.f_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.f_min.returnPressed.connect(self.updateScale)
        self.uiCalibra1.p_max.returnPressed.connect(self.updateScale)
        self.uiCalibra1.p_min.returnPressed.connect(self.updateScale)

        self.uiCalibra1.amostragemCBox.currentIndexChanged.connect(self.updateTimer)
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
                self.uiCalibra1.forcaLabel.setText(str(dado[0])+" Tonf")
                self.uiCalibra1.calibranteLabel.setText(str(dado[1].split()[0])+" mV")
            except IndexError:
                print("Erro no Indice do Array Enviado pela Serial")

            try:
                self.graph.updateGraph(float(dado[0]),float(dado[1]))
            except ValueError:
                print("Erro nos Valores do Array Enviado pela Serial")

        else:
            pass
        self.timeant=time.time()

    def updateScale(self):
        try:
            self.x_scale = int(self.uiCalibra1.t_max.text())
            self.y_min = int(self.uiCalibra1.f_min.text())
            self.y_max   = int(self.uiCalibra1.f_max.text())
        except ValueError:
            self.x_scale = 100
            self.y_min = 0
            self.y_max = 32700
            print("Erro!: Campos de Escala Vazios")

        if(self.x_scale=="0"):
            self.x_scale="1"

        self.layout.clear()
        self.graph = self.graph = Graph(self.x_scale, self.y_min , self.y_max, 900, 600, 'r', 'g', "Força", "Tensão no Calibrante")
        self.layout.addItem(self.graph)
        self.scene.focusItem()

    def updateTimer(self):
        self.time=self.uiCalibra1.amostragemCBox.currentText().split(" ")
        self.time[0]=int(self.time[0])
        print(self.time[0])
        if(self.time[0]<100):
            self.time[0]=1000*self.time[0]

        self.timer.stop()
        self.timer.start(self.time[0])
