from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import serial
import time
import sys
from mainwindow import Ui_MainWindow

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
        return self.ser.read()

class Graph(pyqtgraph.GraphicsLayout):

    index=0

    def __init__(self,x_range,y_range,x_size,y_size,color):
        super(Graph,self).__init__()
        self.x_range = x_range
        self.y_range = y_range
        self.x_size = x_size
        self.y_size = y_size

        self.p1 = self.addPlot()
        self.curve1 = self.p1.plot(pen=color)
        self.setPreferredSize(x_size,y_size)
        self.p1.setXRange(0,x_range,padding=0)
        self.p1.setYRange(0, y_range, padding=0)
        self.x1=[]
        self.y1=[]

    def updateGraph(self,value):
        self.y1.append(value)
        self.index += 1
        if len(self.y1)>self.x_range-1:
            del self.y1[0]
            self.index = self.x_range
        else:
            self.x1.append(index)

        self.curve1.setData(self.x1, self.y1)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    ser1 = SerialManager()
    uiCalibra1=Ui_MainWindow()
    uiCalibra1.setupUi(dialog)
    layout = Graph(0,100,0,1023,'r')
    scene = QtGui.QGraphicsScene()

    scene.addItem(layout)
    uiCalibra1.sceneSelector(scene)



    timer = QtCore.QTimer()  #
    timer.timeout.connect(layout.update(ser1.read()))  #
    timer.start(0)

    dialog.showMaximized()
    sys.exit(app.exec_())
