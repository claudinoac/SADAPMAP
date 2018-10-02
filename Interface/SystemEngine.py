# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      Classe SystemEngine                                                                                  #
#      Autor: Alisson Claudino (alisson.claudino@ufrgs.br) -> https://lief.if.ufrgs.br/~itsalissom          #
#      Licença: GNU GPLv2                                                                                   #
#      Propósito: Gerenciar o funcionamento geral do programa, realizando as conexões entre todas as        #
#      classes do sistema.                                                                                  #
#                                                                                                           #                                                                                                          #
# Observações:                                                                                              #
#                                                                                                           #
#                                                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #



# importação de classes
import time
import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from pyqtgraph import GraphicsLayout
from SerialManager import SerialManager
from PressCalib import PressCalib
from TempCalib import TempCalib
from Process import Process
from Graph import Graph


class SystemEngine(object):

    def __init__(self, interType,ui): #Construtor da classe
        self.timer=QtCore.QTimer()
        self.ui=ui
        self.ser1 = SerialManager()
        self.ser1.startPort(str(self.ser1.portList[1].device), 115200)




        self.ser1.serialListPanel(self.ui)



        self.x_scale=10
        self.nCurves = 2
        self.y_min=[0,0]
        self.y_max=[32700,10000]


        self.color = ['r','g']
        self.name = ["Força","Tensão no Calibrante"]
        self.unit = ["Tonf","mV"]

        self.layout=GraphicsLayout()

        self.updateTimer()
        self.graph = Graph(self.time[0]/1000,self.x_scale,self.nCurves, self.y_min, self.y_max, 800, 500, self.color,self.name,self.unit)

        self.layout.addItem(self.graph.axis[0],row=1,col=1,rowspan=1,colspan=1)
        for n in range(1,self.nCurves):
            self.layout.addItem(self.graph.axis[n],row=1,col=n+2,rowspan=1,colspan=1)

        self.layout.addItem(self.graph,row=1,col=2,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axisTime,row=2,col=2,rowspan=1,colspan=1)
        self.layout.setMinimumSize(500, 600)
        self.layout.setMaximumSize(500,600)





        self.scene = QtGui.QGraphicsScene()

        self.scene.addItem(self.layout)



        #self.layout.setMaximumSize(770,550)
        self.scene.focusItem()

        self.sceneSelector(self.scene)

        self.ui.menuPlay_Pause = QtWidgets.QAction(self.ui.MainWindow)
        self.ui.menuPlay_Pause.setText("Play")
        self.ui.menuPlay_Pause.setObjectName("menuPlay_Pause")

        self.ui.menuBar.addAction(self.ui.menuPlay_Pause)
        self.ui.menuPlay_Pause.setCheckable(True)

        self.ui.menuPlay_Pause.triggered.connect(self.playPauseButtonAnimation)

        self.ui.linkActions()





        self.ui.t_max.returnPressed.connect(self.updateScale)
        self.ui.f_max.returnPressed.connect(self.updateScale)
        self.ui.f_min.returnPressed.connect(self.updateScale)
        self.ui.p_max.returnPressed.connect(self.updateScale)
        self.ui.p_min.returnPressed.connect(self.updateScale)

        self.ui.samplingCBox.currentIndexChanged.connect(self.updateTimer)
        self.timeant=time.time()
        self.timer.timeout.connect(self.updateData)

        thread_instance = QtCore.QThread()
        thread_instance.start()
        thread_instance.exec_()
        self.timer.start(100)

    def playPauseButtonAnimation(self):
        if (self.ui.menuPlay_Pause.text() == "Play"):
            self.ui.menuPlay_Pause.setText("Pause")
            self.ui.startTimeLabel.setText(self.ui.currentTimeLabel.text())
        else:
            self.ui.menuPlay_Pause.setText("Play")

    def sceneSelector(self, scene):
        self.ui.CentralGraph.setScene(scene)
        self.ui.CentralGraph.setBackgroundBrush(QtCore.Qt.black)
        self.ui.CentralGraph.setInteractive(False)

    def updateData(self):
        #print(time.time()-self.timeant)
        if(self.ui.menuPlay_Pause.isChecked()==True):
            readData = self.ser1.read()  # Lê o dado da serial
            readData = readData.decode('utf8')
            dado = readData.split(' ', self.nCurves+1)

            dado[len(dado)-1]=dado[len(dado)-1].split('\n',2)[0]
            try:
                self.ui.forceLabel.setText(str(dado[0])+" Tonf")
                self.ui.calibratorLabel.setText(str(dado[1].split()[0])+" mV")
                pass
            except IndexError:
                print("Erro no Indice do Array Enviado pela Serial")
            try:
                self.graph.updateGraph(dado)

            except IndexError:
                print("Erro: Array inválido")
                print(dado)


        else:
            pass
        self.timeant=time.time()

    def updateScale(self):
        try:
            self.x_scale = int(self.ui.t_max.text())
            self.y_min[0] = int(self.ui.f_min.text())
            self.y_max[0]   = int(self.ui.f_max.text())
            self.y_min[1] = int(self.ui.p_min.text())
            self.y_max[1] = int(self.ui.p_max.text())
        except ValueError:
            self.x_scale = 100
            self.y_min[0] = 0
            self.y_max[0] = 32700
            self.y_min[0] = 0
            self.y_max[0] = 10000
            print("Erro!: Campos de Escala Vazios")

        if(self.x_scale=="0"):
            self.x_scale="1"

        self.layout.clear()
        self.graph = Graph(self.time[0] / 1000, self.x_scale, self.nCurves, self.y_min, self.y_max, 800, 500,self.color, self.name, self.unit)
        self.layout.addItem(self.graph.axis[1],row=1,col=3,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axis[0],row=1,col=1,rowspan=1,colspan=1)
        self.layout.addItem(self.graph.axisTime,row=2,col=2,rowspan=1,colspan=1)
        self.layout.addItem(self.graph,row=1,col=2,rowspan=1,colspan=1)
        self.scene.focusItem()

    def updateTimer(self):
        self.time=self.ui.samplingCBox.currentText().split(" ")
        self.time[0]=int(self.time[0])
        print(self.time[0])
        if(self.time[0]<100):
            self.time[0]=1000*self.time[0]

        self.timer.stop()
        self.timer.start(self.time[0])
