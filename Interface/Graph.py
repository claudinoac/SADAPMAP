from pyqtgraph import PlotItem
import time


class Graph(PlotItem):
    index = 0

    def __init__(self, x_range, y_min, y_max, x_size, y_size, color1, color2, name1, name2):
        super(Graph, self).__init__(title="Curvas de Força e Calibrante")
        self.x_range = x_range
        self.y_min = y_min
        self.y_max = y_max
        self.x_size = x_size
        self.y_size = y_size
        self.color1 = color1
        self.color2 = color2
        self.name1 = name1
        self.name2 = name2

        self.addLegend()
        self.curve1 = self.plot(pen=color1, name=self.name1)
        self.curve2 = self.plot(pen=color2, name=self.name2)
        self.showGrid(True, True)

        self.setPreferredSize(self.x_size, self.y_size)
        self.setXRange(0, self.x_range, padding=0)
        self.setYRange(self.y_min, self.y_max, padding=0)
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
