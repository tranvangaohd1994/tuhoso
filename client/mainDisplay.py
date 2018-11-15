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
from time import strftime
import uart
import client
import resources


class Ui_SV_mainDisplay(object):
    def setupUi(self, SV_mainDisplay):
       
        SV_mainDisplay.setObjectName("SV_mainDisplay")
        SV_mainDisplay.resize(1024, 600)
        SV_mainDisplay.setWindowTitle("mainClient")
        SV_mainDisplay.setStyleSheet(".QFrame{\n"
            "    background-image: url(:/images/Background.jpg);\n"
            "}")
        self.centralwidget = QtWidgets.QWidget(SV_mainDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTopMain = QtWidgets.QGroupBox(self.frame)
        self.grTopMain.setGeometry(QtCore.QRect(0, 540, 1024, 60))
        self.grTopMain.setStyleSheet("#grTopMain{ border: 0px solid gray; border-radius: 0px; }.QLabel {font: 57 bold 22pt \"Ubuntu\";color: rgb(255, 255, 255);}")
        self.grTopMain.setTitle("")
        self.grTopMain.setObjectName("grTopMain")
        self.label = QtWidgets.QLabel(self.grTopMain)
        self.label.setGeometry(QtCore.QRect(0, 0, 341, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.grTopMain)
        self.label_2.setGeometry(QtCore.QRect(500, 0, 524, 60))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(450, 90, 571, 131))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Ubuntu\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}")
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
        self.grStatusMotor.setGeometry(QtCore.QRect(10, 90, 431, 130))
        self.grStatusMotor.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75  20pt \"Ubuntu\";}\n"
            "#lbTrangThaiLuuTru{color:#FFFF00 ;font: 75  22pt \"Ubuntu\";}\n"
            "#lbChoMuon{color :#D500F9;font:75 bold 22pt \"Ubuntu\";}\n"
            "#lbTrongKho{color :#D500F9;font:75  bold 22pt \"Ubuntu\";}\n"
            "")
        self.grStatusMotor.setTitle("")
        self.grStatusMotor.setObjectName("grStatusMotor")
        self.lbTrangThaiLuuTru = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrangThaiLuuTru.setGeometry(QtCore.QRect(80, 5, 261, 31))
        self.lbTrangThaiLuuTru.setObjectName("lbTrangThaiLuuTru")
        self.lbTrongKho = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrongKho.setGeometry(QtCore.QRect(160, 40, 101, 45))
        self.lbTrongKho.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTrongKho.setObjectName("lbTrongKho")
        self.lbTempIn_9 = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTempIn_9.setGeometry(QtCore.QRect(10, 40, 141, 45))
        self.lbTempIn_9.setObjectName("lbTempIn_9")
        self.lbChoMuon = QtWidgets.QLabel(self.grStatusMotor)
        self.lbChoMuon.setGeometry(QtCore.QRect(160, 80, 101, 45))
        self.lbChoMuon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbChoMuon.setObjectName("lbChoMuon")
        self.lbTempIn_10 = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTempIn_10.setGeometry(QtCore.QRect(10, 80, 141, 45))
        self.lbTempIn_10.setObjectName("lbTempIn_10")
        self.btKiemTra = QtWidgets.QPushButton(self.grStatusMotor)
        self.btKiemTra.setGeometry(QtCore.QRect(280, 40, 121, 71))
        self.btKiemTra.setObjectName("btKiemTra")
        self.grControl = QtWidgets.QGroupBox(self.frame)
        self.grControl.setGeometry(QtCore.QRect(0, 230, 441, 301))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(10, 220, 151, 81))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btCaiDat = QtWidgets.QPushButton(self.grControl)
        self.btCaiDat.setGeometry(QtCore.QRect(260, 220, 151, 81))
        self.btCaiDat.setObjectName("btCaiDat")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(260, 10, 151, 81))
        self.btDongTu.setObjectName("btDongTu")
        self.btMoTu = QtWidgets.QPushButton(self.grControl)
        self.btMoTu.setGeometry(QtCore.QRect(10, 10, 151, 81))
        self.btMoTu.setObjectName("btMoTu")
        self.btKhoaDC = QtWidgets.QPushButton(self.grControl)
        self.btKhoaDC.setGeometry(QtCore.QRect(10, 115, 151, 81))
        self.btKhoaDC.setObjectName("btKhoaDC")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(260, 115, 151, 81))
        self.btTraCuu.setObjectName("btTraCuu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(450, 230, 571, 301))
        self.grWarning.setStyleSheet("#lbWarning{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbCanhBao{color:#FFFF00 ;font: 75  22pt \"Ubuntu\";}.QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Ubuntu\";}#lbKhoangCach{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbstatusMotor{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbSoNguoi{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}")
        self.grWarning.setTitle("")
        self.grWarning.setObjectName("grWarning")
        self.lbCanhBao = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao.setGeometry(QtCore.QRect(160, 5, 271, 41))
        self.lbCanhBao.setObjectName("lbCanhBao")
        self.lbTempIn_7 = QtWidgets.QLabel(self.grWarning)
        self.lbTempIn_7.setGeometry(QtCore.QRect(390, 135, 81, 45))
        self.lbTempIn_7.setObjectName("lbTempIn_7")
        self.lbKhoangCach = QtWidgets.QLabel(self.grWarning)
        self.lbKhoangCach.setGeometry(QtCore.QRect(270, 135, 111, 45))
        self.lbKhoangCach.setAlignment(QtCore.Qt.AlignCenter)
        self.lbKhoangCach.setObjectName("lbKhoangCach")
        self.lbHumiIn_3 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_3.setGeometry(QtCore.QRect(10, 135, 191, 41))
        self.lbHumiIn_3.setObjectName("lbHumiIn_3")
        self.lbstatusMotor = QtWidgets.QLabel(self.grWarning)
        self.lbstatusMotor.setGeometry(QtCore.QRect(220, 50, 201, 45))
        self.lbstatusMotor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbstatusMotor.setObjectName("lbstatusMotor")
        self.lbSoNguoi = QtWidgets.QLabel(self.grWarning)
        self.lbSoNguoi.setGeometry(QtCore.QRect(250, 95, 141, 45))
        self.lbSoNguoi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSoNguoi.setObjectName("lbSoNguoi")
        self.lbHumiIn_4 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_4.setGeometry(QtCore.QRect(10, 50, 181, 41))
        self.lbHumiIn_4.setObjectName("lbHumiIn_4")
        self.lbHumiIn_5 = QtWidgets.QLabel(self.grWarning)
        self.lbHumiIn_5.setGeometry(QtCore.QRect(10, 95, 231, 41))
        self.lbHumiIn_5.setObjectName("lbHumiIn_5")
        self.lbWarning = QtWidgets.QLabel(self.grWarning)
        self.lbWarning.setGeometry(QtCore.QRect(10, 224, 561, 61))
        self.lbWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWarning.setObjectName("lbWarning")
        self.lbCanhBao_2 = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao_2.setGeometry(QtCore.QRect(10, 175, 211, 41))
        self.lbCanhBao_2.setObjectName("lbCanhBao_2")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 71, 75))
        self.btExit.setStyleSheet("border: none;\n"
            "background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grTopMain.raise_()
        self.grTempOut.raise_()
        self.grStatusMotor.raise_()
        self.grControl.raise_()
        self.grWarning.raise_()
        self.label.raise_()
        self.btExit.raise_()
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

        ctimer = QTimer(self.frame)
        ctimer.timeout.connect(self.showTemp)
        ctimer.start(1000)
        self.setEvent()
        self.isShowDialog = False

    def showTemp(self):
        try:
            _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
            self.label_2.setText(str(_date))

            self.lbHumiInValue.setText(str(uart.dataReceved.humiIn))
            self.lbTempInValue.setText(str(uart.dataReceved.tempIn))
         
            self.lbTempOutValue.setText(str(uart.dataReceved.tempOut))
            self.lbHumiOutValue.setText(str(uart.dataReceved.humiOut))
            self.lbKhoangCach.setText(str(uart.dataReceved.distanceSen_1))
            self.lbWarning.setText(str(uart.listCanhBao[uart.dataCanhBao]))
            self.lbSoNguoi.setText(str(uart.dataReceved.numPersonIn))

            #Status motor
            if uart.dataReceved.statusMotor == 2:
                self.lbstatusMotor.setText("Mở")
            elif uart.dataReceved.statusMotor == 4:
                self.lbstatusMotor.setText("Đóng")
            elif uart.dataReceved.statusMotor == 5:
                self.lbstatusMotor.setText("Dừng")
            else :
                self.lbstatusMotor.setText("")  
            
            if client.isWaiting == 1 :
                if self.isShowDialog == False :
                    self.isShowDialog = True
                    self.callWaitingForm()
            else :
                self.isShowDialog = False

            if client.isActive2Ser == False:
                self.SV_mainDisplay.close()
                     
        except:
            print("error in mainDisplay.ShowTemp()")
            pass

    def setEvent(self):
        self.btDongTu.clicked.connect(self.btDongTu_click)
        self.btExit.clicked.connect(self.btExit_click)
        self.btMoTu.clicked.connect(self.btMoTu_click)

        self.btKiemTra.clicked.connect(self.btKiemTra_click)
        self.btKhoaDC.clicked.connect(self.btKhoaDC_click)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.btTroGiup.clicked.connect(self.btTroGiup_click)
        self.btCaiDat.clicked.connect(self.btCaiDat_click)
        self.NumExit=0

    def btDongTu_click(self):
        client.ThClientMain.sent2Server(b'\xee\xff')
        
    def btMoTu_click(self):
        client.ThClientMain.sent2Server(b'\xee\xee')
    def btExit_click(self):
        self.NumExit +=1
        if self.NumExit == 3 :
            self.SV_mainDisplay.close()

        pass
    
    def btKiemTra_click(self):
        pass
    def btKhoaDC_click(self):
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
        
