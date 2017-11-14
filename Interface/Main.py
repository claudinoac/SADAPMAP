from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import pyqtgraph
import serial
import serial.tools.list_ports
import time
import sys
from SerialManager import SerialManager
from CalibracaoP import Ui_MainWindow
from SystemEngine import SystemEngine
from Graph import Graph

if __name__ == '__main__':

    engine=SystemEngine()
    timer = QtCore.QTimer()  #
    timer.timeout.connect(engine.updateData)  #
    timer.start(0)
    sys.exit(engine.app.exec_())
