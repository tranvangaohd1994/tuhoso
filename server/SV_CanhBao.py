# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CanhBao.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import server
import time
import uart

class Ui_SV_CanhBao(object):
    def setupUi(self, SV_CanhBao):

        SV_CanhBao.setObjectName("SV_CanhBao")
        SV_CanhBao.resize(1280, 800)
        SV_CanhBao.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}")
        self.SV_CanhBao = SV_CanhBao
        self.centralwidget = QtWidgets.QWidget(SV_CanhBao)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(700, 140, 571, 141))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Arial\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 22pt \"Arial\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 22pt \"Arial\";}")
        self.grTempOut.setTitle("")
        self.grTempOut.setObjectName("grTempOut")
        self.lbTempIn_2 = QtWidgets.QLabel(self.grTempOut)
        self.lbTempIn_2.setGeometry(QtCore.QRect(10, 80, 201, 45))
        self.lbTempIn_2.setObjectName("lbTempIn_2")
        self.lbHumiIn_2 = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiIn_2.setGeometry(QtCore.QRect(300, 80, 191, 45))
        self.lbHumiIn_2.setObjectName("lbHumiIn_2")
        self.lbTempOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempOutValue.setGeometry(QtCore.QRect(210, 80, 81, 45))
        self.lbTempOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempOutValue.setObjectName("lbTempOutValue")
        self.lbHumiOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiOutValue.setGeometry(QtCore.QRect(500, 80, 81, 45))
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
        self.grStatusMotor.setGeometry(QtCore.QRect(10, 140, 521, 141))
        self.grStatusMotor.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75  20pt \"Arial\";}\n"
                "#lbTrangThaiLuuTru{color:#FFFF00 ;font: 75  22pt \"Arial\";}\n"
                "#lbChoMuon{color :#D500F9;font:75 22pt \"Arial\";}\n"
                "#lbTrongKho{color :#D500F9;font:75  22pt \"Arial\";}\n"
                "")
        self.grStatusMotor.setTitle("")
        self.grStatusMotor.setObjectName("grStatusMotor")
        self.lbTrangThaiLuuTru = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrangThaiLuuTru.setGeometry(QtCore.QRect(120, 5, 261, 31))
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
        self.btKiemTra.setGeometry(QtCore.QRect(350, 40, 141, 81))
        self.btKiemTra.setObjectName("btKiemTra")
        self.grControl = QtWidgets.QGroupBox(self.frame)
        self.grControl.setGeometry(QtCore.QRect(0, 450, 491, 341))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(30, 190, 161, 101))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btQuanLy = QtWidgets.QPushButton(self.grControl)
        self.btQuanLy.setGeometry(QtCore.QRect(290, 190, 161, 101))
        self.btQuanLy.setObjectName("btQuanLy")
        self.btBaoAnToan = QtWidgets.QPushButton(self.grControl)
        self.btBaoAnToan.setGeometry(QtCore.QRect(30, 10, 161, 101))
        self.btBaoAnToan.setObjectName("btBaoAnToan")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(290, 10, 161, 101))
        self.btTraCuu.setObjectName("btTraCuu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(620, 430, 641, 341))
        self.grWarning.setStyleSheet("#lbCanhBao{color:#FF0000 ;font: 75  22pt \"Arial\";}#FrameCanhBao{background-image: url(:/images/canhbaosuco.jpg);}")
        self.grWarning.setTitle("")
        self.grWarning.setObjectName("grWarning")
        self.lbCanhBao = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao.setGeometry(QtCore.QRect(210, 5, 271, 41))
        self.lbCanhBao.setObjectName("lbCanhBao")
        self.FrameCanhBao = QtWidgets.QFrame(self.grWarning)
        self.FrameCanhBao.setGeometry(QtCore.QRect(90, 70, 471, 241))
        self.FrameCanhBao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCanhBao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCanhBao.setObjectName("FrameCanhBao")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 71, 75))
        self.btExit.setStyleSheet("border: none;background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grWarning_2 = QtWidgets.QGroupBox(self.frame)
        self.grWarning_2.setGeometry(QtCore.QRect(10, 290, 1261, 121))
        self.grWarning_2.setStyleSheet("#lbCanhBao_2{color: rgb(255, 255, 0);font: 75 22pt \"Arial\";}")
        self.grWarning_2.setTitle("")
        self.grWarning_2.setObjectName("grWarning_2")
        self.lbCanhBao_2 = QtWidgets.QLabel(self.grWarning_2)
        self.lbCanhBao_2.setGeometry(QtCore.QRect(10, 20, 1241, 75))
        self.lbCanhBao_2.setObjectName("lbCanhBao_2")
        SV_CanhBao.setCentralWidget(self.centralwidget)

        self.retranslateUi(SV_CanhBao)
        QtCore.QMetaObject.connectSlotsByName(SV_CanhBao)

    def retranslateUi(self, SV_CanhBao):
        _translate = QtCore.QCoreApplication.translate
        SV_CanhBao.setWindowTitle(_translate("SV_CanhBao", "MainWindow"))
        self.lbTempIn_2.setText(_translate("SV_CanhBao", "Nhiệt độ ngoài : "))
        self.lbHumiIn_2.setText(_translate("SV_CanhBao", "Độ ẩm ngoài : "))
        self.lbTempOutValue.setText(_translate("SV_CanhBao", "25.6"))
        self.lbHumiOutValue.setText(_translate("SV_CanhBao", "25.8"))
        self.lbTempInValue.setText(_translate("SV_CanhBao", "28"))
        self.lbTempIn.setText(_translate("SV_CanhBao", "Nhiệt độ trong : "))
        self.lbHumiInValue.setText(_translate("SV_CanhBao", "56.8"))
        self.lbHumiIn.setText(_translate("SV_CanhBao", "Độ ẩm trong :"))
        self.lbTrangThaiLuuTru.setText(_translate("SV_CanhBao", "Trạng thái lưu trữ"))
        self.lbTrongKho.setText(_translate("SV_CanhBao", "5"))
        self.lbTempIn_9.setText(_translate("SV_CanhBao", "Trong kho :"))
        self.lbChoMuon.setText(_translate("SV_CanhBao", "2"))
        self.lbTempIn_10.setText(_translate("SV_CanhBao", "Cho mượn :"))
        self.btKiemTra.setText(_translate("SV_CanhBao", "Kiểm tra"))
        self.btTroGiup.setText(_translate("SV_CanhBao", "Trợ giúp"))
        self.btBaoAnToan.setText(_translate("SV_CanhBao", "Báo\nan toàn"))
        self.btTraCuu.setText(_translate("SV_CanhBao", "Tra cứu"))
        self.lbCanhBao.setText(_translate("SV_CanhBao", "Trạng thái vận hành"))

        self.setEvent()

    def setEvent(self):
        print("Mo form Su co ")
        #server.statusSuCo = 1
        if server.statusSuCo == 1:
            self.lbCanhBao_2.setText("Cột "+server.arraySuCo[0]+ " có người,để đảm bảo an toàn hệ thống sẽ tự động dừng!")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbCoNguoi.jpg);}")
        elif server.statusSuCo == 2 or  server.statusSuCo == 3 :
            self.lbCanhBao_2.setText("Cột "+server.arraySuCo[1]+" có cháy, hệ thống tự động đóng lại \nđể đảm bảo an toàn cho hệ thống!")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbChay.jpg);}")
        else :
            self.lbCanhBao_2.setText("Cảnh báo sự cố trong giá, hệ thống sẽ tự động dừng lại!\n Vui lòng kiểm tra lại sự cố để hệ thống hoạt động trở lại!")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbSuCo.jpg);}")

        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkDone)
        self.ctimer.start(300)
        
        self.btBaoAnToan.clicked.connect(self.btBaoAnToan_click)

    def checkDone(self):
        self.lbHumiInValue.setText(str(uart.dataReceved.humiIn))
        self.lbTempInValue.setText(str(uart.dataReceved.tempIn))
         
        self.lbTempOutValue.setText(str(uart.dataReceved.tempOut))
        self.lbHumiOutValue.setText(str(uart.dataReceved.humiOut))


        if server.statusSuCo == 0:
            print("Dong form Su co trong ham checkDone")
            self.ctimer.stop()
            server.serverMain.DoneSuCo(False)
            self.SV_CanhBao.close()
            #self.btBaoAnToan_click()

    def btBaoAnToan_click(self):
        self.ctimer.stop()
        server.serverMain.DoneSuCo(True)
        self.SV_CanhBao.close()
        pass

import resources

"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_CanhBao = QtWidgets.QMainWindow()
    ui = Ui_SV_CanhBao()
    ui.setupUi(SV_CanhBao)
    SV_CanhBao.show()
    sys.exit(app.exec_())

"""