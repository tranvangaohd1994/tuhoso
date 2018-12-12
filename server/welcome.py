# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal,QTimer
from SV_Login import Ui_SVLogin
import server
import masterPC
import uart
from pygame import mixer

class MyQFrame(QtWidgets.QFrame):
    #
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QFrame.mousePressEvent(self, event)

class Ui_welcomeForm(object):
    def setupUi(self, welcomeForm):
        self.NumExit =0
        self.Form = welcomeForm
        welcomeForm.setObjectName("welcomeForm")
        welcomeForm.resize(1280, 800)
        welcomeForm.setStyleSheet("#welcomeForm{background-image: url(:/images/welcome.jpg);}#btExit{border: none;background-color: none;}#frame{border: none;background-color: none;}")
        self.frame = MyQFrame(welcomeForm)
        self.frame.setGeometry(QtCore.QRect(0, 149, 1280, 631))
        self.frame.setObjectName("frame")
        self.btExit = QtWidgets.QPushButton(welcomeForm)
        self.btExit.setGeometry(QtCore.QRect(0, 0, 161, 91))
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")

        self.retranslateUi(welcomeForm)
        QtCore.QMetaObject.connectSlotsByName(welcomeForm)

    def retranslateUi(self, welcomeForm):
        _translate = QtCore.QCoreApplication.translate
        welcomeForm.setWindowTitle(_translate("welcomeForm", "Form"))
        
        self.frame.clicked.connect(self.frame_click)
        self.btExit.clicked.connect(self.btnExit_click)

        linkFile = server.folderMP3+ "001.mp3"
        server.playmp3(linkFile)

        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.getdataFromClient)
        self.ctimer.start(300)


    def getdataFromClient(self):
        if server.isExitApp:
            server.serverMain.sentLogin2AllClient()
            server.isListenCL = False
            server.serverMain.stop()
            self.ctimer.stop()
            del server.serverMain
            uart.isRead =False
            self.Form.close()

    def btnExit_click(self):
        self.NumExit +=1
        if self.NumExit == 3 :
            # server.isListenCL = False
            # server.serverMain.stop()
            # del server.serverMain
            # uart.isRead =False
            self.Form.close()

    def frame_click(self):
        print("just clicked")
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SVLogin()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullScreen:
            self.window.showFullScreen()
            
    def closeEvent(self):
        self.ctimer.cancel()
        server.isListenCL = False
        server.serverMain.stop()
        del server.serverMain
        del masterPC.ServerPC
        uart.isRead =False

import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    welcomeForm = QtWidgets.QWidget()
    ui = Ui_welcomeForm()
    ui.setupUi(welcomeForm)
    welcomeForm.show()
    if server.isFullScreen:
        welcomeForm.showFullScreen()
    sys.exit(app.exec_())

