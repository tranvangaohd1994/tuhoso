# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from mainDisplay import Ui_SV_mainDisplay
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
import sys
import client

class MyQFrame(QtWidgets.QFrame):
    #
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QFrame.mousePressEvent(self, event)

class Ui_welcomeForm(object):
    def setupUi(self, welcomeForm):
        welcomeForm.setObjectName("welcomeForm")
        welcomeForm.setWindowTitle("welcomeClient")
        welcomeForm.resize(1280, 800)
        self.welcomeForm = welcomeForm
        self.frame = MyQFrame(welcomeForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".MyQFrame{background-image: url(:/images/welcome.png);}")
        self.frame.clicked.connect(self.frame_click)
        #endUI
        self.setEvent()

    def setEvent(self):
        self.isOpenForm =False
        ctimer = QTimer(self.frame)
        ctimer.timeout.connect(self.checkServerActive)
        ctimer.start(200)

    def checkServerActive(self):
        if client.isActive2Ser and self.isOpenForm==False:
            self.isOpenForm =True
            self.ui = Ui_SV_mainDisplay()
            self.ui.setupUi()
            self.ui.show()
            if client.isFullScreen:
                self.ui.showFullScreen()
        elif client.isActive2Ser == False:
            self.isOpenForm = False
        
        if client.isExitApp :
            client.isSent2Ser = False
            client.isListeningSer =False
            client.isRead =False
            self.welcomeForm.close()
            sys.exit()
        #neu co ket noi den server thi gui data cho server

    def frame_click(self):
        print("frame clicked ",client.ThClientMain.numClick2close)
        client.ThClientMain.numClick2close+=1
        if(client.ThClientMain.numClick2close == 5) :
            client.isSent2Ser = False
            client.isListeningSer =False
            client.isRead =False
            self.welcomeForm.close()
            sys.exit()

import resources

if __name__ == "__main__":
    
    try:
        app = QtWidgets.QApplication(sys.argv)
        welcomeForm = QtWidgets.QWidget()
        ui = Ui_welcomeForm()
        ui.setupUi(welcomeForm)
        welcomeForm.show()
        if client.isFullScreen:
            welcomeForm.showFullScreen()
        sys.exit(app.exec_())
    except Exception as e :
        client.loggerInfor.info('ERROR IN mainDisplay->showTemp : ', e.__doc__)
        
