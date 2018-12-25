# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate

from SV_QuanLy import Ui_SVQuanLy
from formWaiting import Ui_FormWaiting
from SV_CanhBao import Ui_SV_CanhBao
from kbNumber import Ui_Dialog 
from time import strftime
from formTimKiem import Ui_formTimKiem
from logTemp import Ui_SV_LogTemp
from formKhoaDC import Ui_FormKhoaDC

import time
import struct
import server
import uart

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
        self.btQuanLy = QtWidgets.QPushButton(self.grControl)
        self.btQuanLy.setGeometry(QtCore.QRect(254, 248, 161, 80))
        self.btQuanLy.setObjectName("btQuanLy")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(254, 50, 161, 80))
        self.btDongTu.setObjectName("btDongTu")
        self.btThongGio = QtWidgets.QPushButton(self.grControl)
        self.btThongGio.setGeometry(QtCore.QRect(54, 150, 161, 80))
        self.btThongGio.setObjectName("btThongGio")
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
        SV_mainDisplay.setCentralWidget(self.centralwidget)

        self.retranslateUi(SV_mainDisplay)
        QtCore.QMetaObject.connectSlotsByName(SV_mainDisplay)    
    
    def retranslateUi(self, SV_mainDisplay):
        _translate = QtCore.QCoreApplication.translate
        SV_mainDisplay.setWindowTitle(_translate("SV_mainDisplay", "MainWindow"))
        self.lbTempOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTrongKho.setText(_translate("SV_mainDisplay", "0"))
        self.lbChoMuon.setText(_translate("SV_mainDisplay", "0"))
        self.btKiemTra.setText(_translate("SV_mainDisplay", "Kiểm tra"))
        self.btTroGiup.setText(_translate("SV_mainDisplay", "Trợ giúp"))
        self.btQuanLy.setText(_translate("SV_mainDisplay", "Cài đặt"))
        self.btDongTu.setText(_translate("SV_mainDisplay", "Đóng giá"))
        self.btThongGio.setText(_translate("SV_mainDisplay", "Thông gió"))
        self.btTraCuu.setText(_translate("SV_mainDisplay", "Tra cứu"))
        self.btMoTu.setText(_translate("SV_mainDisplay", "Mở giá"))
        self.lbKhoangCach.setText(_translate("SV_mainDisplay", "20"))
        self.lbstatusMotor.setText(_translate("SV_mainDisplay", "Đóng"))
        self.lbSoNguoi.setText(_translate("SV_mainDisplay", "0"))
        self.lbWarning.setText(_translate("SV_mainDisplay", "a"))
        self.btXemChiTiet.setText(_translate("SV_mainDisplay", "Xem chi tiết"))

        self.SV_mainDisplay = SV_mainDisplay
        self.initDisplay()

    def initDisplay(self):
        self.setEvent()
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.showTemp)
        self.ctimer.start(1000)
        self.isShowWaitForm = False
        self.isShowSuCoForm = False
        self.isShowFormKhoaDC = False
        self.saveLog = True
        self.isPressThongGio = True

    def showTemp(self):
        #try:
            _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
            minitue = int(strftime("%M"))
            sec = int(strftime("%S"))
            if minitue % 10 == 0 :
                if self.saveLog :
                    self.saveLog = False
                    server.saveNhietDoDoAm()
            else :
                self.saveLog = True
            if sec % 1 == 0:
                server.serverMain.sendTempOut()
            #neu dang trong che do bao duong ko lam gi luon return luon
             #Kiem tra den thap sent to Arduino to status of server 
            if server.isWaiting == 2 or server.isWaiting == 3 or server.isWaiting == 1: #Dung khan cap bao den vang
                uart.DataCamBien[4] = 0x32
                uart.sentCambien()
            elif server.isWaiting == 0: # hoat dong binh thuong bao den xanh
                uart.DataCamBien[4] = 0x31
                uart.sentCambien()

            if server.caseBD > 0:
                return
                
            self.lbHumiInValue.setText(str(uart.dataReceved.humiIn))
            self.lbTempInValue.setText(str(uart.dataReceved.tempIn))
            self.lbTempOutValue.setText(str(uart.dataReceved.tempOut))
            self.lbHumiOutValue.setText(str(uart.dataReceved.humiOut))
           
            tuActive = server.tuActive
            
            if tuActive[0] == 'L' or tuActive[0] == 'R': #hien thi tu nao dang mo va thong bao nguoi vao ra
                if server.dataReceivedSer[tuActive].statusMotor == 2:
                    self.lbstatusMotor.setText('Giá '+ str(server.converNameTu(tuActive)) + " Mở")
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
            if server.isWaiting == 3 and ( server.statusSuCo == 1 or server.statusSuCo == 4 ):
                if self.isShowSuCoForm == False :
                    self.isShowSuCoForm = True
                    self.callSuCoForm()
                return

            if server.isWaiting !=3 or server.statusSuCo !=5 :
                self.isShowFormKhoaDC = False
            if server.isWaiting == 3 and server.statusSuCo == 5 :
                if self.isShowFormKhoaDC == False :
                    self.isShowFormKhoaDC = True
                    self.callFormKhoaDC()
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
                server.numThongGio = -2
                self.btThongGio_click()

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

            '''phan kiem tra PC --> master bat tat dieu hoa'''
            if server.statusVanHanh == 0x34 : #DieuKhienDieuHoa
                self.callDieuHoaForm()
            elif server.statusVanHanh == 40 : # bat che do bao duong
                self.callBaoDuongForm()
                
        #except Exception as e:
         #   print("error in mainDisplay.ShowTemp() " + str(e.__doc__))

    def setEvent(self):
        self.btDongTu.clicked.connect(self.btDongTu_click)
        self.btExit.clicked.connect(self.btExit_click)
        self.btMoTu.clicked.connect(self.btMoTu_click)

        self.btKiemTra.clicked.connect(self.btKiemTra_click)
        self.btThongGio.clicked.connect(self.btThongGio_click)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.btTroGiup.clicked.connect(self.btTroGiup_click)
        self.btQuanLy.clicked.connect(self.btQuanLy_click)
        self.btXemChiTiet.clicked.connect(self.btXemChiTiet_click)
        self.NumExit = 0
        self.btClickTimer = False

        #get mouse event
        self.xS = self.xE = 0
        self.yS = self.yE = 0
        self.lengthMouse = 80
    
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
        #chon dong tat ca cac tu o ca 2 ben
        server.tuTraiPhai = 'A'
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
        maxTu = server.numClientLeft + server.numClientRight + 1
        dialogKey = Ui_Dialog(maxTu)
        value = dialogKey.exec_()
        if value:
            nameTu = server.serverMain.getNameOfTu(int(value))
            if nameTu[0] == 'H':
                return
            server.tuTraiPhai = nameTu[0]
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
    def btXemChiTiet_click(self):
        self.ui = Ui_SV_LogTemp()
        self.setWindow()
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
    def callFormKhoaDC(self):
        self.ui = Ui_FormKhoaDC()
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

    #event mouse
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
            print("swipe right do nothing")
        elif difX < - self.lengthMouse:
            print("swipe left")
        elif difY > self.lengthMouse :
            print("swipe down - dong toan bo gia")
            server.tuTraiPhai = 'A'
            server.dongMoTuFunction(0,0)
            
        elif difY < - self.lengthMouse :
            print('swipr Up - thuc hien thong gio')
            server.serverMain.thongGioFuction()
            
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
