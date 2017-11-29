from datetime import datetime
from PyQt5 import QtWidgets,QtCore,QtGui

class InterfaceTimer(object):

    def __init__(self):
        self.startTimerButton = QtWidgets.QPushButton()
        self.stopTimerButton = QtWidgets.QPushButton()
        self.startRegTimerButton = QtWidgets.QPushButton()
        self.stopRegTimerButton = QtWidgets.QPushButton()
        self.regTimerLabel=QtWidgets.QLabel()

        self.timerLabel = QtWidgets.QLabel()
        self.currentTimeLabel = QtWidgets.QLabel()
        self.currentTimer = QtCore.QTimer()
        self.regTimer=QtCore.QTimer()
        self.MainWindow=QtWidgets.QDialog()

        self.regTimerLabel.setText("0.0 s")
        self.timerLabel.setText("0.0 s")
        self.timeValue=0
        self.regTimerValue=1000

    def linkActions(self):
        self.startTimerButton.pressed.connect(self.startScreenTimer)
        self.stopTimerButton.pressed.connect(self.stopScreenTimer)
        self.currentTimer.timeout.connect(self.updateCurrentTime)
        self.startRegTimerButton.pressed.connect(self.startRegressiveTimer)
        self.stopRegTimerButton.pressed.connect(self.stopRegressiveTimer)
        self.currentTimer.start(500)
        self.screenTimerFlag = False

    def startRegressiveTimer(self):
        try:
            if(self.regTimerLabel.text().split(" ",3)[1]=="s"):
                self.regTimerValue=self.regTimerLabel.text().split(" ",3)[0]

            else:
                self.regTimerValue=self.regTimerLabel.text()
            print(self.regTimerValue)
            self.regTimerValue=float(self.regTimerValue)

        except(IndexError):
            self.regTimerValue=self.regTimerLabel.text()

        except(ValueError,TypeError):
            error=QtWidgets.QMessageBox(self.MainWindow)
            error.setText("Valor Inválido! Definindo valor padrão de 1000 segundos")
            error.setWindowTitle("ERRO!")
            error.exec()
            self.regTimerValue = 1000

        print(self.regTimerValue)
        self.regTimerValue = float(self.regTimerValue)


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
        self.startRegTimerButton.pressed.connect(self.startRegressiveTimer)
        self.regTimerLabel.setText("0.00 s")

    def updateRegTimer(self):
        if(self.regTimerValue>=0.1):
            self.regTimerValue -= 0.1

        self.regTimerLabel.setText("%.1f s"%self.regTimerValue)

    def startScreenTimer(self):
        self.screenTimer = QtCore.QTimer()
        self.screenTimer.timeout.connect(self.updateScreenTimer)
        self.screenTimer.start(100)
        self.startTimerButton.pressed.disconnect()
        self.startTimerButton.pressed.connect(self.pauseScreenTimer)
        self.startTimerButton.setText("Pausar")

    def pauseScreenTimer(self):
        self.screenTimer.stop()
        self.startTimerButton.setText("Continuar")
        self.startTimerButton.pressed.disconnect()
        self.startTimerButton.pressed.connect(self.startScreenTimer)

    def stopScreenTimer(self):
        self.screenTimer.stop()
        self.timerLabel.setText("0.00 s")
        self.timeValue = 0
        self.screenTimerFlag = False
        self.startTimerButton.setText("Iniciar")

    def updateScreenTimer(self):
        self.timeValue += 0.1
        self.timerLabel.setText("%.1f s" % self.timeValue)

    def updateCurrentTime(self):
        self.currentTime = (str(datetime.now().time()))
        self.currentTime = self.currentTime.split(":", 4)
        self.currentTime[2] = self.currentTime[2].split(".", 3)
        self.currentTimeLabel.setText("%s:%s:%s" % (self.currentTime[0], self.currentTime[1], self.currentTime[2][0]))
