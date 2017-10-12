from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import serial
import time
import sys
from mainwindow import Ui_MainWindow


class GUI(Ui_MainWindow):
    def __init__(self, dialog):
        Ui_MainWindow.__init__(self)
        self.setupUi(dialog)

class SerialManager(object):
    def __init__(self):
        self.ser = serial.Serial('/dev/ttyACM0', 115200)  # Inicialização da Serial com baudrate 115200bps
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

        self.x_range = x_range
        self.y_range = y_range
        self.x_size = x_size
        self.y_size = y_size

        self.p1 = self.addPlot()
        self.curve1 = p1.plot(pen=color)
        self.setPreferredSize(x_size,y_size)
        self.p1.setXRange(0,x_range,padding=0)
        self.p1.setYRange(0, y_range, padding=0)
        self.x1=[]
        self.y1=[]



    def updateGraph(self,value):
        y1.append(value)
        index += 1
        if len(y1)>x_range-1:
            del y1[0]
            self.index = x_range
        else:
            x1.append(index)

        self.curve1.setData(x1,y1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()

    prog = GUI(dialog)

    dialog.show()
    sys.exit(app.exec_())
