from pyqtgraph.Qt import QtGui, QtCore       #importação de classes
import pyqtgraph as pg
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 115200)  #Inicialização da Serial com baudrate 115200bps
ser.setDTR(False)                            #Reset do arduino para reinicio da leitura
time.sleep(0.022)
ser.setDTR(True)

ser.readline()                              #Primeiro valor da serial sai com lixo

app = QtGui.QApplication([])
layout = pg.GraphicsLayout()
scene=QtGui.QGraphicsScene()
view=QtGui.QGraphicsView(scene)
scene.addItem(layout)
p1 = layout.addPlot()
curve1 = p1.plot(pen='r')
view.show()
view.setFixedSize(690,550)
layout.setPreferredSize(640,500)
y1 = []                                     #Inicialização da lista dinâmica dos valores de y
x1 = []                                     #Inicialização da lista dinâmica dos valores de x
x_max = 100                                  #Variável que define o tamanho do eixo
indx = 0                                    #Variável auxiliar de contagem

p1.setYRange(0, 1023, padding=0)        #Define os limites do gráfico
p1.setXRange(0, x_max, padding=0)



def update():                               #Método para atualizar os arrays com valores de x, y e atualizar o gráfico
    global curve1, indx, y1, x1, ser        #Dá acesso das variáveis globais à função
    while (ser.inWaiting() == 0):           #Aguarda a serial liberar dado
        pass
    readData = float(ser.readline())        #Lê o dado da serial
    y1.append(readData)                     #Armazena o dado na lista do eixo y
    indx += 1                               #Adiciona um na variavel auxiliar
    if len(y1) > x_max-1:                   #Verifica se foi excedido o tamanho máximo do eixo x para o array
        del y1[0]                           #Caso sim, libera o valor da primeira posição para manter o array, e consequentemente o gráfico, com escala constante
        indx = x_max                        #impede indx de divergir
    else:
        x1.append(indx)                     #Vai adicionando valores de 0 a x_max no eixo x até que a lista x lote e tenha mesmo tamanho da lista y

    curve1.setData(x1, y1)                  #Atualiza os dados da curva


    #app.processEvents()                     #

timer = QtCore.QTimer()                     #
timer.timeout.connect(update)               #
timer.start(0)                              #


if __name__ == '__main__':                  #
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_'):   #
        QtGui.QApplication.instance().exec_()                          #