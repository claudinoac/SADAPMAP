# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/CalibracaoT.ui'
#
# Created: Fri Nov 24 19:35:13 2017
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 695)
        MainWindow.setMinimumSize(QtCore.QSize(817, 0))
        MainWindow.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"color: rgb(255,255,255);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setAutoFillBackground(False)
        self.centralWidget.setObjectName("centralWidget")
        self.CentralGraph = QtWidgets.QGraphicsView(self.centralWidget)
        self.CentralGraph.setGeometry(QtCore.QRect(420, 10, 931, 611))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CentralGraph.sizePolicy().hasHeightForWidth())
        self.CentralGraph.setSizePolicy(sizePolicy)
        self.CentralGraph.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CentralGraph.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.CentralGraph.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.CentralGraph.setAlignment(QtCore.Qt.AlignJustify)
        self.CentralGraph.setObjectName("CentralGraph")

        self.scaleBox = QtWidgets.QGroupBox(self.centralWidget)
        self.scaleBox.setGeometry(QtCore.QRect(10, 10, 401, 231))
        self.scaleBox.setToolTip("")
        self.scaleBox.setStatusTip("")
        self.scaleBox.setWhatsThis("")
        self.scaleBox.setAutoFillBackground(False)
        self.scaleBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(194, 8, 6);\n"
"color: rgb(255, 255, 255);")
        self.scaleBox.setFlat(False)
        self.scaleBox.setCheckable(False)
        self.scaleBox.setObjectName("scaleBox")
        self.tempBox = QtWidgets.QGroupBox(self.scaleBox)
        self.tempBox.setGeometry(QtCore.QRect(10, 30, 181, 91))
        self.tempBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.tempBox.setObjectName("tempBox")
        self.temp_max = QtWidgets.QLineEdit(self.tempBox)
        self.temp_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.temp_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.temp_max.setObjectName("temp_max")
        self.temp_max_label = QtWidgets.QLabel(self.tempBox)
        self.temp_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.temp_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.temp_max_label.setObjectName("temp_max_label")
        self.temp_min_label = QtWidgets.QLabel(self.tempBox)
        self.temp_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.temp_min_label.setStyleSheet("border:rgb(255,255,255)")
        self.temp_min_label.setObjectName("temp_min_label")
        self.temp_min = QtWidgets.QLineEdit(self.tempBox)
        self.temp_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.temp_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.temp_min.setObjectName("temp_min")
        self.powerBox = QtWidgets.QGroupBox(self.scaleBox)
        self.powerBox.setGeometry(QtCore.QRect(210, 30, 181, 91))
        self.powerBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.powerBox.setObjectName("powerBox")
        self.p_max = QtWidgets.QLineEdit(self.powerBox)
        self.p_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.p_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.p_max.setObjectName("p_max")
        self.p_max_label = QtWidgets.QLabel(self.powerBox)
        self.p_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.p_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_max_label.setObjectName("p_max_label")
        self.p_min_label = QtWidgets.QLabel(self.powerBox)
        self.p_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.p_min_label.setStyleSheet("border: rgb(255,255,255)")
        self.p_min_label.setObjectName("p_min_label")
        self.p_min = QtWidgets.QLineEdit(self.powerBox)
        self.p_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.p_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.p_min.setObjectName("p_min")
        self.timeGBox = QtWidgets.QGroupBox(self.scaleBox)
        self.timeGBox.setGeometry(QtCore.QRect(10, 130, 181, 91))
        self.timeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.timeGBox.setObjectName("timeGBox")
        self.t_max = QtWidgets.QLineEdit(self.timeGBox)
        self.t_max.setGeometry(QtCore.QRect(90, 40, 61, 21))
        self.t_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.t_max.setObjectName("t_max")
        self.t_max_label = QtWidgets.QLabel(self.timeGBox)
        self.t_max_label.setGeometry(QtCore.QRect(30, 40, 51, 21))
        self.t_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.t_max_label.setObjectName("t_max_label")
        self.forceBox = QtWidgets.QGroupBox(self.scaleBox)
        self.forceBox.setGeometry(QtCore.QRect(210, 130, 181, 91))
        self.forceBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceBox.setObjectName("forceBox")
        self.f_max = QtWidgets.QLineEdit(self.forceBox)
        self.f_max.setGeometry(QtCore.QRect(90, 30, 61, 21))
        self.f_max.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.f_max.setObjectName("f_max")
        self.f_max_label = QtWidgets.QLabel(self.forceBox)
        self.f_max_label.setGeometry(QtCore.QRect(30, 30, 57, 21))
        self.f_max_label.setStyleSheet("border: rgb(255,255,255)")
        self.f_max_label.setObjectName("f_max_label")
        self.f_min_label = QtWidgets.QLabel(self.forceBox)
        self.f_min_label.setGeometry(QtCore.QRect(30, 60, 57, 21))
        self.f_min_label.setStyleSheet("border: rgb(255,255,255)")
        self.f_min_label.setObjectName("f_min_label")
        self.f_min = QtWidgets.QLineEdit(self.forceBox)
        self.f_min.setGeometry(QtCore.QRect(90, 60, 61, 21))
        self.f_min.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);")
        self.f_min.setObjectName("f_min")
        self.samplingBox = QtWidgets.QGroupBox(self.centralWidget)
        self.samplingBox.setGeometry(QtCore.QRect(150, 250, 121, 71))
        self.samplingBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(255, 83, 0);\n"
"color: rgb(255,255,255);")
        self.samplingBox.setObjectName("samplingBox")
        self.samplingCBox = QtWidgets.QComboBox(self.samplingBox)
        self.samplingCBox.setGeometry(QtCore.QRect(20, 30, 91, 31))
        self.samplingCBox.setMouseTracking(False)
        self.samplingCBox.setAutoFillBackground(False)
        self.samplingCBox.setStyleSheet("background-color:rgb(53, 53, 53)\n"
"")
        self.samplingCBox.setObjectName("samplingCBox")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.samplingCBox.addItem("")
        self.cronometroBox = QtWidgets.QGroupBox(self.centralWidget)
        self.cronometroBox.setGeometry(QtCore.QRect(10, 330, 401, 201))
        self.cronometroBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border:1px solid rgb(123, 0, 129);")
        self.cronometroBox.setObjectName("cronometroBox")
        self.startTimerButton = QtWidgets.QPushButton(self.cronometroBox)
        self.startTimerButton.setGeometry(QtCore.QRect(170, 30, 51, 31))
        self.startTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(44, 0, 47);")
        self.startTimerButton.setObjectName("startTimerButton")
        self.timerGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.timerGBox.setGeometry(QtCore.QRect(10, 30, 141, 71))
        self.timerGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.timerGBox.setObjectName("timerGBox")
        self.timerLabel = QtWidgets.QLabel(self.timerGBox)
        self.timerLabel.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.timerLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"border: 1px solid rgb(44, 0, 47);\n"
"font: 75 12pt \"Noto Serif\";")
        self.timerLabel.setObjectName("timerLabel")
        self.currentTimeGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.currentTimeGBox.setGeometry(QtCore.QRect(240, 30, 151, 71))
        self.currentTimeGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.currentTimeGBox.setObjectName("currentTimeGBox")
        self.currentTimeLabel = QtWidgets.QLabel(self.currentTimeGBox)
        self.currentTimeLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.currentTimeLabel.setStyleSheet("background-color:rgb(80, 80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.currentTimeLabel.setObjectName("currentTimeLabel")
        self.horaAtualGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.horaAtualGBox.setGeometry(QtCore.QRect(240, 120, 151, 71))
        self.horaAtualGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.horaAtualGBox.setObjectName("horaAtualGBox")
        self.horaAtualLabel = QtWidgets.QLabel(self.horaAtualGBox)
        self.horaAtualLabel.setGeometry(QtCore.QRect(30, 30, 91, 31))
        self.horaAtualLabel.setStyleSheet("background-color:rgb(80, 80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.horaAtualLabel.setObjectName("horaAtualLabel")
        self.stopTimerButton = QtWidgets.QPushButton(self.cronometroBox)
        self.stopTimerButton.setGeometry(QtCore.QRect(170, 70, 51, 31))
        self.stopTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(44, 0, 47);")
        self.stopTimerButton.setObjectName("stopTimerButton")
        self.regTimerGBox = QtWidgets.QGroupBox(self.cronometroBox)
        self.regTimerGBox.setGeometry(QtCore.QRect(10, 120, 141, 71))
        self.regTimerGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.regTimerGBox.setObjectName("regTimerGBox")
        self.regTimerLabel = QtWidgets.QLabel(self.regTimerGBox)
        self.regTimerLabel.setGeometry(QtCore.QRect(20, 30, 81, 31))
        self.regTimerLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"border: 1px solid rgb(255,255,255);\n"
"color:rgb(255,255,255);\n"
"font: 75 12pt \"Noto Serif\";")
        self.regTimerLabel.setObjectName("regTimerLabel")
        self.startRegTimerButton = QtWidgets.QPushButton(self.cronometroBox)
        self.startRegTimerButton.setGeometry(QtCore.QRect(170, 120, 51, 31))
        self.startRegTimerButton.setStyleSheet("border: 1px solid rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.startRegTimerButton.setObjectName("startRegTimerButton")
        self.stopRegTimerButton = QtWidgets.QPushButton(self.cronometroBox)
        self.stopRegTimerButton.setGeometry(QtCore.QRect(170, 160, 51, 31))
        self.stopRegTimerButton.setStyleSheet("background-color:rgb(53, 53, 53);\n"
"border: 1px solid rgb(255,255,255);")
        self.stopRegTimerButton.setObjectName("stopRegTimerButton")
        self.prensaNameGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.prensaNameGBox.setGeometry(QtCore.QRect(10, 250, 121, 71))
        self.prensaNameGBox.setStyleSheet("\n"
"border: 1px solid rgb(27, 144, 0);\n"
"background-color: rgb(86, 86, 86);")
        self.prensaNameGBox.setObjectName("prensaNameGBox")
        self.prensaName = QtWidgets.QLineEdit(self.prensaNameGBox)
        self.prensaName.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.prensaName.setStyleSheet("font: 11pt \"Noto Serif\";\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.prensaName.setObjectName("prensaName")
        self.arquivoSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arquivoSalvoLabel.setGeometry(QtCore.QRect(420, 630, 111, 16))
        self.arquivoSalvoLabel.setObjectName("arquivoSalvoLabel")
        self.arqSalvoLabel = QtWidgets.QLabel(self.centralWidget)
        self.arqSalvoLabel.setGeometry(QtCore.QRect(530, 630, 241, 16))
        self.arqSalvoLabel.setObjectName("arqSalvoLabel")
        self.ambientTempGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.ambientTempGBox.setGeometry(QtCore.QRect(290, 250, 121, 71))
        self.ambientTempGBox.setStyleSheet("\n"
"border: 1px solid rgb(255, 243, 0);\n"
"background-color: rgb(86, 86, 86);")
        self.ambientTempGBox.setObjectName("ambientTempGBox")
        self.ambientTempLabel = QtWidgets.QLineEdit(self.ambientTempGBox)
        self.ambientTempLabel.setGeometry(QtCore.QRect(10, 30, 101, 31))
        self.ambientTempLabel.setStyleSheet("font: 14pt \"Noto Serif\";\n"
"color:rgb(255,255,255);\n"
"background-color:rgb(53, 53, 53)")
        self.ambientTempLabel.setObjectName("ambientTempLabel")
        self.absolValGBox = QtWidgets.QGroupBox(self.centralWidget)
        self.absolValGBox.setGeometry(QtCore.QRect(10, 540, 401, 101))
        self.absolValGBox.setStyleSheet("background-color: rgb(86, 86, 86);\n"
"border: 1px solid rgb(26, 149, 172)")
        self.absolValGBox.setObjectName("absolValGBox")
        self.tempGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.tempGBox.setGeometry(QtCore.QRect(10, 30, 121, 61))
        self.tempGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.tempGBox.setObjectName("tempGBox")
        self.tempLabel = QtWidgets.QLabel(self.tempGBox)
        self.tempLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.tempLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.tempLabel.setObjectName("tempLabel")
        self.powGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.powGBox.setGeometry(QtCore.QRect(270, 30, 121, 61))
        self.powGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.powGBox.setObjectName("powGBox")
        self.powLabel = QtWidgets.QLabel(self.powGBox)
        self.powLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.powLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.powLabel.setObjectName("powLabel")
        self.forceGBox = QtWidgets.QGroupBox(self.absolValGBox)
        self.forceGBox.setGeometry(QtCore.QRect(140, 30, 121, 61))
        self.forceGBox.setStyleSheet("background-color:rgb(53, 53, 53)")
        self.forceGBox.setObjectName("forceGBox")
        self.forceLabel = QtWidgets.QLabel(self.forceGBox)
        self.forceLabel.setGeometry(QtCore.QRect(10, 20, 101, 31))
        self.forceLabel.setStyleSheet("background-color: rgb(80,80,80);\n"
"color:rgb(255,255,255);\n"
"font: 14pt \"Noto Serif\";")
        self.forceLabel.setObjectName("forceLabel")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuStatusBar = QtWidgets.QStatusBar(MainWindow)
        self.menuStatusBar.setObjectName("menuStatusBar")
        MainWindow.setStatusBar(self.menuStatusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1366, 23))
        self.menuBar.setObjectName("menuBar")
        self.menuArquivo = QtWidgets.QMenu(self.menuBar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuEtapa = QtWidgets.QMenu(self.menuBar)
        self.menuEtapa.setObjectName("menuEtapa")
        self.menuPorta = QtWidgets.QMenu(self.menuBar)
        self.menuPorta.setObjectName("menuPorta")
        self.menuPlay_Pause = QtWidgets.QMenu(self.menuBar)
        self.menuPlay_Pause.setObjectName("menuPlay_Pause")
        self.menuTermopar = QtWidgets.QMenu(self.menuBar)
        self.menuTermopar.setObjectName("menuTermopar")
        self.menuFinalizar = QtWidgets.QMenu(self.menuBar)
        self.menuFinalizar.setObjectName("menuFinalizar")
        MainWindow.setMenuBar(self.menuBar)
        self.alternaCalibraP = QtWidgets.QAction(MainWindow)
        self.alternaCalibraP.setObjectName("alternaCalibraP")
        self.alternaCalibraT = QtWidgets.QAction(MainWindow)
        self.alternaCalibraT.setObjectName("alternaCalibraT")
        self.alternaProc = QtWidgets.QAction(MainWindow)
        self.alternaProc.setObjectName("alternaProc")
        self.botaoAbrir = QtWidgets.QAction(MainWindow)
        self.botaoAbrir.setEnabled(False)
        self.botaoAbrir.setIconVisibleInMenu(True)
        self.botaoAbrir.setObjectName("botaoAbrir")
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.actionSalvar_Como = QtWidgets.QAction(MainWindow)
        self.actionSalvar_Como.setObjectName("actionSalvar_Como")
        self.botaoSalvar = QtWidgets.QAction(MainWindow)
        self.botaoSalvar.setObjectName("botaoSalvar")
        self.botaoSalvarComo = QtWidgets.QAction(MainWindow)
        self.botaoSalvarComo.setObjectName("botaoSalvarComo")
        self.selectPortaUSB = QtWidgets.QAction(MainWindow)
        self.selectPortaUSB.setObjectName("selectPortaUSB")
        self.menuArquivo.addAction(self.botaoAbrir)
        self.menuArquivo.addAction(self.botaoSalvar)
        self.menuArquivo.addAction(self.botaoSalvarComo)
        self.menuEtapa.addAction(self.alternaCalibraP)
        self.menuEtapa.addAction(self.alternaCalibraT)
        self.menuEtapa.addAction(self.alternaProc)
        self.menuBar.addAction(self.menuArquivo.menuAction())
        self.menuBar.addAction(self.menuEtapa.menuAction())
        self.menuBar.addAction(self.menuPorta.menuAction())
        self.menuBar.addAction(self.menuTermopar.menuAction())
        self.menuBar.addAction(self.menuFinalizar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pauseTimerButton = self.startRegTimerButton


        self.menuPlay_Pause = QtWidgets.QAction(MainWindow)
        self.menuPlay_Pause.setText("Play")
        self.menuPlay_Pause.setObjectName("menuPlay_Pause")
        self.menuBar.addAction(self.menuPlay_Pause)
        self.menuPlay_Pause.setCheckable(True)

        self.menuPlay_Pause.toggled.connect(self.playPauseButtonAnimation)

        self.pauseTimerButton.setText("Iniciar")
        self.screenTimerFlag = False
        self.startTimerButton.pressed.connect(self.startScreenTimer)
        self.stopTimerButton.pressed.connect(self.stopScreenTimer)
        self.pauseTimerButton.pressed.connect(self.playPauseScreenTimer)
        self.currentTimer = QtCore.QTimer()
        self.currentTimer.timeout.connect(self.updateCurrentTime)
        self.currentTimer.start(500)

        self.screenTimerFlag = False
        self.retranslateUi(MainWindow)


    def sceneSelector(self, scene):
        self.CentralGraph.setScene(scene)
        self.CentralGraph.setBackgroundBrush(QtCore.Qt.black)
        self.CentralGraph.setInteractive(False)


    def serialListPanel(self, seriaList):
        self.usb = []
        for i in range(0, len(seriaList)):
            self.usb.append(QtWidgets.QAction(self.MainWindow))
            self.usb[i].setText(seriaList[i].device)
            self.usb[i].setCheckable(True)
            self.menuPorta.addAction(self.usb[i])


    def playPauseButtonAnimation(self):
        if (self.menuPlay_Pause.text() == "Play"):
            self.menuPlay_Pause.setText("Pause")
            self.startTimeLabel.setText(self.currentTimeLabel.text())
        else:
            self.menuPlay_Pause.setText("Play")


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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SADAMAP - Análise de Dados: Etapa 2 - Calibração de Temperatura"))
        self.scaleBox.setTitle(_translate("MainWindow", "Escalas de Visualização (Range)"))
        self.tempBox.setTitle(_translate("MainWindow", "Temperatura (ºC)"))
        self.temp_max.setText(_translate("MainWindow", "1000"))
        self.temp_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.temp_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.temp_min.setText(_translate("MainWindow", "100"))
        self.powerBox.setTitle(_translate("MainWindow", "Potência (kW)"))
        self.p_max.setText(_translate("MainWindow", "100"))
        self.p_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.p_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.p_min.setText(_translate("MainWindow", "10"))
        self.timeGBox.setTitle(_translate("MainWindow", "Tempo (s)"))
        self.t_max.setText(_translate("MainWindow", "50"))
        self.t_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.forceBox.setTitle(_translate("MainWindow", "Força (kN)"))
        self.f_max.setText(_translate("MainWindow", "1000"))
        self.f_max_label.setText(_translate("MainWindow", "Máximo:"))
        self.f_min_label.setText(_translate("MainWindow", "Mínimo:"))
        self.f_min.setText(_translate("MainWindow", "20"))
        self.samplingBox.setTitle(_translate("MainWindow", "Amostragem"))
        self.samplingCBox.setItemText(0, _translate("MainWindow", "100 mseg"))
        self.samplingCBox.setItemText(1, _translate("MainWindow", "200 mseg"))
        self.samplingCBox.setItemText(2, _translate("MainWindow", "500 mseg"))
        self.samplingCBox.setItemText(3, _translate("MainWindow", "1 seg"))
        self.samplingCBox.setItemText(4, _translate("MainWindow", "1.5 seg"))
        self.samplingCBox.setItemText(5, _translate("MainWindow", "2 seg"))
        self.samplingCBox.setItemText(6, _translate("MainWindow", "2.5 seg"))
        self.samplingCBox.setItemText(7, _translate("MainWindow", "5 seg"))
        self.samplingCBox.setItemText(8, _translate("MainWindow", "10 seg"))
        self.cronometroBox.setTitle(_translate("MainWindow", "Timer"))
        self.startTimerButton.setText(_translate("MainWindow", "Iniciar"))
        self.timerGBox.setTitle(_translate("MainWindow", "Cronômetro"))
        self.timerLabel.setText(_translate("MainWindow", "10.2674 s"))
        self.currentTimeGBox.setTitle(_translate("MainWindow", "Horário de Início"))
        self.currentTimeLabel.setText(_translate("MainWindow", "16:30:15"))
        self.horaAtualGBox.setTitle(_translate("MainWindow", "Horário Atual"))
        self.horaAtualLabel.setText(_translate("MainWindow", "17:05:56"))
        self.stopTimerButton.setText(_translate("MainWindow", "Parar"))
        self.regTimerGBox.setTitle(_translate("MainWindow", "Cont. Regressivo"))
        self.regTimerLabel.setText(_translate("MainWindow", "10.2674 s"))
        self.startRegTimerButton.setText(_translate("MainWindow", "Iniciar"))
        self.stopRegTimerButton.setText(_translate("MainWindow", "Parar"))
        self.prensaNameGBox.setTitle(_translate("MainWindow", "Prensa"))
        self.prensaName.setText(_translate("MainWindow", "Pr 400 Tonf"))
        self.arquivoSalvoLabel.setText(_translate("MainWindow", "Arquivo Salvo em:"))
        self.arqSalvoLabel.setText(_translate("MainWindow", "/home/LAPMA/Pressao/1025565.temp"))
        self.ambientTempGBox.setTitle(_translate("MainWindow", "Temp. Ambiente"))
        self.ambientTempLabel.setText(_translate("MainWindow", "    26 ºC"))
        self.absolValGBox.setTitle(_translate("MainWindow", "Valores Absolutos"))
        self.tempGBox.setTitle(_translate("MainWindow", "Temperatura"))
        self.tempLabel.setText(_translate("MainWindow", "42.679 ºC"))
        self.powGBox.setTitle(_translate("MainWindow", "Potência"))
        self.powLabel.setText(_translate("MainWindow", "23.567 kW"))
        self.forceGBox.setTitle(_translate("MainWindow", "Força"))
        self.forceLabel.setText(_translate("MainWindow", "340.34 kN"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuEtapa.setTitle(_translate("MainWindow", "Etapa"))
        self.menuPorta.setTitle(_translate("MainWindow", "Porta"))
       # self.menuPlay_Pause.setTitle(_translate("MainWindow", "Iniciar/Pausar"))
        self.menuTermopar.setTitle(_translate("MainWindow", "Termopar"))
        self.menuFinalizar.setTitle(_translate("MainWindow", "Finalizar"))
        self.alternaCalibraP.setText(_translate("MainWindow", "Calibração P"))
        self.alternaCalibraT.setText(_translate("MainWindow", "Calibração T"))
        self.alternaProc.setText(_translate("MainWindow", "Processamento"))
        self.botaoAbrir.setText(_translate("MainWindow", "Abrir"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar_Como.setText(_translate("MainWindow", "Salvar Como"))
        self.botaoSalvar.setText(_translate("MainWindow", "Salvar"))
        self.botaoSalvarComo.setText(_translate("MainWindow", "Salvar Como"))
        self.selectPortaUSB.setText(_translate("MainWindow", "Selecionar porta USB"))

