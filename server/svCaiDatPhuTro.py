# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CaiDatPhuTro.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from svDieuKhienDieuHoa import Ui_svDieuHoa
from setTime import Ui_setTime
from logTemp import Ui_SV_LogTemp
import server

class Ui_SVCaiDatPhuTro(object):
    def setupUi(self, SVCaiDatPhuTro):
        SVCaiDatPhuTro.setObjectName("SVCaiDatPhuTro")
        SVCaiDatPhuTro.resize(1280, 800)
        self.SVCaiDatPhuTro = SVCaiDatPhuTro
        self.frame = QtWidgets.QFrame(SVCaiDatPhuTro)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#lbtitle{color:red ;font: 75  30pt \"Arial\";}QPushButton:pressed { background-color: #FF6E40}#btBack{color:white;border-image: url(:/images/back.png);}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(410, 110, 491, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btDcThoiGian = QtWidgets.QPushButton(self.frame)
        self.btDcThoiGian.setGeometry(QtCore.QRect(290, 230, 181, 81))
        self.btDcThoiGian.setObjectName("btDcThoiGian")
        self.btCdTinhNang = QtWidgets.QPushButton(self.frame)
        self.btCdTinhNang.setGeometry(QtCore.QRect(560, 230, 181, 81))
        self.btCdTinhNang.setObjectName("btCdTinhNang")
        self.btThamSlave = QtWidgets.QPushButton(self.frame)
        self.btThamSlave.setGeometry(QtCore.QRect(830, 230, 181, 81))
        self.btThamSlave.setObjectName("btThamSlave")
        self.btTietKiemNangLuong = QtWidgets.QPushButton(self.frame)
        self.btTietKiemNangLuong.setGeometry(QtCore.QRect(290, 345, 181, 81))
        self.btTietKiemNangLuong.setObjectName("btTietKiemNangLuong")
        self.btAmBao = QtWidgets.QPushButton(self.frame)
        self.btAmBao.setGeometry(QtCore.QRect(560, 345, 181, 81))
        self.btAmBao.setObjectName("btAmBao")
        self.btHuyThongBao = QtWidgets.QPushButton(self.frame)
        self.btHuyThongBao.setGeometry(QtCore.QRect(830, 345, 181, 81))
        self.btHuyThongBao.setObjectName("btHuyThongBao")
        self.btKhoa = QtWidgets.QPushButton(self.frame)
        self.btKhoa.setGeometry(QtCore.QRect(290, 460, 181, 81))
        self.btKhoa.setObjectName("btKhoa")

        self.btTemp = QtWidgets.QPushButton(self.frame)
        self.btTemp.setGeometry(QtCore.QRect(290, 580, 181, 81))
        self.btTemp.setObjectName("btTemp")

        self.btMoKhoa = QtWidgets.QPushButton(self.frame)
        self.btMoKhoa.setGeometry(QtCore.QRect(560, 460, 181, 81))
        self.btMoKhoa.setObjectName("btMoKhoa")
        self.btCdGoc = QtWidgets.QPushButton(self.frame)
        self.btCdGoc.setGeometry(QtCore.QRect(830, 460, 181, 81))
        self.btCdGoc.setObjectName("btCdGoc")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(830, 580, 181, 81))
        self.btBack.setObjectName("btBack")
        
        self.btDkDieuHoa = QtWidgets.QPushButton(self.frame)
        self.btDkDieuHoa.setGeometry(QtCore.QRect(560, 580, 181, 81))
        self.btDkDieuHoa.setObjectName("btDkDieuHoa")

        self.retranslateUi(SVCaiDatPhuTro)
        QtCore.QMetaObject.connectSlotsByName(SVCaiDatPhuTro)

    def retranslateUi(self, SVCaiDatPhuTro):
        _translate = QtCore.QCoreApplication.translate
        SVCaiDatPhuTro.setWindowTitle(_translate("SVCaiDatPhuTro", "Form"))
        self.lbtitle.setText(_translate("SVCaiDatPhuTro", "Cài đặt phụ trợ"))
        self.btDcThoiGian.setText(_translate("SVCaiDatPhuTro", "Điều chỉnh\nthời gian"))
        self.btCdTinhNang.setText(_translate("SVCaiDatPhuTro", "Cài đặt\ntính năng"))
        self.btThamSlave.setText(_translate("SVCaiDatPhuTro", "Thăm dò\nmáy chủ"))
        self.btTietKiemNangLuong.setText(_translate("SVCaiDatPhuTro", "Tiết kiệm\nnăng lượng"))
        self.btAmBao.setText(_translate("SVCaiDatPhuTro", "Âm báo\nnhắc nhở"))
        self.btHuyThongBao.setText(_translate("SVCaiDatPhuTro", "Hủy\nthông báo"))
        self.btKhoa.setText(_translate("SVCaiDatPhuTro", "Khóa"))
        self.btMoKhoa.setText(_translate("SVCaiDatPhuTro", "Mở khóa"))
        self.btTemp.setText(_translate("SVCaiDatPhuTro", "Log\nNhiệt độ"))
        self.btCdGoc.setText(_translate("SVCaiDatPhuTro", "Khôi phục\ncài đặt gốc"))
        self.btBack.setText(_translate("SVCaiDatPhuTro", "Quay lại"))
        self.btDkDieuHoa.setText(_translate("SVCaiDatPhuTro", "Điều hòa"))

        self.setEvent()

    def setEvent(self):
        self.btDkDieuHoa.clicked.connect(self.btDkDieuHoa_click)
        self.btBack.clicked.connect(self.SVCaiDatPhuTro.close)
        self.btMoKhoa.clicked.connect(self.btMoKhoa_click)
        self.btKhoa.clicked.connect(self.btKhoa_click)
        self.btDcThoiGian.clicked.connect(self.btDcThoiGian_click)
        self.btTemp.clicked.connect(self.btTemp_click)
    def btTemp_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SV_LogTemp()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullScreen :
            self.window.showFullScreen()
        self.SVCaiDatPhuTro.close()

    def btDcThoiGian_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_setTime()
        self.ui.setupUi(self.window)
        self.window.show()
        #self.window.showFullScreen()
        self.SVCaiDatPhuTro.close()

    def btKhoa_click(self):
        for i in range(1,server.numClientLeft+1):
            nameTu = "Left_"+str(i)
            server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc\x00')
        print("btKhoa_click")
        
    def btMoKhoa_click(self):
        for i in range(1,server.numClientLeft+1):
            nameTu = "Left_"+str(i)
            server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc\x01')
        print("btMoKhoa_click")    

    def btDkDieuHoa_click(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_svDieuHoa()
        self.ui.setupUi(self.window)
        self.window.show()
        #self.window.showFullScreen()
        self.SVCaiDatPhuTro.close()

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