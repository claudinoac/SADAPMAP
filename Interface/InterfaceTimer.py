from datetime import datetime
from PyQt5 import QtWidgets,QtCore

class InterfaceTimer(object):

    def __init__(self):
        self.startTimerButton = QtWidgets.QPushButton()
        self.pauseTimerButton = QtWidgets.QPushButton()
        self.stopTimerButton = QtWidgets.QPushButton()
        self.startRegTimerButton = QtWidgets.QPushButton()
        self.stopRegTimerButton = QtWidgets.QPushButton()
        self.regTimerLabel=QtWidgets.QLabel()

        self.screenTimerLabel = QtWidgets.QLabel()
        self.currentTimeLabel = QtWidgets.QLabel()
        self.currentTimer = QtCore.QTimer()


        self.regTimerLabel.setText("0 s")
        self.timeValue=0
        self.regTimerValue=0

    def linkActions(self):
        self.startTimerButton.pressed.connect(self.startScreenTimer)
        self.pauseTimerButton.pressed.connect(self.playPauseScreenTimer)
        self.stopTimerButton.pressed.connect(self.stopScreenTimer)
        self.currentTimer.timeout.connect(self.updateCurrentTime)
        self.startRegTimerButton.pressed.connect(self.startRegressiveTimer)
        self.stopRegTimerButton.pressed.connect(self.startRegressiveTimer)
        self.currentTimer.start(500)
        self.screenTimerFlag = False

    def startRegressiveTimer(self):
        try:
            self.regTimerValue=self.regTimerLabel.text()
            self.regTimerValue.split(" ", 3)
            self.regTimerValue=float(self.regTimerValue[0])
        except(ValueError):
            print(self.regTimerLabel.text)

        self.regTimer=QtCore.QTimer()
        self.regTimer.timeout.connect(self.updateRegTimer)
        self.regTimer.start(100)
        self.startRegTimerButton.pressed.disconnect()
        self.startRegTimerButton.setText("Pausar")
        self.startRegTimerButton.pressed.connect(self.pauseRegressiveTimer)

    def pauseRegressiveTimer(self):
        self.regTimer.stop()
        self.startRegTimerButton.setText("Continuar")
        self.startRegTimerButton.pressed.disconnect()
        self.startRegTimerButton.pressed.connect(self.startRegressiveTimer)

    def stopRegressiveTimer(self):
        self.regTimer.stop()
        self.startRegTimerButton.setText("Iniciar")
        self.startRegTimerButton.pressed.disconnect()
        self.startRegTimerButton.pressed.connect(startRegressiveTimer)
        self.regTimerLabel.setText("0.00 s")

    def updateRegTimer(self):
        while(self.regTimerValue!=0):
            self.regTimerValue -= 0.1

        self.regTimerLabel.setText("%.1f seg"%self.regTimerValue)

    def startScreenTimer(self):
        self.timeValue = 0
        self.screenTimer = QtCore.QTimer()
        self.screenTimer.timeout.connect(self.updateScreenTimer)
        self.screenTimer.start(100)
        self.startTimerButton.setText("Reiniciar")
        self.pauseTimerButton.setText("Pausar")
        self.screenTimerFlag = True

    def playPauseScreenTimer(self):
        self.startTimerButton.setText("Reiniciar")
        if (self.pauseTimerButton == "Iniciar"):
            self.startScreenTimer()
        if (self.screenTimerFlag == True):
            self.screenTimer.stop()
            self.screenTimerFlag = False
            self.pauseTimerButton.setText("Continuar")
        else:
            try:
                self.screenTimer.start(100)
                self.screenTimerFlag = True
                self.pauseTimerButton.setText("Pausar")
            except:
                self.startScreenTimer()

    def stopScreenTimer(self):
        self.screenTimer.stop()
        self.screenTimerLabel.setText("0.00 seg")
        self.timeValue = 0
        self.screenTimerFlag = False
        self.startTimerButton.setText("Iniciar")
        self.pauseTimerButton.setText("Iniciar")



    def updateScreenTimer(self):
        self.timeValue += 0.1
        self.screenTimerLabel.setText("%.1f seg" % self.timeValue)

    def updateCurrentTime(self):
        self.currentTime = (str(datetime.now().time()))
        self.currentTime = self.currentTime.split(":", 4)
        self.currentTime[2] = self.currentTime[2].split(".", 3)
        self.currentTimeLabel.setText("%s:%s:%s" % (self.currentTime[0], self.currentTime[1], self.currentTime[2][0]))
