
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,pyqtSignal
import client
import resources
import logging
class MyQFrame(QtWidgets.QFrame):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QFrame.mousePressEvent(self, event)

class Ui_FormWaiting(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 600)
        self.form = Form
        self.frameWaiting = MyQFrame(Form)
        self.frameWaiting.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting1.jpg);}\n"
            "#btStop{background-color:#B2FF59;font: 75  14 bold \"Ubuntu\";border: 2px solid #FFAB91;border-radius: 10px;}\n"
            "#btStop:pressed {background-color: #FF6E40;}")
        self.frameWaiting.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameWaiting.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameWaiting.setObjectName("frameWaiting")
      
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
       
        self.frameWaiting.clicked.connect(self.btStop_clicked)
        self.InitUI()
    
    def InitUI(self):
        self.logger = logging.getLogger("Ui_FormWaiting")
        ctimer = QTimer(self.frameWaiting)
        ctimer.timeout.connect(self.checkDone)
        ctimer.start(200)
        self.NumWaiting = 0
        
    def checkDone(self):
        if client.isWaiting != 1 :
            self.logger.debug("Check done")
            self.form.close()

        self.NumWaiting+=1
        if self.NumWaiting > 25:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting3.jpg);}")
        elif self.NumWaiting > 15:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting2.jpg);}")
        elif self.NumWaiting > 5:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting1.jpg);}")
        else:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting0.jpg);}")
        
            
    def btStop_clicked(self):
        client.isWaiting = 2
        client.ThClientMain.sent2Server(b'\xef\xed')
        self.form.close()
        print("form waiting : Dung khan cap")
        self.logger.debug("form waiting : Dung khan cap")



