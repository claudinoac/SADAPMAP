from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import serial
import time
import sys
from CalibracaoP import Ui_MainWindow

class SerialManager(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyUSB0', 115200)  # Inicialização da Serial com baudrate 115200bps
        self.ser.setDTR(False)  # Reset do arduino para reinicio da leitura
        time.sleep(0.022)
        self.ser.setDTR(True)
        self.ser.readline()  # Primeiro valor da serial sai com lixo

    def read(self):
        if(self.ser.inWaiting()==0):
            pass
        return self.ser.readline()

class Graph(pyqtgraph.GraphicsLayout):

    index=1

    def __init__(self,x_range,y_range,x_size,y_size,color1,color2):
        super(Graph,self).__init__()
        self.x_range = x_range
        self.y_range = y_range
        self.x_size = x_size
        self.y_size = y_size
        self.color1 = color1
        self.color2 = color2

        self.p1 = self.addPlot()
        self.curve1 = self.p1.plot(pen=color1)
        self.curve2 = self.p1.plot(pen=color2)
        self.setPreferredSize(self.x_size,self.y_size)
        self.p1.setXRange(0,self.x_range,padding=0)
        self.p1.setYRange(0, self.y_range, padding=0)
        self.x1=[]
        self.y1=[]
        self.y2=[]

        #self.p1.enableAutoScale()

    def updateGraph(self,y1,y2):
        self.y1.append(y1)
        self.y2.append(y2)

        if len(self.y1)>self.x_range+1:
            del self.y1[0]
            del self.y2[0]
            self.index = self.x_range
        else:
            self.x1.append(self.index)
        self.index = self.index + 1

        self.curve1.setData(self.x1, self.y1)
        self.curve2.setData(self.x1,self.y2)




    def setGraphScale(self,x_range,y_range):
        self.x_range=x_range
        self.y_range=y_range
        self.x1=[]
        self.y1=[]
        self.y2=[]
        self.index=0
        self.clear()
        self.p1=self.addPlot()
        self.p1.setXRange(0, self.x_range, padding=0)
        self.p1.setYRange(0, self.y_range, padding=0)
        self.curve1=self.p1.plot(pen=self.color1)
        self.curve2=self.p1.plot(pen=self.color2)




class SystemEngine(object):

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.dialog = QtWidgets.QMainWindow()
        self.ser1 = SerialManager()
        self.uiCalibra1 = Ui_MainWindow()
        self.uiCalibra1.setupUi(self.dialog)
        self.layout = Graph(100, 10230, 900, 600, 'r','g')
        self.scene = QtGui.QGraphicsScene()
        self.scene.addItem(self.layout)
        self.uiCalibra1.sceneSelector(self.scene)
        self.dialog.showMaximized()
        self.prev_x_scale=100
        self.x_scale=100


    def updateData(self):

        readData = self.ser1.read()  # Lê o dado da serial
        readData = readData.decode('utf8')
        dado = readData.split(' ', 3)
        self.x_scale=int(self.uiCalibra1.f_max.text())
        if(self.x_scale != self.prev_x_scale):
            self.layout.setGraphScale(int(self.x_scale),32700)
        self.prev_x_scale = self.x_scale
        self.layout.updateGraph(float(dado[0]),float(dado[1]))

if __name__ == '__main__':

    engine=SystemEngine()
    timer = QtCore.QTimer()  #
    timer.timeout.connect(engine.updateData)  #
    timer.start(0)
    sys.exit(engine.app.exec_())
