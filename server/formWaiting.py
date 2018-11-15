# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formWaiting.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,pyqtSignal,QEventLoop
import server
import resources
import logging
from pygame import mixer
import time

class MyQFrame(QtWidgets.QFrame):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QFrame.mousePressEvent(self, event)

class Ui_FormWaiting(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 800)
        self.form = Form
        self.frameWaiting = MyQFrame(Form)
        self.frameWaiting.setObjectName("frameWaiting")
        self.frameWaiting.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting0.jpg);}\n"
            "#btStop{background-color:#B2FF59;font: 75  14 \"Arial\";border: 2px solid #FFAB91;border-radius: 10px;}\n"
            "#btStop:pressed {background-color: #FF6E40;}")
        self.frameWaiting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWaiting.setFrameShadow(QtWidgets.QFrame.Raised)
        
      
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.InitUI()
        
        self.frameWaiting.clicked.connect(self.btStop_clicked)
       
    
    def InitUI(self):
        self.logger = logging.getLogger("Ui_FormWaiting")
        
        self.ctimer = QTimer(self.frameWaiting)
        self.ctimer.timeout.connect(self.checkDone)
        self.Gaptimer = 200
        self.ctimer.start(self.Gaptimer)
        self.NumWaiting = 0

        self.linkFile = server.folderMP3 + "007.mp3"
        
        #loop = QEventLoop()
        #loop.exec_()
        
    def checkDone(self):
        #print("check Done -- timeout--",server.isWaiting)
        self.NumWaiting += 1
        if self.NumWaiting > (5000 / self.Gaptimer ):
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting3.jpg);}")
        elif self.NumWaiting > (3000 / self.Gaptimer):
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting2.jpg);}")
        elif self.NumWaiting > (1000 / self.Gaptimer):
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting1.jpg);}")
        else:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting0.jpg);}")

        if server.isFlag2906 == False and self.NumWaiting < (2000 / self.Gaptimer ) : #time out toi da 2s
            return
            
        #phat hien qua dong he thong dung khan cap
        if server.serverMain.checkQuaDong() :
            self.linkFile = server.folderMP3 + "018.mp3"
            self.btStop_clicked()
            return
        
        if server.isWaiting == 0 :
            linkFile = server.folderMP3 + "003.mp3"
            server.playmp3(linkFile)

            print("check Done isWaiting ",server.isWaiting , server.haveSucoClient)
            self.ctimer.stop()
            self.form.close()
            return

        elif server.isWaiting == 2:
            print(" timer check dung khan cap ",server.isWaiting)
            self.btStop_clicked()
            return
        if server.haveSucoClient == True:
            print("form waiting : co su co")
            self.btStop_clicked()
            return
        
        
            
    def btStop_clicked(self):
        
        server.playmp3(self.linkFile)
        server.serverMain.sentStop2AllClient()
        self.ctimer.stop()
        print("form waiting : Dung khan cap")
        self.form.close()



