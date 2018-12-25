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
        self.SV_CanhBao = SV_CanhBao
        
        self.centralwidget = QtWidgets.QWidget(SV_CanhBao)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QLabel{color:#F44336 ;font:  bold 18pt \"Arial\";qproperty-alignment: AlignCenter;}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #4e9400;font: bold 25pt \"Arial\";color:#ffffff}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btKiemTra = QtWidgets.QPushButton(self.frame)
        self.btKiemTra.setGeometry(QtCore.QRect(380, 320, 171, 81))
        self.btKiemTra.setObjectName("btKiemTra")
        self.lbTrongKho = QtWidgets.QLabel(self.frame)
        self.lbTrongKho.setGeometry(QtCore.QRect(270, 310, 101, 45))
        self.lbTrongKho.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTrongKho.setObjectName("lbTrongKho")
        self.lbChoMuon = QtWidgets.QLabel(self.frame)
        self.lbChoMuon.setGeometry(QtCore.QRect(270, 350, 101, 45))
        self.lbChoMuon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbChoMuon.setObjectName("lbChoMuon")
        self.btTraCuu = QtWidgets.QPushButton(self.frame)
        self.btTraCuu.setGeometry(QtCore.QRect(340, 540, 171, 81))
        self.btTraCuu.setObjectName("btTraCuu")
        self.btQuanLy = QtWidgets.QPushButton(self.frame)
        self.btQuanLy.setGeometry(QtCore.QRect(340, 640, 171, 81))
        self.btQuanLy.setObjectName("btQuanLy")
        self.btTroGiup = QtWidgets.QPushButton(self.frame)
        self.btTroGiup.setGeometry(QtCore.QRect(140, 640, 171, 81))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btBaoAnToan = QtWidgets.QPushButton(self.frame)
        self.btBaoAnToan.setGeometry(QtCore.QRect(140, 540, 171, 81))
        self.btBaoAnToan.setObjectName("btBaoAnToan")
        self.lbTempInValue = QtWidgets.QLabel(self.frame)
        self.lbTempInValue.setGeometry(QtCore.QRect(340, 429, 81, 31))
        self.lbTempInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempInValue.setObjectName("lbTempInValue")
        self.lbTempOutValue = QtWidgets.QLabel(self.frame)
        self.lbTempOutValue.setGeometry(QtCore.QRect(480, 429, 81, 31))
        self.lbTempOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempOutValue.setObjectName("lbTempOutValue")
        self.lbHumiOutValue = QtWidgets.QLabel(self.frame)
        self.lbHumiOutValue.setGeometry(QtCore.QRect(480, 470, 81, 31))
        self.lbHumiOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiOutValue.setObjectName("lbHumiOutValue")
        self.lbHumiInValue = QtWidgets.QLabel(self.frame)
        self.lbHumiInValue.setGeometry(QtCore.QRect(345, 470, 71, 31))
        self.lbHumiInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiInValue.setObjectName("lbHumiInValue")
        SV_CanhBao.setCentralWidget(self.centralwidget)

        self.retranslateUi(SV_CanhBao)
        QtCore.QMetaObject.connectSlotsByName(SV_CanhBao)

    def retranslateUi(self, SV_CanhBao):
        _translate = QtCore.QCoreApplication.translate
        SV_CanhBao.setWindowTitle(_translate("SV_CanhBao", "MainWindow"))
        self.btKiemTra.setText(_translate("SV_CanhBao", "Kiểm tra"))
        self.lbTrongKho.setText(_translate("SV_CanhBao", "5"))
        self.lbChoMuon.setText(_translate("SV_CanhBao", "2"))
        self.btTraCuu.setText(_translate("SV_CanhBao", "Tra cứu"))
        self.btQuanLy.setText(_translate("SV_CanhBao", "Trợ giúp"))
        self.btTroGiup.setText(_translate("SV_CanhBao", "Cài đặt\n"
                "phụ trợ"))
        self.btBaoAnToan.setText(_translate("SV_CanhBao", "Báo\n"
                "an toàn"))
        self.lbTempInValue.setText(_translate("SV_CanhBao", "28"))
        self.lbTempOutValue.setText(_translate("SV_CanhBao", "25.6"))
        self.lbHumiOutValue.setText(_translate("SV_CanhBao", "25.8"))
        self.lbHumiInValue.setText(_translate("SV_CanhBao", "56.8"))

        self.setEvent()

    def setEvent(self):
        print("Mo form Su co ")
        #server.statusSuCo = 1
        if server.statusSuCo == 1:
            self.SV_CanhBao.setStyleSheet(".QFrame{background-image:url(:/images/scCoNguoi.png);}")
        elif server.statusSuCo == 2 or  server.statusSuCo == 3 :
            self.SV_CanhBao.setStyleSheet(".QFrame{background-image:url(:/images/scCoChay.png);}")
        else :
            self.SV_CanhBao.setStyleSheet(".QFrame{background-image:url(:/images/scVatCan.png);}")

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