from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import time
import numpy as np
import serial

ser=serial.Serial('/dev/ttyUSB0',115200)
app = QtGui.QApplication([])
win = pg.GraphicsWindow()
p1 = win.addPlot()
curve1 = p1.plot()

y1=[]
x1=[]
indx = 0


def update():
    global curve1, indx, y1,x1
    while (ser.inWaiting() == 0):
        pass
    readData= float(ser.readline())
    y1.append(readData)
    print(readData)
    indx+=1
    if len(y1)>99:
       del y1[0]
       indx=100
    else:
        x1.append(indx)

    curve1.setData(x1,y1)
    p1.setXRange(0, 100, padding=0)
    p1.setYRange(0,1023,padding=0)
    app.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)




if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_'):
        QtGui.QApplication.instance().exec_()