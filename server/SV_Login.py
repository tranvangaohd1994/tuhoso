# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_Login.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget,QLineEdit,QDialog ,QGridLayout, QLabel,QPushButton,QMainWindow,QApplication,QWidget,QHBoxLayout)
from PyQt5.QtCore import pyqtSignal,QTimer
from keyboard import Ui_Keyboard
#from mainDisplay import Ui_SV_mainDisplay
from SV_ChonTuCaiDat import Ui_SVChonClient
import resources
import uart
from pygame import mixer
import threading
import server
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
from pirc522 import RFID
import time

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_SVLogin(object):
    def setupUi(self, SV_Login):
        SV_Login.setObjectName("SV_Login")
        SV_Login.resize(1280, 800)
        self.SV_Login = SV_Login

        self.frame = QtWidgets.QFrame(SV_Login)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/Background.jpg);}#lbtitle{color:#F44336 ;font: 75  36pt \"Arial\";}#lbThongBao{color:#F44336 ;font: 75  34pt \"Arial\";}#lbtitle2{color:#2196F3 ;font: 75  30pt \"Arial\";}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(400, 130, 471, 71))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(570, 530, 191, 101))
        self.btBack.setObjectName("btBack")
        self.tbInput = MyQLineEdit(self.frame)
        self.tbInput.setGeometry(QtCore.QRect(430, 330, 421, 71))
        self.tbInput.setObjectName("tbInput")
        self.lbtitle2 = QtWidgets.QLabel(self.frame)
        self.lbtitle2.setGeometry(QtCore.QRect(450, 260, 381, 61))
        self.lbtitle2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle2.setObjectName("lbtitle2")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(160, 440, 961, 51))
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setObjectName("lbThongBao")
        

        self.retranslateUi(SV_Login)
        QtCore.QMetaObject.connectSlotsByName(SV_Login)

        self.btBack.clicked.connect(SV_Login.close)
    def retranslateUi(self, SV_Login):
        _translate = QtCore.QCoreApplication.translate
        SV_Login.setWindowTitle(_translate("SV_Login", "Form"))
        self.lbtitle.setText(_translate("SV_Login", "Giao diện quản lý"))
        self.btBack.setText(_translate("SV_Login", "Quay lại"))
        self.lbThongBao.setText("Có thể quẹt thẻ RFID hoặc quét vân tay")
        self.lbtitle2.setText(_translate("SV_Login", "Nhập mật khẩu"))

        self.setEvent()
       
    def setEvent(self):
        self.tbInput.clicked.connect(self.tbInput_click)
       
        self.linkFile = server.folderMP3 + "002.mp3"
        server.playmp3(self.linkFile)
        #lock de dong bo thread
        self.threadLock = threading.Lock()
        self.isRun = True
        self.isRunRFID = True
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkScanOK)
        self.ctimer.start(10)
        

        
        t1 = threading.Thread(target=self.runThreadSensor)
        t1.start()
        """
        t2RFID = threading.Thread(target=self.runRFID)
        t2RFID.start()
        """

    def checkScanOK(self):
        if self.isRun == False:
            self.dangNhap()
        
    def runThreadSensor(self):
        while self.isRun:
            if self.isRunRFID :
                self.threadLock.acquire()
                self.rdr = RFID()
                self.runRFID()
                self.rdr.cleanup()
                self.isRunRFID=False
                self.threadLock.release()
            else :
                self.runScan()
                self.isRunRFID = True

    def runScan(self):
                    
        try:
            f = PyFingerprint(server.usbFinger, 57600, 0xFFFFFFFF, 0x00000000)
            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')
            print("pass van tay lan 1")

        except Exception as e:
            try :
                f = PyFingerprint(server.usbDieuHoa, 57600, 0xFFFFFFFF, 0x00000000)
                if ( f.verifyPassword() == False ):
                    raise ValueError('The given fingerprint sensor password is wrong!')
                tempUSB = server.usbDieuHoa
                server.usbDieuHoa =  server.usbFinger
                server.usbFinger = tempUSB
                print("pass van tay lan 2")
            except Exception as e:
                print('The fingerprint sensor could not be initialized!')
                print('Exception message: ' + str(e))
                self.lbThongBao.setText("Kiểm Tra cảm biến vân tay")
                return
        print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
        try:
            print('Waiting for finger...')
            ## Wait that finger is read
            numC = 0
            while ( f.readImage() == False and self.isRun):
                numC+=1
                if numC > 20 :
                    return
            ## Converts read image to characteristics and stores it in charbuffer 1
            if self.isRun == False:
                return
            f.convertImage(0x01)
            ## Searchs template
            result = f.searchTemplate()
            positionNumber = result[0]
            accuracyScore = result[1]

            if ( positionNumber == -1 ):
                print('No match found!')
                self.lbThongBao.setText("Vân tay không khớp")
                
            else:
                print('Khop van tay')
                self.isRun = False
                return
                
        except Exception as e:
            self.lbThongBao.setText("Kiểm Tra cảm biến vân tay")
            print('Operation failed!')
            print('Exception message: ' + str(e))

    def runRFID(self):
        print("Starting RFID")
        loop = 5
        while loop > 0 and self.isRun:
            loop -= 1
            try:
                util = self.rdr.util()
                #rdr.wait_for_tag()

                (error, data) = self.rdr.request()
                if not error:
                    print("\nDetected: " + format(data, "02x"))

                (error, uid) = self.rdr.anticoll()
                if not error:
                    print("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
                    print("Setting tag")
                    util.set_tag(uid)
                    print("\nAuthorizing")
                    #util.auth(rdr.auth_a, [0x12, 0x34, 0x56, 0x78, 0x96, 0x92])
                    util.auth(self.rdr.auth_b, [0x74, 0x00, 0x52, 0x35, 0x00, 0xFF])
                    print("\nReading")
                    util.read_out(4)
                    print("\nDeauthorizing")
                    util.deauth()
                    #set active open new form
                    self.isRun = False
                time.sleep(0.01)
            except Exception as e:
                print('Exception RFID: ' + str(e))

    def tbInput_click(self):
        dialogKey = Ui_Keyboard()
        value = dialogKey.exec_()
        self.tbInput.setText(value)
        if value == '1994':
            server.isExitApp = True
            self.SV_Login.close()
        elif value == uart.dtMK or value == uart.dtMKHard:
            self.isRun = False
            self.dangNhap()
        else :
            self.lbThongBao.setText("Nhập sai mật khẩu")
    def dangNhap(self):
        self.ctimer.stop()
        self.lbThongBao.setText("")
        server.userLogin = True
        server.serverMain.sentLogin2AllClient()
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SVChonClient()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen:
            self.window.showFullScreen()
        self.SV_Login.close()


import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVCaiDatPhuTro = QtWidgets.QWidget()
    ui = Ui_SVCaiDatPhuTro()
    ui.setupUi(SVCaiDatPhuTro)
    SVCaiDatPhuTro.show()
    sys.exit(app.exec_())

"""