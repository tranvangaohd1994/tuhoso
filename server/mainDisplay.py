# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from SV_QuanLy import Ui_SVQuanLy
from formWaiting import Ui_FormWaiting
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
from SV_CanhBao import Ui_SV_CanhBao
from kbNumber import Ui_Dialog 
from time import strftime
from formTimKiem import Ui_formTimKiem

import time
import struct
import server
import uart

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
        self.btQuanLy = QtWidgets.QPushButton(self.grControl)
        self.btQuanLy.setGeometry(QtCore.QRect(320, 300, 171, 101))
        self.btQuanLy.setObjectName("btQuanLy")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(320, 20, 171, 101))
        self.btDongTu.setObjectName("btDongTu")
        self.btMoTu = QtWidgets.QPushButton(self.grControl)
        self.btMoTu.setGeometry(QtCore.QRect(10, 20, 171, 101))
        self.btMoTu.setObjectName("btMoTu")
        self.btThongGio = QtWidgets.QPushButton(self.grControl)
        self.btThongGio.setGeometry(QtCore.QRect(10, 160, 171, 101))
        self.btThongGio.setObjectName("btThongGio")
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
    
    def retranslateUi(self, SV_mainDisplay):
        _translate = QtCore.QCoreApplication.translate
        SV_mainDisplay.setWindowTitle(_translate("SV_mainDisplay", "MainWindow"))
        self.SV_mainDisplay = SV_mainDisplay
        self.label.setText(_translate("SV_mainDisplay", "Tủ Master"))
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
        self.btQuanLy.setText(_translate("SV_mainDisplay", "Quản lý"))
        self.btDongTu.setText(_translate("SV_mainDisplay", "Đóng tủ"))
        self.btMoTu.setText(_translate("SV_mainDisplay", "Mở tủ"))
        self.btThongGio.setText(_translate("SV_mainDisplay", "Thông gió"))
        self.btTraCuu.setText(_translate("SV_mainDisplay", "Tra cứu"))
        self.lbCanhBao.setText(_translate("SV_mainDisplay", "Trạng thái vận hành"))
        self.lbTempIn_7.setText(_translate("SV_mainDisplay", "cm"))
        self.lbKhoangCach.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiIn_3.setText(_translate("SV_mainDisplay", "Khoảng cách :"))
        self.lbstatusMotor.setText(_translate("SV_mainDisplay", "32"))
        self.lbSoNguoi.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiIn_4.setText(_translate("SV_mainDisplay", "Trạng thái tủ :"))
        self.lbHumiIn_5.setText(_translate("SV_mainDisplay", "Số người trong tủ :"))
        self.lbWarning.setText(_translate("SV_mainDisplay", "Cháy trong và ngoài"))
        self.lbCanhBao_2.setText(_translate("SV_mainDisplay", "Cảnh báo sự cố :"))

        self.initDisplay()

    def initDisplay(self):

        self.setEvent()
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.showTemp)
        self.ctimer.start(1000)
        self.isShowWaitForm = False
        self.isShowSuCoForm = False
        self.saveLog = True
        self.isPressThongGio = True

    def showTemp(self):
        try:
            
            _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
            self.label_2.setText(str(_date))
            minitue = int(strftime("%M"))
            sec = int(strftime("%S"))
            if minitue % 10 == 0 :
                if self.saveLog :
                    self.saveLog = False
                    server.saveNhietDoDoAm()
            else :
                self.saveLog = True
            if sec % 10 == 0:
                server.serverMain.sendTempOut()
            #neu dang trong che do bao duong ko lam gi luon return luon
            if server.caseBD > 0:
                return

            self.lbHumiInValue.setText(str(uart.dataReceved.humiIn))
            self.lbTempInValue.setText(str(uart.dataReceved.tempIn))
            self.lbTempOutValue.setText(str(uart.dataReceved.tempOut))
            self.lbHumiOutValue.setText(str(uart.dataReceved.humiOut))
           
            tuActive = server.tuActive
            
            if tuActive[0] == 'L' or tuActive[0] == 'R': #hien thi tu nao dang mo va thong bao nguoi vao ra
                if server.dataReceivedSer[tuActive].statusMotor == 2:
                    self.lbstatusMotor.setText(tuActive + " Mở")
                    self.lbSoNguoi.setText(str(server.dataReceivedSer[tuActive].numPersonIn))
                elif server.dataReceivedSer[tuActive].statusMotor == 4:
                    self.lbstatusMotor.setText("Đóng")
                    self.lbSoNguoi.setText("")

                self.lbKhoangCach.setText(str(server.dataReceivedSer[tuActive].distanceSen_1))
            else: #neu ko co tu nao dang mo thi setText bang Dong or Dung
                self.lbKhoangCach.setText("")
                self.lbSoNguoi.setText("")
                self.lbWarning.setText("")
                self.lbstatusMotor.setText("Đóng")    
                if server.isWaiting == 2: # dung khan cap
                    self.lbstatusMotor.setText("Dừng")

            #thong bao co nguoi vao tu
            tuHumen,isHumenIn,numHumen = server.serverMain.checkHumen()
            if isHumenIn:
                #co nguoi vao tu
                self.linkFile = server.folderMP3 + "009.mp3"
                server.playmp3(self.linkFile)
                self.lbSoNguoi.setText(str(numHumen))
                self.lbstatusMotor.setText(tuHumen)
            
            #check su co xem có sự cố cháy ko nếu có sự cố cháy thì chỉ hiện sự cố cháy thôi rồi return 
            server.serverMain.checkSuCo(False)
            if server.statusSuCo == 0 :# khong co su co thi reset form 
                self.isShowSuCoForm = False
            if server.arraySuCo[1] != '0' or server.arraySuCo[2] != '0': # su co co chay
                if self.isShowSuCoForm == False :
                    if server.arraySuCo[1] != '0':
                        #phat hien chay trong tu --> mo tu bi chay
                        self.linkFile = server.folderMP3 + "010.mp3"
                        server.playmp3(self.linkFile)
                        if server.arraySuCo[1][0] == 'M' : # mo 2 tu gan master nhat Left_1 Right_1
                            server.tuTraiPhai = 'A'
                            server.dongMoTuFunction(4, 'All_1')
                        elif server.arraySuCo[1][0] == 'L' or server.arraySuCo[1][0] == 'R' :
                            server.tuTraiPhai = server.arraySuCo[1][0]
                            server.dongMoTuFunction(3 , server.arraySuCo[1])
                    else:
                        #phat hien chay ngoai tu -> dong tat ca cac tu
                        self.linkFile = server.folderMP3 + "011.mp3"
                        server.playmp3(self.linkFile)
                        server.tuTraiPhai = 'A'
                        server.dongMoTuFunction(0,1)

                    self.isShowSuCoForm = True
                    self.callSuCoForm()

                return 

            #dang van hanh ma co vat can thi hien form su co canh bao vat can
            if server.isWaiting == 3 and ( server.arraySuCo[0] != '0' or server.statusSuCo == 4 ):
                if self.isShowSuCoForm == False :
                    self.isShowSuCoForm = True
                    self.callSuCoForm()
                return
            
            #yeu cau dong mo tu va khong co nguoi trong tu
            if server.isWaiting == 0 or server.isWaiting == 2: 
                self.isShowWaitForm = False
            elif server.isWaiting == 1 :
                if self.isShowWaitForm == False :
                    self.isShowWaitForm = True
                    self.callWaitingForm()
            
            '''phan nay kiem tra thong gio timer thuc thi thong gio'''
            #check thong gio co bat hay khong
            if server.numThongGio >= 1 :
                if server.serverMain.checkAllTuIsClosed() :
                    print("timer call thong gio")
                    server.numThongGio = -2
                    self.btThongGio_click()
                else :
                    server.numThongGio += 1
                    if server.numThongGio == 30: #sau 10s cac tu chua dong huy lenh thong gio nay di
                        server.numThongGio = 0
                        server.executeThongGio = 0
                        server.countThongGio = 60
                        print("TimOut reset thong gio self.numThongGio = 0")
            if server.executeThongGio == 0 : # thong gio dang khong thuc thi
                dateH = int(strftime("%H"))
                dateM = int(strftime("%M"))
                timeThongGio = uart.dataAllJsonConfig["timeThongGio"]
                timeSplit = timeThongGio.split(':')
                if dateH == int(timeSplit[0]) and dateM == int(timeSplit[1]) and timeSplit[3] == '1':# co kich hoat ham autoThongGio
                    print("Mo thong gio tu dong")
                    self.isPressThongGio = False #thuc hien tu dong
                    self.btThongGio_click() # thuc hien chuc nang mo thong gio
                    server.countThongGio = int(timeSplit[2]) * 60 
                    
            elif server.executeThongGio == 1 : #che do thong gio dang mo
                server.countThongGio -= 1 #tang so giay thong gio dang mo len 1
                if server.countThongGio <= 0 and self.isPressThongGio == False: #chi tu dong tat khi tu dong bat, khi bat bang tay ko tu tat thong gio
                    self.btThongGio_click() # neu het thoi gian thong gio tat che do thong gio
            if server.numThongGio == -3 :
                self.btThongGio.setText("Tắt\nThông gió")
            elif server.numThongGio == 0 :
                self.isPressThongGio = True
                self.btThongGio.setText("Thông gió")

            #Kiem tra den thap sent to Arduino to status of server 
            if server.isWaiting == 2 or server.isWaiting == 3 or server.isWaiting == 1: #Dung khan cap bao den vang
                uart.DataCamBien[4] = 0x32
                uart.sentCambien()
            elif server.isWaiting == 0: # hoat dong binh thuong bao den xanh
                uart.DataCamBien[4] = 0x31
                uart.sentCambien()

            '''phan kiem tra PC --> master bat tat dieu hoa'''
            if server.statusVanHanh == 0x34 : #DieuKhienDieuHoa
                self.callDieuHoaForm()
            elif server.statusVanHanh == 40 : # bat che do bao duong
                self.callBaoDuongForm()
        except Exception as e:
            print("error in mainDisplay.ShowTemp() " + str(e))

    def setEvent(self):
        self.btDongTu.clicked.connect(self.btDongTu_click)
        self.btExit.clicked.connect(self.btExit_click)
        self.btMoTu.clicked.connect(self.btMoTu_click)

        self.btKiemTra.clicked.connect(self.btKiemTra_click)
        self.btThongGio.clicked.connect(self.btThongGio_click)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.btTroGiup.clicked.connect(self.btTroGiup_click)
        self.btQuanLy.clicked.connect(self.btQuanLy_click)
        self.NumExit = 0
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
        
    def btDongTu_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()
        #chon dong tu ben nao
        dialogKey = Ui_Dialog(10,True)
        value, isChoosed = dialogKey.exec_()
        print("bt dong tu clicked")
        if isChoosed != 'H' and server.isWaiting != 1:
            server.tuTraiPhai = isChoosed
            server.dongMoTuFunction(0,0)
            
    def btExit_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        self.NumExit +=1
        if self.NumExit == 3 :
            server.userLogin = False
            server.serverMain.sentLogin2AllClient()
            self.ctimer.stop()
            self.SV_mainDisplay.close()
    
    def btMoTu_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()
        maxTu = server.numClientLeft if server.numClientLeft > server.numClientRight else server.numClientRight
        dialogKey = Ui_Dialog(maxTu,True)
        value , isChoosed = dialogKey.exec_()
        if value == '0' or isChoosed == 'H':
            return
        if server.tuTraiPhai == 'L' and int(value) <= server.numClientLeft:
            nameTu = "Left_"+str(value)
        elif server.tuTraiPhai == 'R' and int(value) <= server.numClientRight :
            nameTu = "Right_" + str(value)
        else:
            return
        if server.isWaiting == 2:
            server.dongMoTuFunction(2,nameTu)
        elif server.isWaiting == 0 :
            server.dongMoTuFunction(1,nameTu)
        
    def btKiemTra_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        pass
   
    def btThongGio_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()
        server.serverMain.thongGioFuction()
        
    def btTroGiup_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        pass

    def setWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen :
            self.window.showFullScreen()

    def btTraCuu_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()
        self.ui = Ui_formTimKiem()
        self.setWindow()

    def btQuanLy_click(self):
        #chong doi phim 
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        self.ui = Ui_SVQuanLy()
        self.setWindow()
    
    def callWaitingForm(self):
        self.ui = Ui_FormWaiting()
        self.setWindow()
    
    def callSuCoForm(self):
        #co su co bao den thap
        uart.DataCamBien[4] = 0x33
        uart.sentCambien()
        self.ui = Ui_SV_CanhBao()
        self.setWindow()
    
    def callBaoDuongForm(self):
        from BaoDuongServer import Ui_BaoDuongServer
        self.ui = Ui_BaoDuongServer()
        self.setWindow()
    def callDieuHoaForm(self):
        from svDieuKhienDieuHoa import Ui_svDieuHoa
        self.ui = Ui_svDieuHoa()
        self.setWindow()
import resources
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_mainDisplay = QtWidgets.QMainWindow()
    ui = Ui_SV_mainDisplay()
    ui.setupUi(SV_mainDisplay)
    SV_mainDisplay.show()
    sys.exit(app.exec_())

"""
