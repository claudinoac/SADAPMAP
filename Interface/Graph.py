from pyqtgraph import PlotItem,AxisItem
import numpy as np

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#      Classe Graph baseada em pyqtgraph                                                                    #
#      Autor: Alisson Claudino de Jesus  (alisson.claudino@ufrgs.br)                                        #
#      Licença: GNU GPLv2                                                                                   #
#      Propósito: Gerar gráficos de tempo real com diversas curvas                                          #
#                                                                                                           #
#                                                                                                           #
# Observações:                                                                                              #
#   Os parâmetros iniciais dados são: taxa de amostragem (em segundos), escala de tempo (float),            #
#   numero de eixos (int),valores de escala y_min e y_max (arrays de float), dimensões do gráfico (int,int) #
#   cores das curvas (array de char), nomes das curvas (array de strings). e unidades das curvas (array de  #
#   string)                                                                                                 #
#                                                                                                           #
#   Para a função updateData, é dado um array de float de mesmo tamanho que o número de curvas para que     #
#   todas possam ser atualizadas corretamente                                                               #
#                                                                                                           #
#   O atributo index é utilizado para controle do tamanho dos vetores com valores de x e y de gráfico       #
#                                                                                                           #
#   x_range e x_sampling são os valores para visualização do eixo x e amostragem. Eles definem o tamanho    #
#   que os arrays devem ter para ter uma correta sincronia da visualização de gráfico e da amostragem.      #
#                                                                                                           #
#   Os arrays precisam manter-se com os mesmos tamanhos, e devem ter tamanhos limitados para não            #
#   consumir muita memória.                                                                                 #
#                                                                                                           #
#   Como para ambas as curvas pode ser setada somente uma escala, para fazer com que cada uma possua        #
#   sua própria escala, o plot tem uma escala definida pelo maior e menor valor de escala das curvas        #
#   e então cada valor dado possui um offset e um fator de correção para correta visualização dos dados     #
#   na tela.                                                                                                #
#                                                                                                           #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


class Graph(PlotItem):      #Herança de pyqtgraph.PlotItem

    index = 0           #Valor de índice para controle de tamanho dos arrays
    offset = []         #Array com valores de offset para correta visualização das curvas
    correctFactor = []  #Array com valores de fator de correção para correta visualização das curvas

    def __init__(self,x_sampling, x_range, n_axis, y_min, y_max, x_size, y_size, color, name,unit):  #Construtor da classe
        super(Graph, self).__init__()  #Instanciamento do construtor da classe mãe

        for n in range(0,n_axis):
            self.offset.append(min(y_min)-y_min[n])
            self.correctFactor.append((max(y_max)+min(y_min))/(y_max[n]-y_min[n]))

        self.x_range = x_range/x_sampling  #Correção de escala coerente com a amostragem
        self.curve = []                    #Declaração do array de curvas
        self.axis = []                     #Declaração do array de eixos
        self.y=[]                          #Declaração da matriz de valores das curvas

        self.curve.append(self.plot(pen=color[0], name=name[0]))  #Plotagem da primeira curva
        self.axis.append(AxisItem("left",color[0]))               #Primeiro eixo fica à esquerda do gráfico
        self.axis[0].setLabel(name[0], unit[0])                   #Configuração do primeiro eixo com seu nome e sua respectiva unidade
        self.axis[0].setRange(y_min[0], y_max[0])                 #Configuração do primeiro eixo com seu respectivo range
        y_axis = np.array([])                                     #Plotagem de array vazio para base do array de valores de y
        self.y.append(y_axis)                                     #Adição dos array de valores da primeira curva vazio



        for n in range(1,n_axis): #Repetição do ultimo grupo de comandos, porém aplicando-se a todos os eixos e curvas consecutivos
            self.curve.append(self.plot(pen=color[n], name=name[n]))
            self.axis.append(AxisItem("right",color[n]))
            self.axis[n].setLabel(name[n],unit[n])
            self.axis[n].setRange(y_min[n],y_max[n])
            self.y.append(y_axis)

        self.axisTime = AxisItem("bottom", 'w')     #Declaração do eixo de tempo
        self.axisTime.setLabel("Tempo", 's')        #Configuração do eixo de tempo com seu nome e unidade
        self.axisTime.setRange(0, x_range)          #Configuração da escala do eixo de tempo
        self.setXRange(0, self.x_range, padding=0)  #Configuração da escala de tempo no gráfico
        self.x=[]                               #Declaração do array de valores de tempo vazio

        self.showAxis("left", False)            #Desativação dos eixos convencionais do gráfico
        self.showAxis("bottom", False)
        self.setMinimumSize(x_size, y_size)     #Fixação do tamanho do gráfico

        self.setYRange(min(y_min), max(y_max), padding=0)   #Configuração da escala Y real do gráfico (Cada curva deve se adequar à sua respectiva escala)


    def updateGraph(self, y):

        for n in range(0,len(y)):
            self.y[n]=np.append(self.y[n],(float(y[n])+self.offset[n])*self.correctFactor[n])    #Cada valor contido no array y vai para seu respectivo array com sua respectiva escala
            print(float(y[n]))

        if len(self.y[0]) > self.x_range:                 #Tamanho do array de tempo deve ser igual ao de cada curva
            for n in range(0,len(y)):                     #Quando o mesmo chega no valor máximo (definido pela escala+amostragem)
                self.y[n] = np.delete(self.y[n], 0)       #O valor de índice 0 é removido para que um novo valor possa entrar no maior indice
            self.index = self.x_range                     #Valor de índice quando chega no máximo, é mantido nele
        else:
            self.x.append(self.index)                     #Se o tamanho do array ainda não chegou ao seu máximo, então valores vão sendo adicionados no array de tempo

        for n in range(0, len(y)):
            self.curve[n].setData(self.x,self.y[n])       #Replotagem das curvas com valores atualizados
        self.index += 1                                   #Valor de índice é aumentado
