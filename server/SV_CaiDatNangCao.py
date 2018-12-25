# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CaiDatNangCao.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from setChieuQuayDC import Ui_setChieuQuayDC
from setKCGiamToc import Ui_setKCGiamToc
from setKCMotu import Ui_setKCMoTu
from setTocDoDC import Ui_setTocDoDc
from BaoDuongServer import Ui_BaoDuongServer
from setPassword import Ui_setPassword
from setLucChongKet import Ui_setLucChongKet
import server
from PyQt5 import QtCore, QtGui, QtWidgets
from setThongGio import Ui_setThongGio
from setDieuKienVanHanh import Ui_setDieuKienVanHanh
from setThemTu import Ui_setThemTu

class Ui_SVCaiDatNangCao(object):
    def setupUi(self, SVCaiDatNangCao):
        SVCaiDatNangCao.setObjectName("SVCaiDatNangCao")
        SVCaiDatNangCao.resize(1280, 800)
        self.SVCaiDatNangCao = SVCaiDatNangCao
        
        self.frame = QtWidgets.QFrame(SVCaiDatNangCao)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/cdnc.png);}#btBack{color:white;border-image: url(:/images/back.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 15px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btLucKet = QtWidgets.QPushButton(self.frame)
        self.btLucKet.setGeometry(QtCore.QRect(140, 340, 215, 100))
        self.btLucKet.setObjectName("btLucKet")
        self.btChieuDC = QtWidgets.QPushButton(self.frame)
        self.btChieuDC.setGeometry(QtCore.QRect(402, 340, 215, 100))
        self.btChieuDC.setObjectName("btChieuDC")
        self.btTocDoDC = QtWidgets.QPushButton(self.frame)
        self.btTocDoDC.setGeometry(QtCore.QRect(665, 340, 215, 100))
        self.btTocDoDC.setObjectName("btTocDoDC")
        self.btKCMotu = QtWidgets.QPushButton(self.frame)
        self.btKCMotu.setGeometry(QtCore.QRect(140, 470, 215, 100))
        self.btKCMotu.setObjectName("btKCMotu")
        self.btKCGiamToc = QtWidgets.QPushButton(self.frame)
        self.btKCGiamToc.setGeometry(QtCore.QRect(402, 470, 215, 100))
        self.btKCGiamToc.setObjectName("btKCGiamToc")
        self.btTatCamBien = QtWidgets.QPushButton(self.frame)
        self.btTatCamBien.setGeometry(QtCore.QRect(665, 470, 215, 100))
        self.btTatCamBien.setObjectName("btTatCamBien")
        self.btCheDoBaoDuong = QtWidgets.QPushButton(self.frame)
        self.btCheDoBaoDuong.setGeometry(QtCore.QRect(925, 340, 215, 100))
        self.btCheDoBaoDuong.setObjectName("btCheDoBaoDuong")
        self.btDoiMatKhau = QtWidgets.QPushButton(self.frame)
        self.btDoiMatKhau.setGeometry(QtCore.QRect(925, 470, 215, 100))
        self.btDoiMatKhau.setObjectName("btDoiMatKhau")
        self.btCdGoc = QtWidgets.QPushButton(self.frame)
        self.btCdGoc.setGeometry(QtCore.QRect(925, 595, 215, 100))
        self.btCdGoc.setObjectName("btCdGoc")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(950, 230, 181, 91))
        self.btBack.setObjectName("btBack")
        self.btQuanLyTu = QtWidgets.QPushButton(self.frame)
        self.btQuanLyTu.setGeometry(QtCore.QRect(665, 595, 215, 100))
        self.btQuanLyTu.setObjectName("btQuanLyTu")
        self.btMoiTruongVH = QtWidgets.QPushButton(self.frame)
        self.btMoiTruongVH.setGeometry(QtCore.QRect(140, 595, 215, 101))
        self.btMoiTruongVH.setObjectName("btMoiTruongVH")
        self.btThongGio = QtWidgets.QPushButton(self.frame)
        self.btThongGio.setGeometry(QtCore.QRect(402, 595, 215, 100))
        self.btThongGio.setObjectName("btThongGio")

        self.retranslateUi(SVCaiDatNangCao)
        QtCore.QMetaObject.connectSlotsByName(SVCaiDatNangCao)

    def retranslateUi(self, SVCaiDatNangCao):
        _translate = QtCore.QCoreApplication.translate
        SVCaiDatNangCao.setWindowTitle(_translate("SVCaiDatNangCao", "Form"))
        self.btLucKet.setText(_translate("SVCaiDatNangCao", "Cấp độ Lực\nchống kẹt"))
        self.btChieuDC.setText(_translate("SVCaiDatNangCao", "Chiều quay\n Động cơ"))
        self.btTocDoDC.setText(_translate("SVCaiDatNangCao", "Tốc độ\n Động cơ"))
        self.btKCMotu.setText(_translate("SVCaiDatNangCao", "Khoảng cách\n Mở tủ"))
        self.btKCGiamToc.setText(_translate("SVCaiDatNangCao", "Khoảng cách\n giảm tốc"))
        self.btTatCamBien.setText(_translate("SVCaiDatNangCao", "Tắt\n Cảm biến"))
        self.btCheDoBaoDuong.setText(_translate("SVCaiDatNangCao", "Chế độ\n Bảo dưỡng"))
        self.btDoiMatKhau.setText(_translate("SVCaiDatNangCao", "Đổi\n Mật khẩu"))
        self.btCdGoc.setText(_translate("SVCaiDatNangCao", "Khôi Phục\n Cài đặt gốc"))
        self.btBack.setText(_translate("SVCaiDatNangCao", "Quay lại"))
        self.btQuanLyTu.setText(_translate("SVCaiDatNangCao", "Quản lý tủ"))
        self.btMoiTruongVH.setText(_translate("SVCaiDatNangCao", "Môi Trường\n vận hành"))
        self.btThongGio.setText(_translate("SVCaiDatNangCao", "Thông gió"))

        self.setEvent()
    def setEvent(self):
        self.btKCGiamToc.clicked.connect(self.btKCGiamToc_click)
        self.btKCMotu.clicked.connect(self.btKCMotu_click)
        self.btTocDoDC.clicked.connect(self.btTocDoDC_click)
        self.btChieuDC.clicked.connect(self.btChieuDC_click)
        self.btBack.clicked.connect(self.SVCaiDatNangCao.close)
        self.btCheDoBaoDuong.clicked.connect(self.btBaoDuong_click)
        self.btDoiMatKhau.clicked.connect(self.btDoiMatKhau_click)
        self.btLucKet.clicked.connect(self.btLucKet_click)
        self.btThongGio.clicked.connect(self.btThongGio_click)
        self.btMoiTruongVH.clicked.connect(self.btMoiTruongVH_click)
        self.btQuanLyTu.clicked.connect(self.btQuanLyTu_click)

    def setWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen :
            self.window.showFullScreen()
    
    def btQuanLyTu_click(self):
        self.ui = Ui_setThemTu()
        self.setWindow()

    def btMoiTruongVH_click(self):
        self.ui = Ui_setDieuKienVanHanh()
        self.setWindow()
    
    def btThongGio_click(self):
        self.ui = Ui_setThongGio()
        self.setWindow()

    def btLucKet_click(self):
        self.ui = Ui_setLucChongKet()
        self.setWindow()

    def btDoiMatKhau_click(self):
        self.ui = Ui_setPassword()
        self.setWindow()

    def btKCMotu_click(self):
        self.ui = Ui_setKCMoTu()
        self.setWindow()
        
    def btKCGiamToc_click(self):
        self.ui = Ui_setKCGiamToc()
        self.setWindow()
        
    def btTocDoDC_click(self):
        self.ui = Ui_setTocDoDc()
        self.setWindow()
        
    def btChieuDC_click(self):
        self.ui = Ui_setChieuQuayDC()
        self.window = QtWidgets.QMainWindow()
        if server.numClientLeft > 0 :
            self.ui.setupUi(self.window)
        else :
            self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen :
            self.window.showFullScreen()

    def btBaoDuong_click(self):
        self.ui = Ui_BaoDuongServer()
        self.setWindow()  
        
import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVCaiDatNangCao = QtWidgets.QWidget()
    ui = Ui_SVCaiDatNangCao()
    ui.setupUi(SVCaiDatNangCao)
    SVCaiDatNangCao.show()
    sys.exit(app.exec_())

"""