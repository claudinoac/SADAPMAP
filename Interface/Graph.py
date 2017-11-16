import pyqtgraph
import time

class Graph(pyqtgraph.GraphicsLayout):

    index=1

    def __init__(self,x_range,y_range,x_size,y_size,color1,color2):
        super(Graph,self).__init__()
        self.x_range = x_range
        self.y_range = y_range
        self.x_size = x_size
        self.y_size = y_size
        self.color1 = color1
        self.color2 = color2

        self.p1 = self.addPlot()
        self.curve1 = self.p1.plot(pen=color1)
        self.curve2 = self.p1.plot(pen=color2)
        self.setPreferredSize(self.x_size,self.y_size)
        self.p1.setXRange(0,self.x_range,padding=0)
        self.p1.setYRange(0, self.y_range, padding=0)
        self.x1=[]
        self.y1=[]
        self.y2=[]
        self.timeant=time.time()


    def updateGraph(self,y1,y2):
        #print(time.time()-self.timeant)
        self.y1.append(y1)
        self.y2.append(y2)
        if len(self.y1)>self.x_range+1:
            del self.y1[0]
            del self.y2[0]
            self.index = self.x_range
        else:
            self.x1.append(self.index)
        self.index = self.index + 1

        self.curve1.setData(self.x1, self.y1)
        self.curve2.setData(self.x1,self.y2)
        self.timeant = time.time()


    def setGraphScale(self,x_range,y_range):

        if(x_range==0):
            x_range=1

        if(y_range==0):
            y_range=1

        self.x_range=x_range
        self.y_range=y_range
        self.x1=[]
        self.y1=[]
        self.y2=[]
        self.index=0
        self.clear()
        self.p1=self.addPlot()
        self.p1.setXRange(0, self.x_range, padding=0)
        self.p1.setYRange(0, self.y_range, padding=0)
        self.curve1=self.p1.plot(pen=self.color1)
        self.curve2 = self.p1.plot(pen=self.color2)