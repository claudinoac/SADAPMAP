from PyQt5 import QtGui, QtCore, QtWidgets       #importação de classes
import pyqtgraph as pg
import serial
import time
from CalibracaoP import Ui_MainWindow

ser = serial.Serial('/dev/ttyUSB0', 115200)  #Inicialização da Serial com baudrate 115200bps
ser.setDTR(False)                            #Reset do arduino para reinicio da leitura
time.sleep(0.022)
ser.setDTR(True)

ser.readline()                              #Primeiro valor da serial sai com lixo

app = QtGui.QApplication([])
pg.setConfigOption('foreground', 'c')
window=Ui_MainWindow()
dialog = QtWidgets.QMainWindow()
window.setupUi(dialog)
layout = pg.GraphicsLayout()
scene=QtGui.QGraphicsScene()

window.sceneSelector(scene)

scene.addItem(layout)
p1 = layout.addPlot()
p1.showGrid(True,True)
p1.addLegend()
curve1 = p1.plot(pen='r',name="Sensor 1")
curve2 = p1.plot(pen='g',name="Sensor 2")
curve3 = p1.plot(pen='w',name="Sensor 3")
curve4 = p1.plot(pen='y',name="Sensor 4")
curve5 = p1.plot(pen='b',name="Sensor 5")
curve6 = p1.plot(pen='m',name="Sensor 6")
curve7 = p1.plot(pen='c',name="Sensor 7")
curve8 = p1.plot(name="Sensor 8")

#window.CentralGraph.setFixedSize(690,550)
layout.setPreferredSize(900,550)
y1 = []                                     #Inicialização da lista dinâmica dos valores de y
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []
y7 = []
y8 = []
x1 = []                                     #Inicialização da lista dinâmica dos valores de x
x_max = 200                                  #Variável que define o tamanho do eixo
indx = 0                                    #Variável auxiliar de contagem

p1.setYRange(0, 5, padding=0)              #Define os limites do gráfico
p1.setXRange(0, x_max, padding=0)
p1.setLabel("bottom","Tempo",'s')
p1.setLabel("left","Força",'Tonf')
p1.setLabel("right","Tensão no Calibrante",'V')

dialog.showMaximized()




def update():                               #Método para atualizar os arrays com valores de x, y e atualizar o gráfico
    global curve1,curve2, indx, y1, x1, ser #Dá acesso das variáveis globais à função
    while (ser.inWaiting() == 0):           #Aguarda a serial liberar dado
        pass
    readData = ser.readline()       #Lê o dado da serial
    readData=readData.decode('utf8')
    dado=readData.split(' ',8)
    print(dado[3])
    y1.append(float(dado[0])*5/32767)                     #Armazena o dado na lista do eixo y
    y2.append(float(dado[1])*5/32767)
    y3.append(float(dado[2])*5/32767)
    y4.append(float(dado[3])*5/32767)
    y5.append(float(dado[4])*5/32767)
    y6.append(float(dado[5])*5/32767)
    y7.append(float(dado[6])*5/32767)
    y8.append(float(dado[7])*5/32767)

    indx += 1                               #Adiciona um na variavel auxiliar
    if len(y1) > x_max-1:                   #Verifica se foi excedido o tamanho máximo do eixo x para o array
        del y1[0]                           #Caso sim, libera o valor da primeira posição para manter o array, e consequentemente o gráfico, com escala constante
        del y2[0]
        del y3[0]
        del y4[0]
        del y5[0]
        del y6[0]
        del y7[0]
        del y8[0]
        indx = x_max                        #impede indx de divergir
    else:
        x1.append(indx)                     #Vai adicionando valores de 0 a x_max no eixo x até que a lista x lote e tenha mesmo tamanho da lista y
    window.forcaLabel.setText(dado[0])
    window.calibranteLabel.setText(dado[1])
    curve1.setData(x1,y1)                   #Atualiza os dados da curva
    curve2.setData(x1,y2)
    curve3.setData(x1,y3)
    curve4.setData(x1,y4)
    curve5.setData(x1, y5)
    curve6.setData(x1, y6)
    curve7.setData(x1, y7)
    curve8.setData(x1, y8)


    #app.processEvents()                     #

timer = QtCore.QTimer()                     #
timer.timeout.connect(update)               #
timer.start(0)                              #


if __name__ == '__main__':                  #
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_'):   #
        QtGui.QApplication.instance().exec_()
