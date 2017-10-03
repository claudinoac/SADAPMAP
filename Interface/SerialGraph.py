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

readData = [0]
y1=[]
x1=[]
tim=[]
dt=0
t=time.time()
indx = 0

def update():
    global curve1, indx, y1,x1,t,dt
    dt=time.time()-t
    while (ser.inWaiting() == 0):
        pass
    readData= float(ser.readline())
    print(readData)
    y1.append(readData)
    x1.append(dt)
    if indx>50:
       y1.pop(0)
       x1.pop(0)
       indx=0
    else:
       indx+=1

    curve1.setData(x1,y1)
    p1.setXRange(0, 100, padding=0)
    app.processEvents()

timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(0)




if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_'):
        QtGui.QApplication.instance().exec_()