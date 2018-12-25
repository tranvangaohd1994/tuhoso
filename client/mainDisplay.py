# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent

from formWaiting import Ui_FormWaiting
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
from CL_CaiDatPhuTro import Ui_CL_CaiDatPhuTro
from SV_CanhBao import Ui_SV_CanhBao
from BaoDuongClient import Ui_BaoDuongClient
from formKhoaDC import Ui_FormKhoaDC
from time import strftime
import client
import resources
import time


class Ui_SV_mainDisplay(QMainWindow):
    def __init__(self):
        super(Ui_SV_mainDisplay,self).__init__()
    def setupUi(self):
        SV_mainDisplay = self
        SV_mainDisplay.setObjectName("SV_mainDisplay")
        SV_mainDisplay.resize(1280, 800)
        SV_mainDisplay.setStyleSheet(".QFrame{background-image: url(:/images/mainLayout.png);}")
        self.centralwidget = QtWidgets.QWidget(SV_mainDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 10px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(620, 550, 581, 111))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Ubuntu\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}")
        self.grTempOut.setTitle("")
        self.grTempOut.setObjectName("grTempOut")
        self.lbTempOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempOutValue.setGeometry(QtCore.QRect(210, 60, 81, 45))
        self.lbTempOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempOutValue.setObjectName("lbTempOutValue")
        self.lbHumiOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiOutValue.setGeometry(QtCore.QRect(460, 60, 91, 45))
        self.lbHumiOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiOutValue.setObjectName("lbHumiOutValue")
        self.lbTempInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempInValue.setGeometry(QtCore.QRect(210, 20, 81, 45))
        self.lbTempInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempInValue.setObjectName("lbTempInValue")
        self.lbHumiInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiInValue.setGeometry(QtCore.QRect(460, 20, 91, 45))
        self.lbHumiInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiInValue.setObjectName("lbHumiInValue")
        self.grStatusMotor = QtWidgets.QGroupBox(self.frame)
        self.grStatusMotor.setGeometry(QtCore.QRect(100, 250, 481, 171))
        self.grStatusMotor.setStyleSheet(".QLabel{color :#ff0000;font: bold 22pt \"Arial\";}")
        self.grStatusMotor.setTitle("")
        self.grStatusMotor.setObjectName("grStatusMotor")
        self.lbTrongKho = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrongKho.setGeometry(QtCore.QRect(160, 50, 101, 45))
        self.lbTrongKho.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTrongKho.setObjectName("lbTrongKho")
        self.lbChoMuon = QtWidgets.QLabel(self.grStatusMotor)
        self.lbChoMuon.setGeometry(QtCore.QRect(160, 100, 101, 45))
        self.lbChoMuon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbChoMuon.setObjectName("lbChoMuon")
        self.btKiemTra = QtWidgets.QPushButton(self.grStatusMotor)
        self.btKiemTra.setGeometry(QtCore.QRect(280, 60, 161, 81))
        self.btKiemTra.setObjectName("btKiemTra")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 101, 81))
        self.btExit.setStyleSheet("border: none;background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grControl = QtWidgets.QGroupBox(self.frame)
        self.grControl.setGeometry(QtCore.QRect(90, 370, 461, 411))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(54, 248, 161, 80))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btCaiDat = QtWidgets.QPushButton(self.grControl)
        self.btCaiDat.setGeometry(QtCore.QRect(254, 248, 161, 80))
        self.btCaiDat.setObjectName("btCaiDat")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(254, 50, 161, 80))
        self.btDongTu.setObjectName("btDongTu")
        self.btKhoaDC = QtWidgets.QPushButton(self.grControl)
        self.btKhoaDC.setGeometry(QtCore.QRect(54, 150, 161, 80))
        self.btKhoaDC.setObjectName("btKhoaDC")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(254, 150, 161, 80))
        self.btTraCuu.setObjectName("btTraCuu")
        self.btMoTu = QtWidgets.QPushButton(self.grControl)
        self.btMoTu.setGeometry(QtCore.QRect(54, 50, 161, 80))
        self.btMoTu.setObjectName("btMoTu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(610, 230, 581, 301))
        self.grWarning.setStyleSheet(".QLabel{color: rgb(255, 0, 0);font: Bold 22pt \"Arial\";}")
        self.grWarning.setTitle("")
        self.grWarning.setObjectName("grWarning")
        self.lbKhoangCach = QtWidgets.QLabel(self.grWarning)
        self.lbKhoangCach.setGeometry(QtCore.QRect(240, 104, 141, 45))
        self.lbKhoangCach.setAlignment(QtCore.Qt.AlignCenter)
        self.lbKhoangCach.setObjectName("lbKhoangCach")
        self.lbstatusMotor = QtWidgets.QLabel(self.grWarning)
        self.lbstatusMotor.setGeometry(QtCore.QRect(200, 55, 281, 45))
        self.lbstatusMotor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbstatusMotor.setObjectName("lbstatusMotor")
        self.lbSoNguoi = QtWidgets.QLabel(self.grWarning)
        self.lbSoNguoi.setGeometry(QtCore.QRect(250, 153, 121, 41))
        self.lbSoNguoi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSoNguoi.setObjectName("lbSoNguoi")
        self.lbWarning = QtWidgets.QLabel(self.grWarning)
        self.lbWarning.setGeometry(QtCore.QRect(160, 183, 421, 71))
        self.lbWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWarning.setObjectName("lbWarning")
        self.btXemChiTiet = QtWidgets.QPushButton(self.frame)
        self.btXemChiTiet.setGeometry(QtCore.QRect(788, 660, 241, 61))
        self.btXemChiTiet.setObjectName("btXemChiTiet")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self, SV_mainDisplay):
        _translate = QtCore.QCoreApplication.translate
        SV_mainDisplay.setWindowTitle(_translate("SV_mainDisplay", "MainWindow"))
        self.SV_mainDisplay = SV_mainDisplay        
        self.lbTempOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTrongKho.setText(_translate("SV_mainDisplay", "0"))
        self.lbChoMuon.setText(_translate("SV_mainDisplay", "0"))
        self.btKhoaDC.setText(_translate("SV_mainDisplay", "Khóa ĐC"))
        self.btKiemTra.setText(_translate("SV_mainDisplay", "Kiểm tra"))
        self.btTroGiup.setText(_translate("SV_mainDisplay", "Trợ giúp"))
        self.btCaiDat.setText(_translate("SV_mainDisplay", "Cài đặt"))
        self.btDongTu.setText(_translate("SV_mainDisplay", "Đóng giá"))
        self.btTraCuu.setText(_translate("SV_mainDisplay", "Tra cứu"))
        self.btMoTu.setText(_translate("SV_mainDisplay", "Mở giá"))
        self.lbKhoangCach.setText(_translate("SV_mainDisplay", "0"))
        self.lbstatusMotor.setText(_translate("SV_mainDisplay", "Đóng"))
        self.lbSoNguoi.setText(_translate("SV_mainDisplay", "0"))
        self.lbWarning.setText(_translate("SV_mainDisplay", "a"))
        self.btXemChiTiet.setText(_translate("SV_mainDisplay", "Xem chi tiết"))

        self.initDisplay()

    def initDisplay(self):

        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.showTemp)
        self.ctimer.start(1000)
        self.setEvent()
        self.isShowDialog = False
        self.isShowSuCoForm = False
        self.isShowBaoDuong =False
        self.isShowFormKhoaDC = False
        client.caseBD = -1

        #get mouse event
        self.xS = self.xE = 0
        self.yS = self.yE = 0
        self.lengthMouse = 80
    
    def mousePressEvent(self,ev):
        self.xS = ev.pos().x()
        self.yS = ev.pos().y()
        #print('mousePress  ',self.xS, self.yS)
    
    def mouseReleaseEvent(self,ev):
        self.xE = ev.pos().x()
        self.yE = ev.pos().y()
        difX = self.xE - self.xS
        difY = self.yE - self.yS

        if difX > self.lengthMouse :
            client.ThClientMain.sent2Server(b'\xcc\xc0')
            print("swipe right")
        elif difX < - self.lengthMouse:
            client.ThClientMain.sent2Server(b'\xcc\xc1')
            print("swipe left")
        elif difY > self.lengthMouse :
            client.ThClientMain.sent2Server(b'\xcc\xc2')
            print("swipe down")
        elif difY < - self.lengthMouse :
            client.ThClientMain.sent2Server(b'\xcc\xc3')
            print('swipr Up')

    def showTemp(self):
        try:
            self.lbHumiInValue.setText(str(client.dataReceved.humiIn))
            self.lbTempInValue.setText(str(client.dataReceved.tempIn))
         
            self.lbTempOutValue.setText(str(client.dataReceved.tempOut))
            self.lbHumiOutValue.setText(str(client.dataReceved.humiOut))
            self.lbKhoangCach.setText(str(client.dataReceved.distanceSen_Real))
            self.lbWarning.setText(str(client.listCanhBao[client.dataCanhBao]))
            self.lbSoNguoi.setText(str(client.dataReceved.numPersonIn))

            #button khoa dong co hay khong
            if client.DataCamBien[5] == 0x30:
                self.btKhoaDC.setText("Khóa ĐC")
                self.btKhoaDC.setStyleSheet('color:white')
                self.isKhoa = 0
            elif client.DataCamBien[5] == 0x31:
                self.btKhoaDC.setText("Mở ĐC")
                self.btKhoaDC.setStyleSheet('color:red')
                self.isKhoa = 1
            #save nhiet do do am 
            minitue = int(strftime("%M"))
            if minitue % 10 == 0 :
                if self.saveLog :
                    self.saveLog = False
                    client.saveNhietDoDoAm()
            else :
                self.saveLog = True
                
            #Status motor
            if client.dataReceved.statusMotor == 2:
                self.lbstatusMotor.setText("Mở")
            elif client.dataReceved.statusMotor == 4:
                self.lbstatusMotor.setText("Đóng")
            elif client.dataReceved.statusMotor == 5:
                self.lbstatusMotor.setText("Dừng")
            else :
                self.lbstatusMotor.setText("")  

            if client.isActive2Ser == False:
                self.ctimer.stop()
                self.SV_mainDisplay.close()

            #che do bao duong se ko cho cac che do khac hoat dong nen return
            if client.caseBD >= 0:
                if self.isShowBaoDuong == False :
                    self.isShowBaoDuong = True
                    self.callBaoDuongForm()
                return 
            else :
                self.isShowBaoDuong = False

            print("statusSuCo = ", client.statusSuCo, " isWaiting = ", client.isWaiting,"statusMotor = ",client.dataReceved.statusMotor)
            #client check xem có cháy ko nếu có cháy hiện màn cảnh báo có cháy
            if client.statusSuCo == 0:
                self.isShowSuCoForm = False

            if client.statusSuCo == 2 or client.statusSuCo == 3:
                if self.isShowSuCoForm == False :
                    self.isShowSuCoForm = True
                    self.callSuCoForm()
                return            
            #check su co co nguoi trong tu hay khong hoac co gia sach nho
            if client.isWaiting == 3 and (client.statusSuCo == 1 or client.statusSuCo == 4):
                if self.isShowSuCoForm == False :
                    self.isShowSuCoForm = True
                    self.callSuCoForm()
                return
            
            if client.isWaiting != 3 or client.statusSuCo !=5 :
                self.isShowFormKhoaDC = False
            if client.isWaiting == 3 and client.statusSuCo == 5 :
                if self.isShowFormKhoaDC == False :
                    self.isShowFormKhoaDC = True
                    self.callFormKhoaDC()
                return
            #hiện màn waiting dong tu co nguoi ben trong
            if client.isWaiting == 0 or client.isWaiting == 2:
                self.isShowDialog = False
            elif client.isWaiting == 1 :
                if self.isShowDialog == False :
                    self.isShowDialog = True
                    self.callWaitingForm()
       
        except Exception as e:
            print("ERROR IN mainDisplay->showTemp : ",e.__doc__)
            client.loggerInfor.info('ERROR IN mainDisplay->showTemp : ', e.__doc__)
    def setEvent(self):
        self.NumExit=0
        self.isKhoa = 0
        
        self.btDongTu.clicked.connect(self.btDongTu_click)
        self.btExit.clicked.connect(self.btExit_click)
        self.btMoTu.clicked.connect(self.btMoTu_click)

        self.btKiemTra.clicked.connect(self.btKiemTra_click)
        self.btKhoaDC.clicked.connect(self.btKhoaDC_click)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.btTroGiup.clicked.connect(self.btTroGiup_click)
        self.btCaiDat.clicked.connect(self.btCaiDat_click)
        self.btClickTimer = False
    #de chong doi phim bam
    def buttonTimer(self):
        self.btTimer = QTimer(self.frame)
        self.btTimer.timeout.connect(self.stopButtonTimer)
        self.btTimer.start(500)
        self.btClickTimer = True
    def stopButtonTimer(self):
        self.btTimer.stop()
        self.btClickTimer = False
        print("stopButtonTimer - button is actived")
    
    def btDongTu_click(self,bbb):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        client.ThClientMain.sent2Server(b'\xee\xff')
        
    def btMoTu_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()
            
        client.ThClientMain.sent2Server(b'\xee\xee')
    def btExit_click(self):
        self.NumExit +=1
        if self.NumExit == 3 :
            self.ctimer.stop()
            self.SV_mainDisplay.close()
        pass
    
    def btKiemTra_click(self):
        pass
    def btKhoaDC_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        self.isKhoa += 1
        print("Khoa  dc", self.isKhoa)

        for i in range(0,8):
            client.DataCamBien[i] = 0x00

        if self.isKhoa == 2:
            client.DataCamBien[5] = 0x30
            self.btKhoaDC.setText("Khóa ĐC")
            self.isKhoa = 0
            client.sentCambien()
            
        if self.isKhoa == 1:
            
            self.btKhoaDC.setText("Mở ĐC")
            client.DataCamBien[5] = 0x31
            client.sentCambien()
        pass

    def btTraCuu_click(self):
        pass
    def btTroGiup_click(self):
        pass
    def btCaiDat_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_CL_CaiDatPhuTro()
        self.ui.setupUi(self.window)
        self.window.show()
        if client.isFullScreen:
            self.window.showFullScreen()
        
        pass
    def callFormKhoaDC(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FormKhoaDC()
        self.ui.setupUi(self.window)
        self.window.show()
        if client.isFullScreen:
            self.window.showFullScreen()
    def callWaitingForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_FormWaiting()
        self.ui.setupUi(self.window)
        self.window.show()
        if client.isFullScreen:
            self.window.showFullScreen()
    
    def callSuCoForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SV_CanhBao()
        self.ui.setupUi(self.window)
        self.window.show()
        if client.isFullScreen:
            self.window.showFullScreen()
    def callBaoDuongForm(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_BaoDuongClient()
        self.ui.setupUi(self.window)
        self.window.show()
        if client.isFullScreen:
            self.window.showFullScreen()
        
