
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,pyqtSignal
import client
import resources

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
       
        self.frameWaiting.clicked.connect(self.btStop_clicked)
        self.InitUI()
    
    def InitUI(self):
        self.ctimer = QTimer(self.frameWaiting)
        self.wait0x06 = True
        self.ctimer.timeout.connect(self.checkDone)
        self.ctimer.start(200)
        self.NumWaiting = 0
        
    def checkDone(self):
        self.NumWaiting+=1
        #thay doi hinh nen 
        if self.NumWaiting > 25:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting3.jpg);}")
        elif self.NumWaiting > 15:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting2.jpg);}")
        elif self.NumWaiting > 5:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting1.jpg);}")
        else:
            self.frameWaiting.setStyleSheet("#frameWaiting{background-image: url(:/images/waiting0.jpg);}")


        #cho nhan duoc co 0x06 moi check xem co su co van hanh khong
        if self.wait0x06 :
            if self.NumWaiting > 5 or client.dataReceved.statusMotor == 6 or client.dataReceved.statusMotor == 3 or client.dataReceved.statusMotor == 1:
                self.wait0x06 = False
            client.loggerInfor.info('waiting 06 done ')
            return

        if client.isWaiting != 1 :
            self.ctimer.stop()
            self.form.close()

        if client.dataReceved.statusMotor == 5 :
            #co su co trong qua trinh van hanh
            self.btStop_clicked()
            print("formWaiting checkDone - co su co trong qua trinh van hanh")
            
    def btStop_clicked(self):
        try :
            client.isWaiting = 2
            client.ThClientMain.sent2Server(b'\xef\xed')
            self.ctimer.stop()
            self.form.close()
            print("form waiting : Dung khan cap")
        except Exception as e:
            client.loggerInfor.info('waiting push ', e.__doc__)



