# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svDieuKhienDieuHoa.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, QTimer
from kbNumber import Ui_Dialog , MSG_Dialog
import struct
import serial
import threading
import server

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)


class Ui_svDieuHoa(object):
    def setupUi(self, svDieuHoa):
        svDieuHoa.setObjectName("svDieuHoa")
        svDieuHoa.resize(1024, 600)
        self.svDieuHoa = svDieuHoa
        self.frame = QtWidgets.QFrame(svDieuHoa)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}#lbtitle{color:red ;font: 75  30pt \"Arial\";}QPushButton:pressed { background-color: #FF6E40}#btBack{color:white;border-image: url(:/images/back.png);}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #9bff5d;font: 75 20pt \"Arial\";}#tbInput { background-color: #81D4FA;font: 75  24pt \"Arial\"; color:#000000}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(180, 90, 721, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btHocLenhOn = QtWidgets.QPushButton(self.frame)
        self.btHocLenhOn.setGeometry(QtCore.QRect(50, 160, 181, 81))
        self.btHocLenhOn.setObjectName("btHocLenhOn")
        self.btHocLenhOff = QtWidgets.QPushButton(self.frame)
        self.btHocLenhOff.setGeometry(QtCore.QRect(260, 160, 181, 81))
        self.btHocLenhOff.setObjectName("btHocLenhOff")
        self.btHocLenhDKNhiet = QtWidgets.QPushButton(self.frame)
        self.btHocLenhDKNhiet.setGeometry(QtCore.QRect(150, 390, 181, 81))
        self.btHocLenhDKNhiet.setObjectName("btHocLenhDKNhiet")
        self.btHocLenhTatQuat = QtWidgets.QPushButton(self.frame)
        self.btHocLenhTatQuat.setGeometry(QtCore.QRect(260, 280, 181, 81))
        self.btHocLenhTatQuat.setObjectName("btHocLenhTatQuat")
        self.btHocLenhBatQuat = QtWidgets.QPushButton(self.frame)
        self.btHocLenhBatQuat.setGeometry(QtCore.QRect(50, 280, 181, 81))
        self.btHocLenhBatQuat.setObjectName("btHocLenhBatQuat")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(430, 500, 191, 81)) #ffc107
        self.btBack.setObjectName("btBack")
        self.btBack.setStyleSheet("background-color: #ffc107")

        self.tbInput = MyQLineEdit(self.frame)
        self.tbInput.setGeometry(QtCore.QRect(430, 390, 191, 81))
        self.tbInput.setObjectName("tbInput")
        self.btTatQuat = QtWidgets.QPushButton(self.frame)
        self.btTatQuat.setGeometry(QtCore.QRect(820, 280, 181, 81))
        self.btTatQuat.setObjectName("btTatQuat")
        self.btTatDieuHoa = QtWidgets.QPushButton(self.frame)
        self.btTatDieuHoa.setGeometry(QtCore.QRect(820, 160, 181, 81))
        self.btTatDieuHoa.setObjectName("btTatDieuHoa")
        self.btBatDieuHoa = QtWidgets.QPushButton(self.frame)
        self.btBatDieuHoa.setGeometry(QtCore.QRect(610, 160, 181, 81))
        self.btBatDieuHoa.setObjectName("btBatDieuHoa")
        self.btBatQuat = QtWidgets.QPushButton(self.frame)
        self.btBatQuat.setGeometry(QtCore.QRect(610, 280, 181, 81))
        self.btBatQuat.setObjectName("btBatQuat")
        self.btDatNhietDo = QtWidgets.QPushButton(self.frame)
        self.btDatNhietDo.setGeometry(QtCore.QRect(720, 390, 181, 81))
        self.btDatNhietDo.setObjectName("btDatNhietDo")

        self.retranslateUi(svDieuHoa)
        QtCore.QMetaObject.connectSlotsByName(svDieuHoa)

    def retranslateUi(self, svDieuHoa):
        _translate = QtCore.QCoreApplication.translate
        svDieuHoa.setWindowTitle(_translate("svDieuHoa", "Form"))
        self.lbtitle.setText(_translate("svDieuHoa", "Điều khiển - học lệnh điều hòa"))
        self.btHocLenhOn.setText(_translate("svDieuHoa", "Học lệnh\nON"))
        self.btHocLenhOff.setText(_translate("svDieuHoa", "Học lệnh\nOFF"))
        self.btHocLenhDKNhiet.setText(_translate("svDieuHoa", "Học lệnh\nđk nhiệt"))
        self.btHocLenhTatQuat.setText(_translate("svDieuHoa", "Học lệnh\ntắt quạt"))
        self.btHocLenhBatQuat.setText(_translate("svDieuHoa", "Học lệnh\nbật quạt"))
        self.btBack.setText(_translate("svDieuHoa", "Quay lại"))
        self.btTatQuat.setText(_translate("svDieuHoa", "Tắt quạt"))
        self.btTatDieuHoa.setText(_translate("svDieuHoa", "Tắt\nđiều hòa"))
        self.btBatDieuHoa.setText(_translate("svDieuHoa", "Bật\nđiều hòa"))
        self.btBatQuat.setText(_translate("svDieuHoa", "Bật quạt"))
        self.btDatNhietDo.setText(_translate("svDieuHoa", "Đặt\nnhiệt độ"))

        self.setEvent()

    def setEvent(self):
        self.tbInput.setText('20')
        self.btHoc = None
        self.btDieuKhien = None
        self.btBack.clicked.connect(self.btBack_click)
        self.InitUSB()
        if self.serOK == False:
            return
        
        self.tbInput.clicked.connect(self.tbInput_click)

        self.btHocLenhOn.clicked.connect(self.btHocLenhOn_click)
        self.btHocLenhOff.clicked.connect(self.btHocLenhOff_click)
        self.btHocLenhDKNhiet.clicked.connect(self.btHocLenhDKNhiet_click)
        self.btHocLenhTatQuat.clicked.connect(self.btHocLenhTatQuat_click)
        self.btHocLenhBatQuat.clicked.connect(self.btHocLenhBatQuat_click)

        self.btTatQuat.clicked.connect(self.btTatQuat_click)
        self.btTatDieuHoa.clicked.connect(self.btTatDieuHoa_click)
        self.btBatDieuHoa.clicked.connect(self.btBatDieuHoa_click)
        self.btBatQuat.clicked.connect(self.btBatQuat_click)
        self.btDatNhietDo.clicked.connect(self.btDatNhietDo_click)
        self.isRunThread = True
        t1 = threading.Thread(target=self.checkReceive)
        t1.start()

    def tbInput_click(self):
        dialogKey= Ui_Dialog(31)
        value = dialogKey.exec_()
        if value :
            if int(value) < 16:
                self.tbInput.setText("16")
                
            self.tbInput.setText(value)
        self.tbInput.setStyleSheet("background-color: #b6ffb2") #b6ffb2  #81D4FA

    def btHocLenhBatQuat_click(self):
        self.returnColor()
        self.btHoc = self.btHocLenhBatQuat
        self.sentData(b'\x31\x32\x00\x00\x00\x00\x00\x00')
        

    def btHocLenhDKNhiet_click(self):
        self.returnColor()
        self.btHoc = self.btHocLenhDKNhiet
        dt = struct.pack('B',int(self.tbInput.text()))
        self.sentData(b'\x31' + dt + b'\x00\x00\x00\x00\x00\x00')
        

    def btHocLenhOff_click(self):
        self.returnColor()
        self.btHoc = self.btHocLenhOff
        self.sentData(b'\x31\x30\x00\x00\x00\x00\x00\x00')
        
    def btHocLenhOn_click(self):
        self.returnColor()
        self.btHoc = self.btHocLenhOn
        self.sentData(b'\x31\x31\x00\x00\x00\x00\x00\x00')
        
        
    def btHocLenhTatQuat_click(self):
        self.returnColor()
        self.btHoc = self.btHocLenhTatQuat
        self.sentData(b'\x31\x33\x00\x00\x00\x00\x00\x00')
        


    def btBatDieuHoa_click(self):
        self.returnColor()
        self.btDieuKhien = self.btBatDieuHoa
        self.btHoc = None
        self.sentData(b'\x30\x31\x00\x00\x00\x00\x00\x00')
        
    def btTatDieuHoa_click(self):
        self.returnColor()
        self.btDieuKhien = self.btTatDieuHoa
        self.btHoc = None
        self.sentData(b'\x30\x30\x00\x00\x00\x00\x00\x00')
        
       
    def btDatNhietDo_click(self):
        self.returnColor()
        dt = struct.pack('B',int(self.tbInput.text()))
        self.btDieuKhien = self.btDatNhietDo
        self.btHoc = None
        self.sentData(b'\x30' + dt + b'\x00\x00\x00\x00\x00\x00')
        
        
    def btBatQuat_click(self):
        self.returnColor()
        self.btDieuKhien = self.btBatQuat
        self.btHoc = None
        self.sentData(b'\x30\x32\x00\x00\x00\x00\x00\x00')
        
        
    def btTatQuat_click(self):
        self.returnColor()
        self.btDieuKhien = self.btTatQuat
        self.btHoc = None
        self.sentData(b'\x30\x33\x00\x00\x00\x00\x00\x00')
        
    def returnColor(self):
        if self.btDieuKhien != None:
            self.btDieuKhien.setStyleSheet("background-color: #9bff5d")
            #tra lai mau ban dau cho button

    def btBack_click(self):
        self.isRunThread = False
        if self.serOK:
            self.ser.close()
        self.svDieuHoa.close()

    def InitUSB(self):
        try :
            self.ser = serial.Serial(
                port = server.usbDieuHoa,
                baudrate = 9600,
                parity = serial.PARITY_NONE,
                stopbits = serial.STOPBITS_ONE,
                bytesize = serial.EIGHTBITS,
                timeout = 1
            )
            self.serOK = True
        except Exception as e:
            print("Exception in InitUSB : ",e)
            self.serOK = False
            
    def sentData(self,data2):
        if self.serOK == False :
            print("Error in Serial")
            return
        if self.btHoc != None :
            #khi an thi mau vang
            self.btHoc.setStyleSheet("background-color: #ffff00")
            self.btDieuKhien = None

        if self.btDieuKhien != None :
            #khi an thi mau vang
            self.btDieuKhien.setStyleSheet("background-color: #ffff00")
            self.btHoc = None

        crcData = b'\x00\x00'
        dataSent = b'\xee\xee' + data2 + crcData
        self.ser.write(dataSent)
        self.ser.flush()

    def checkReceive(self):
        if self.serOK == False:
            return
        while self.isRunThread :
            dt = self.ser.read(3)
            if len(dt) == 3 :
                #ERR ff5f2e
                if dt[0] == 0x45 and dt[1] == 0x52 and dt[2] == 0x52 :
                    #self.tbInput.setStyleSheet("background-color: #ff5f2e")
                    self.buttonClicked.setStyleSheet("background-color: #ff5f2e")
                elif dt[0] == 0x41 and dt[1] == 0x43 and dt[2] == 0x4b:
                    if self.btDieuKhien != None :
                        self.btDieuKhien.setStyleSheet("background-color: #ff0000")
                    if self.btHoc != None :
                        self.btHoc.setStyleSheet("background-color: #ff0000")
                    
                    #self.tbInput.setStyleSheet("background-color: #81D4FA")
                else:
                    print("dataReceive not ACK or ERR : ",dt)
        print("Thread recived dieu khien dieu hoa close : ")

import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    svDieuHoa = QtWidgets.QWidget()
    ui = Ui_svDieuHoa()
    ui.setupUi(svDieuHoa)
    svDieuHoa.show()
    sys.exit(app.exec_())

"""