import matplotlib.pyplot as plt
import numpy as np
import time
import serial #importacao do modulo serial
import random
leitura =[]
fig, ax = plt.subplots()
ser = serial.Serial('COM6') #abre porta serial COM6 

contador = 0
eixo_x = 50
while True:
    while (ser.inWaiting()==0):    
     pass
    dados  =int( ser.readline()[:-1])    #firmware deve ter um delay de pelo menos 100ms entre cada envio
    print dados
    ax.clear()
    ax.set_xlim([0,eixo_x])   #faixa do eixo horizontal
    ax.set_ylim([0,1023]) # faixa do eixo vertical   
    #leitura.append(random.randint(0,1023))  #teste com numeros aleatorios
    leitura.append(dados)  
   
    ax.plot(leitura)
    plt.pause(.000001)     
    contador = contador + 1
    if (contador > eixo_x):
	   leitura.pop(0)

ser.close()
