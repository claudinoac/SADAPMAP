# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      Classe SerialManager                                                                                 #
#      Autor: Alisson Claudino (alisson.claudino@ufrgs.br) -> https://lief.if.ufrgs.br/~itsalissom          #
#      Licença: GNU GPLv2                                                                                   #
#      Propósito: Estabelecer comunicação com o hardware do sistema, adquirindo as medidas brutas           #
#      dos sensores                                                                                         #
#                                                                                                           #
#                                                                                                           #
# Observações:                                                                                              #
#                                                                                                           #
#       O construtor da classe obtém a lista de portas seriais disponíveis e armazena em um array para      #
#   possibilitar que o usuário escolha qual porta utilizar.                                                 #
#       O buffer de entrada é limpado a cada leitura para que a leitura realizada seja de tempo real        #
#   independente da amostragem. Caso não fosse limpo, valores anteriores iriam interferir nas               #
#   medidas (oversampling).                                                                                 #
#                                                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

#Importação de bibliotecas
import serial
import serial.tools.list_ports
import time
from PyQt5 import QtWidgets

class SerialManager(object):

    def __init__(self): #Construtor da classe
        self.portList = serial.tools.list_ports.comports() #Armazena a lista de portas em um array

        self.portNum=len(self.portList) #Imprime no stdout a lista de portas disponíveis
        for i in range (0,self.portNum):
            print(self.portList[i].device)

    def startPort(self,port,baud):  #Inicializador da conexão com a porta e baudrate definidos
        self.ser = serial.Serial(port, baud)
        self.ser.setDTR(False)  # Reset do arduino para reinicio da leitura
        time.sleep(0.022)
        self.ser.setDTR(True)
        self.ser.readline()  # Primeiro valor da serial sai com lixo

    def read(self): #Função para realizar a leitura do valor atual na serial.
        if(self.ser.inWaiting()==0):
            pass
        self.ser.flushInput()      #Limpeza do buffer de entrada
        return self.ser.readline()  #Leitura de todos os valores em uma linha

    def serialListPanel(self, uiWindow): #Função para disponibilizar a lista de portas na interface
        uiWindow.usb = []
        for i in range(0, len(self.portList)): #As portas vão sendo adicionadas uma a uma
            uiWindow.usb.append(QtWidgets.QAction(uiWindow.MainWindow))
            uiWindow.usb[i].setText(self.portList[i].device)
            uiWindow.usb[i].setCheckable(True)
            uiWindow.serialMenu.addAction(uiWindow.usb[i])
