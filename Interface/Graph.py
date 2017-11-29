from pyqtgraph import PlotItem,AxisItem,GridItem
import time


class Graph(PlotItem):
    index = 0

    def __init__(self,x_sampling, x_range, n_axis, y_min, y_max, x_size, y_size, color, name,unit):
        super(Graph, self).__init__()
        self.x_sampling=1
        self.x_range = x_range/x_sampling

        self.curve = []
        self.axis = []
        self.y=[]

        self.curve.append(self.plot(pen=color[0], name=name[0]))
        self.axis.append(AxisItem("left",color[0]))
        self.axis[0].setLabel(name[0], unit[0])
        self.axis[0].setRange(y_min[0], y_max[0])

        y_axis = [0]
        self.y.append(y_axis)


        try:
            for n in range(1,n_axis):
                self.curve.append(self.plot(pen=color[n], name=name[n]))
                self.axis.append(AxisItem("right",color[n]))
                self.axis[n].setLabel(name[n],unit[n])
                self.axis[n].setRange(y_min[n],y_max[n])
                self.y.append(y_axis)
                print(y_axis)
        except Exception as e:
            print(e)

        self.axisTime = AxisItem("bottom", 'w')
        self.axisTime.setLabel("Tempo", 's')
        self.axisTime.setRange(0, x_range)
        self.x=[]
        self.x.append(0)

        self.showAxis("left", False)
        self.showAxis("bottom", False)

        self.setMinimumSize(x_size, y_size)

        self.setXRange(0, self.x_range, padding=0)
        self.setYRange(min(y_min), max(y_max), padding=0)

        self.timeant = time.time()


    def updateGraph(self, y):
        # print(time.time()-self.timeant)


        for n in range(0,len(y)):
            print(y[n])
            print(self.y[n])
            self.y[n].append(y[n])

        if len(self.y[0]) > self.x_range+1 :
            for n in range(0,len(y)):
                self.y[n].pop(0)
            self.index = self.x_range
        else:
            self.x.append(self.index)

        self.index = self.index + 1


        for n in range(0,len(y)):
            self.curve[0].setData(self.x, self.y[0])

        self.timeant = time.time()
