from PyQt5 import QtCore,QtGui,QtWidgets  # importação de classes
import time
import sys
from SystemEngine import SystemEngine

if __name__ == '__main__':


    engine=SystemEngine()
    timer = QtCore.QTimer()  #
    timer.timeout.connect(engine.updateData)  #
    timer.start(0)
    sys.exit(engine.app.exec_())
