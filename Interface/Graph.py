from pyqtgraph import PlotItem,AxisItem,GridItem
import time


class Graph(PlotItem):
    index = 0

    def __init__(self,x_sampling, x_range, y1_min, y1_max, y2_min, y2_max, x_size, y_size, color1, color2, name1, name2):
        super(Graph, self).__init__()
        self.x_sampling=1
        self.x_range = x_range/x_sampling
        self.y1_min = y1_min
        self.y1_max = y1_max
        self.y2_min = y2_min
        self.y2_max = y2_max
        self.x_size = x_size
        self.y_size = y_size
        self.color1 = color1
        self.color2 = color2
        self.name1 = name1
        self.name2 = name2
        self.curve1 = self.plot(pen=color1, name=self.name1)
        self.curve2 = self.plot(pen=color2, name=self.name2)

        self.axisTime = AxisItem("bottom", 'w')
        self.axis2 = AxisItem("right", color2)
        self.axis1 = AxisItem("left", color1)
        self.axis1.setLabel(self.name1,'Tonf')
        self.axis2.setLabel(self.name2,'mV')
        self.axisTime.setLabel("Tempo", 's')


        self.axisTime.setRange(0,x_range)
        self.axis1.setRange(y1_min,y1_max)
        self.axis2.setRange(y2_min,y2_max)
        self.showAxis("left",False)
        self.showAxis("bottom",False)

        self.setMinimumSize(x_size,y_size)

        self.setXRange(0, self.x_range, padding=0)
        self.setYRange(min(self.y1_min,self.y2_min), max(self.y1_max,self.y2_max), padding=0)
        self.x1 = []
        self.y1 = []
        self.y2 = []
        self.timeant = time.time()



    def updateGraph(self, y1, y2):
        # print(time.time()-self.timeant)
        self.y1.append(y1)
        self.y2.append(y2)
        if len(self.y1) > self.x_range + 1:
            self.y1.pop(0)
            self.y2.pop(0)
            self.index = self.x_range
        else:
            self.x1.append(self.index)
        self.index = self.index + 1

        self.curve1.setData(self.x1, self.y1)
        self.curve2.setData(self.x1, self.y2)
        #self.timeant = time.time()
