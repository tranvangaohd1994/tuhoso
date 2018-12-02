# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CanhBao.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import client

class Ui_SV_CanhBao(object):
    def setupUi(self, SV_CanhBao):

        SV_CanhBao.setObjectName("SV_CanhBao")
        SV_CanhBao.resize(1024, 600)
        SV_CanhBao.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}")
        self.SV_CanhBao = SV_CanhBao
        self.centralwidget = QtWidgets.QWidget(SV_CanhBao)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 600))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(450, 90, 571, 120))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Arial\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 Bold 22pt \"Arial\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Arial\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Arial\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Arial\";}")
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
        self.grStatusMotor.setGeometry(QtCore.QRect(10, 90, 431, 120))
        self.grStatusMotor.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75  20pt \"Arial\";}#lbTrangThaiLuuTru{color:#FFFF00 ;font: 75  22pt \"Arial\";}#lbChoMuon{color :#D500F9;font:75 bold 22pt \"Arial\";}#lbTrongKho{color :#D500F9;font:75  bold 22pt \"Arial\";}")
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
        self.grControl.setGeometry(QtCore.QRect(0, 330, 441, 261))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btCaiDat = QtWidgets.QPushButton(self.grControl)
        self.btCaiDat.setGeometry(QtCore.QRect(30, 160, 160, 90))
        self.btCaiDat.setObjectName("btCaiDat")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(260, 160, 160, 90))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btBaoAnToan = QtWidgets.QPushButton(self.grControl)
        self.btBaoAnToan.setGeometry(QtCore.QRect(30, 20, 160, 90))
        self.btBaoAnToan.setObjectName("btBaoAnToan")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(260, 20, 160, 90))
        self.btTraCuu.setObjectName("btTraCuu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(450, 310, 571, 290))
        self.grWarning.setStyleSheet("#lbCanhBao{color:#FF0000 ;font: 75  22pt \"Arial\";}")
        self.grWarning.setObjectName("grWarning")
        self.lbCanhBao = QtWidgets.QLabel(self.grWarning)
        self.lbCanhBao.setGeometry(QtCore.QRect(160, 5, 271, 41))
        self.lbCanhBao.setObjectName("lbCanhBao")
        self.FrameCanhBao = QtWidgets.QFrame(self.grWarning)
        self.FrameCanhBao.setGeometry(QtCore.QRect(50, 50, 471, 230))
        self.FrameCanhBao.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.FrameCanhBao.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FrameCanhBao.setObjectName("FrameCanhBao")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 71, 75))
        self.btExit.setStyleSheet("border: none;background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grWarning_2 = QtWidgets.QGroupBox(self.frame)
        self.grWarning_2.setGeometry(QtCore.QRect(10, 215, 1011, 91))
        self.grWarning_2.setStyleSheet("#lbCanhBao_2{color: rgb(255, 255, 0);font: 75 Bold 22pt \"Arial\";}")
        self.grWarning_2.setTitle("")
        self.grWarning_2.setObjectName("grWarning_2")
        self.lbCanhBao_2 = QtWidgets.QLabel(self.grWarning_2)
        self.lbCanhBao_2.setGeometry(QtCore.QRect(10, 10, 971, 75))
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
        self.btCaiDat.setText(_translate("SV_CanhBao", "Cài đặt\nphụ trợ"))
        self.btTroGiup.setText(_translate("SV_CanhBao", "Trợ giúp"))
        self.btBaoAnToan.setText(_translate("SV_CanhBao", "Báo\nan toàn"))
        self.btTraCuu.setText(_translate("SV_CanhBao", "Tra cứu"))
        self.lbCanhBao.setText(_translate("SV_CanhBao", "Trạng thái vận hành"))

        self.setEvent()

    def setEvent(self):
        #client.statusSuCo = 1
        if client.statusSuCo == 1:
            self.lbCanhBao_2.setText("Trong giá có người, hệ thống tự động khóa giá kệ, thao tác điện.\nSau khi giá không có người các thao tác sẽ được kích hoạt lại!")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbCoNguoi.jpg);}")
        elif client.statusSuCo == 2 or client.statusSuCo == 3:
            self.lbCanhBao_2.setText("Phát hiện cháy trong giá, hệ thống tự động khóa các chức năng \nvà đóng lại để đảm bảo an toàn cho hệ thống !")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbChay.jpg);}")
        else :
            self.lbCanhBao_2.setText("Cảnh báo sự cố, Hệ thống sẽ tự động dừng lại!\nVui lòng kiểm tra lại sự cố để hệ thống hoạt động trở lại!")
            self.FrameCanhBao.setStyleSheet("#FrameCanhBao{background-image: url(:/images/cbSuCo.jpg);}")

        
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkDone)
        self.ctimer.start(300)
        
        self.btBaoAnToan.clicked.connect(self.btBaoAnToan_click)

    def checkDone(self):
        self.lbHumiInValue.setText(str(client.dataReceved.humiIn))
        self.lbTempInValue.setText(str(client.dataReceved.tempIn))
         
        self.lbTempOutValue.setText(str(client.dataReceved.tempOut))
        self.lbHumiOutValue.setText(str(client.dataReceved.humiOut))

        if client.statusSuCo == 0:
            self.ctimer.stop()
            self.SV_CanhBao.close()

    def btBaoAnToan_click(self):
        client.ThClientMain.sent2Server(b'\xcb\xcb')
    
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