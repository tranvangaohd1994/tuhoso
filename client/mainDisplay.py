# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from formWaiting import Ui_FormWaiting
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
from CL_CaiDatPhuTro import Ui_CL_CaiDatPhuTro
from SV_CanhBao import Ui_SV_CanhBao
from BaoDuongClient import Ui_BaoDuongClient
from time import strftime
import client
import resources
import time


class Ui_SV_mainDisplay(object):
    def setupUi(self, SV_mainDisplay):
        SV_mainDisplay.setObjectName("SV_mainDisplay")
        SV_mainDisplay.resize(1280, 800)
        SV_mainDisplay.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}")
        self.centralwidget = QtWidgets.QWidget(SV_mainDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTopMain = QtWidgets.QGroupBox(self.frame)
        self.grTopMain.setGeometry(QtCore.QRect(0, 729, 1281, 71))
        self.grTopMain.setStyleSheet("#grTopMain{ border: 0px solid gray; border-radius: 0px; }.QLabel {font: 57 22pt \"Arial\";color: rgb(255, 255, 255);}")
        self.grTopMain.setTitle("")
        self.grTopMain.setObjectName("grTopMain")
        self.label = QtWidgets.QLabel(self.grTopMain)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.grTopMain)
        self.label_2.setGeometry(QtCore.QRect(530, -1, 741, 61))
        
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(690, 120, 581, 171))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Arial\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 22pt \"Arial\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}")
        self.grTempOut.setTitle("")
        self.grTempOut.setObjectName("grTempOut")
        self.lbTempIn_2 = QtWidgets.QLabel(self.grTempOut)
        self.lbTempIn_2.setGeometry(QtCore.QRect(10, 60, 201, 45))
        self.lbTempIn_2.setObjectName("lbTempIn_2")
        self.lbHumiIn_2 = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiIn_2.setGeometry(QtCore.QRect(300, 60, 191, 45))
        self.lbHumiIn_2.setObjectName("lbHumiIn_2")
        self.lbTempOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempOutValue.setGeometry(QtCore.QRect(210, 60, 81, 45))
        self.lbTempOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempOutValue.setObjectName("lbTempOutValue")
        self.lbHumiOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiOutValue.setGeometry(QtCore.QRect(500, 60, 81, 45))
        self.lbHumiOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiOutValue.setObjectName("lbHumiOutValue")
        self.lbTempInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempInValue.setGeometry(QtCore.QRect(210, 20, 81, 45))
        self.lbTempInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempInValue.setObjectName("lbTempInValue")
        self.lbTempIn = QtWidgets.QLabel(self.grTempOut)
        self.lbTempIn.setGeometry(QtCore.QRect(10, 20, 201, 45))
        self.lbTempIn.setObjectName("lbTempIn")
        self.lbHumiInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiInValue.setGeometry(QtCore.QRect(500, 20, 81, 45))
        self.lbHumiInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiInValue.setObjectName("lbHumiInValue")
        self.lbHumiIn = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiIn.setGeometry(QtCore.QRect(300, 20, 191, 41))
        self.lbHumiIn.setObjectName("lbHumiIn")
        self.grStatusMotor = QtWidgets.QGroupBox(self.frame)
        self.grStatusMotor.setGeometry(QtCore.QRect(10, 120, 481, 171))
        self.grStatusMotor.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75  20pt \"Arial\";}\n"
                "#lbTrangThaiLuuTru{color:#FFFF00 ;font: 75  22pt \"Arial\";}\n"
                "#lbChoMuon{color :#D500F9;font:75 22pt \"Arial\";}\n"
                "#lbTrongKho{color :#D500F9;font:75  22pt \"Arial\";}\n"
                "")
        self.grStatusMotor.setTitle("")
        self.grStatusMotor.setObjectName("grStatusMotor")
        self.lbTrangThaiLuuTru = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrangThaiLuuTru.setGeometry(QtCore.QRect(110, 5, 251, 31))
        self.lbTrangThaiLuuTru.setObjectName("lbTrangThaiLuuTru")
        self.lbTrongKho = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrongKho.setGeometry(QtCore.QRect(160, 50, 101, 45))
        self.lbTrongKho.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTrongKho.setObjectName("lbTrongKho")
        self.lbTempIn_9 = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTempIn_9.setGeometry(QtCore.QRect(10, 50, 141, 45))
        self.lbTempIn_9.setObjectName("lbTempIn_9")
        self.lbChoMuon = QtWidgets.QLabel(self.grStatusMotor)
        self.lbChoMuon.setGeometry(QtCore.QRect(160, 100, 101, 45))
        self.lbChoMuon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbChoMuon.setObjectName("lbChoMuon")
        self.lbTempIn_10 = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTempIn_10.setGeometry(QtCore.QRect(10, 100, 141, 45))
        self.lbTempIn_10.setObjectName("lbTempIn_10")
        self.btKiemTra = QtWidgets.QPushButton(self.grStatusMotor)
        self.btKiemTra.setGeometry(QtCore.QRect(310, 50, 161, 91))
        self.btKiemTra.setObjectName("btKiemTra")
        self.grControl = QtWidgets.QGroupBox(self.frame)
        self.grControl.setGeometry(QtCore.QRect(0, 290, 561, 441))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(10, 300, 171, 101))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btCaiDat = QtWidgets.QPushButton(self.grControl)
        self.btCaiDat.setGeometry(QtCore.QRect(320, 300, 171, 101))
        self.btCaiDat.setObjectName("btCaiDat")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(320, 20, 171, 101))
        self.btDongTu.setObjectName("btDongTu")
        self.btMoTu = QtWidgets.QPushButton(self.grControl)
        self.btMoTu.setGeometry(QtCore.QRect(10, 20, 171, 101))
        self.btMoTu.setObjectName("btMoTu")
        self.btKhoaDC = QtWidgets.QPushButton(self.grControl)
        self.btKhoaDC.setGeometry(QtCore.QRect(10, 160, 171, 101))
        self.btKhoaDC.setObjectName("btKhoaDC")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(320, 160, 171, 101))
        self.btTraCuu.setObjectName("btTraCuu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(690, 310, 581, 371))
        self.grWarning.setStyleSheet("#lbWarning{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbCanhBao{color:#FFFF00 ;font: 75  22pt \"Arial\";}.QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Arial\";}#lbKhoangCach{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbstatusMotor{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbSoNguoi{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}")
        self.grWarning.setTitle("")
        self.grWarning.setObjectName("grWarning")
        self.lbCanhBao = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao.setGeometry(QtCore.QRect(160, 5, 271, 41))
        self.lbCanhBao.setObjectName("lbCanhBao")
        self.lbTempIn_7 = QtWidgets.QLabel(self.grWarning)
        self.lbTempIn_7.setGeometry(QtCore.QRect(390, 140, 81, 45))
        self.lbTempIn_7.setObjectName("lbTempIn_7")
        self.lbKhoangCach = QtWidgets.QLabel(self.grWarning)
        self.lbKhoangCach.setGeometry(QtCore.QRect(270, 140, 111, 45))
        self.lbKhoangCach.setText("")
        self.lbKhoangCach.setAlignment(QtCore.Qt.AlignCenter)
        self.lbKhoangCach.setObjectName("lbKhoangCach")
        self.lbHumiIn_3 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_3.setGeometry(QtCore.QRect(10, 140, 191, 41))
        self.lbHumiIn_3.setObjectName("lbHumiIn_3")
        self.lbstatusMotor = QtWidgets.QLabel(self.grWarning)
        self.lbstatusMotor.setGeometry(QtCore.QRect(220, 50, 201, 45))
        self.lbstatusMotor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbstatusMotor.setObjectName("lbstatusMotor")
        self.lbSoNguoi = QtWidgets.QLabel(self.grWarning)
        self.lbSoNguoi.setGeometry(QtCore.QRect(250, 95, 141, 45))
        self.lbSoNguoi.setText("")
        self.lbSoNguoi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSoNguoi.setObjectName("lbSoNguoi")
        self.lbHumiIn_4 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_4.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.lbHumiIn_4.setObjectName("lbHumiIn_4")
        self.lbHumiIn_5 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_5.setGeometry(QtCore.QRect(10, 95, 231, 41))
        self.lbHumiIn_5.setObjectName("lbHumiIn_5")
        self.lbWarning = QtWidgets.QLabel(self.grWarning)
        self.lbWarning.setGeometry(QtCore.QRect(10, 244, 561, 101))
        self.lbWarning.setText("")
        self.lbWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWarning.setObjectName("lbWarning")
        self.lbCanhBao_2 = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao_2.setGeometry(QtCore.QRect(10, 190, 211, 41))
        self.lbCanhBao_2.setObjectName("lbCanhBao_2")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 71, 75))
        self.btExit.setStyleSheet("border: none;background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grTopMain.raise_()
        self.grTempOut.raise_()
        self.grStatusMotor.raise_()
        self.grControl.raise_()
        self.grWarning.raise_()
        self.btExit.raise_()
        self.label_2.raise_()
        SV_mainDisplay.setCentralWidget(self.centralwidget)

        self.retranslateUi(SV_mainDisplay)
        QtCore.QMetaObject.connectSlotsByName(SV_mainDisplay)
        self.setEvent()

    def retranslateUi(self, SV_mainDisplay):
        _translate = QtCore.QCoreApplication.translate
        SV_mainDisplay.setWindowTitle(_translate("SV_mainDisplay", "MainWindow"))
        self.SV_mainDisplay = SV_mainDisplay
        self.label.setText(_translate("SV_mainDisplay", "Tủ 2"))
        self.lbTempIn_2.setText(_translate("SV_mainDisplay", "Nhiệt độ ngoài : "))
        self.lbHumiIn_2.setText(_translate("SV_mainDisplay", "Độ ẩm ngoài : "))
        self.lbTempOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempIn.setText(_translate("SV_mainDisplay", "Nhiệt độ trong : "))
        self.lbHumiInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiIn.setText(_translate("SV_mainDisplay", "Độ ẩm trong :"))
        self.lbTrangThaiLuuTru.setText(_translate("SV_mainDisplay", "Trạng thái lưu trữ"))
        self.lbTrongKho.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempIn_9.setText(_translate("SV_mainDisplay", "Trong kho :"))
        self.lbChoMuon.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempIn_10.setText(_translate("SV_mainDisplay", "Cho mượn :"))
        self.btKiemTra.setText(_translate("SV_mainDisplay", "Kiểm tra"))
        self.btTroGiup.setText(_translate("SV_mainDisplay", "Trợ giúp"))
        self.btCaiDat.setText(_translate("SV_mainDisplay", "Cài Đặt"))
        self.btDongTu.setText(_translate("SV_mainDisplay", "Đóng tủ"))
        self.btMoTu.setText(_translate("SV_mainDisplay", "Mở tủ"))
        self.btKhoaDC.setText(_translate("SV_mainDisplay", "Khóa ĐC"))
        self.btTraCuu.setText(_translate("SV_mainDisplay", "Tra cứu"))
        self.lbCanhBao.setText(_translate("SV_mainDisplay", "Trạng thái vận hành"))
        self.lbTempIn_7.setText(_translate("SV_mainDisplay", "cm"))
        self.lbKhoangCach.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiIn_3.setText(_translate("SV_mainDisplay", "Khoảng cách :"))
        self.lbstatusMotor.setText(_translate("SV_mainDisplay", ""))
        self.lbSoNguoi.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiIn_4.setText(_translate("SV_mainDisplay", "Trạng thái tủ :"))
        self.lbHumiIn_5.setText(_translate("SV_mainDisplay", "Số người trong tủ :"))
        self.lbWarning.setText(_translate("SV_mainDisplay", ""))
        self.lbCanhBao_2.setText(_translate("SV_mainDisplay", "Cảnh báo sự cố :"))

        self.initDisplay()

    def initDisplay(self):

        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.showTemp)
        self.ctimer.start(1000)
        self.setEvent()
        self.isShowDialog = False
        self.isShowSuCoForm = False
        self.isShowBaoDuong =False
        client.caseBD = -1

    def showTemp(self):
        try:
            _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
            self.label_2.setText(str(_date))

            self.lbHumiInValue.setText(str(client.dataReceved.humiIn))
            self.lbTempInValue.setText(str(client.dataReceved.tempIn))
         
            self.lbTempOutValue.setText(str(client.dataReceved.tempOut))
            self.lbHumiOutValue.setText(str(client.dataReceved.humiOut))
            self.lbKhoangCach.setText(str(client.dataReceved.distanceSen_1))
            self.lbWarning.setText(str(client.listCanhBao[client.dataCanhBao]))
            self.lbSoNguoi.setText(str(client.dataReceved.numPersonIn))

            #button khoa dong co hay khong
            if client.DataCamBien[5] == 0x30:
                self.btKhoaDC.setText("Khóa ĐC")
                self.isKhoa = 0
            elif client.DataCamBien[5] == 0x31:
                self.btKhoaDC.setText("Mở ĐC")
                self.isKhoa = 1

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
        
