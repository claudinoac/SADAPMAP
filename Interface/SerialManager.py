import serial
import serial.tools.list_ports
import time
from PyQt5 import QtWidgets

class SerialManager(object):

    def __init__(self):
        self.portList = serial.tools.list_ports.comports()
        self.portNum=len(self.portList)
        for i in range (0,self.portNum):
            print(self.portList[i].device)

    def startPort(self,port,baud):
        self.ser = serial.Serial(port, baud)  # Inicialização da Serial com baudrate 115200bps
        self.ser.setDTR(False)  # Reset do arduino para reinicio da leitura
        time.sleep(0.022)
        self.ser.setDTR(True)
        self.ser.readline()  # Primeiro valor da serial sai com lixo

    def read(self):
        if(self.ser.inWaiting()==0):
            pass
        self.ser.flushInput()
        return self.ser.readline()

    def serialListPanel(self, uiWindow):
        uiWindow.usb = []
        for i in range(0, len(self.portList)):
            uiWindow.usb.append(QtWidgets.QAction(uiWindow.MainWindow))
            uiWindow.usb[i].setText(self.portList[i].device)
            uiWindow.usb[i].setCheckable(True)
            uiWindow.serialMenu.addAction(uiWindow.usb[i])