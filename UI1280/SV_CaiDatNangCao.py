# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CaiDatNangCao.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SVCaiDatNangCao(object):
    def setupUi(self, SVCaiDatNangCao):
        SVCaiDatNangCao.setObjectName("SVCaiDatNangCao")
        SVCaiDatNangCao.resize(1280, 800)
        self.frame = QtWidgets.QFrame(SVCaiDatNangCao)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/Background.jpg);}#lbtitle{color:red ;font: 75  30pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}#btBack{color:white;border-image: url(:/images/back.png);}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(480, 130, 401, 51))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btLucKet = QtWidgets.QPushButton(self.frame)
        self.btLucKet.setGeometry(QtCore.QRect(270, 210, 191, 91))
        self.btLucKet.setObjectName("btLucKet")
        self.btChieuDC = QtWidgets.QPushButton(self.frame)
        self.btChieuDC.setGeometry(QtCore.QRect(590, 210, 191, 91))
        self.btChieuDC.setObjectName("btChieuDC")
        self.btTocDoDC = QtWidgets.QPushButton(self.frame)
        self.btTocDoDC.setGeometry(QtCore.QRect(910, 210, 191, 91))
        self.btTocDoDC.setObjectName("btTocDoDC")
        self.btKCMotu = QtWidgets.QPushButton(self.frame)
        self.btKCMotu.setGeometry(QtCore.QRect(270, 330, 191, 91))
        self.btKCMotu.setObjectName("btKCMotu")
        self.btKCGiamToc = QtWidgets.QPushButton(self.frame)
        self.btKCGiamToc.setGeometry(QtCore.QRect(590, 330, 191, 91))
        self.btKCGiamToc.setObjectName("btKCGiamToc")
        self.btTatCamBien = QtWidgets.QPushButton(self.frame)
        self.btTatCamBien.setGeometry(QtCore.QRect(910, 330, 191, 91))
        self.btTatCamBien.setObjectName("btTatCamBien")
        self.btCheDoBaoDuong = QtWidgets.QPushButton(self.frame)
        self.btCheDoBaoDuong.setGeometry(QtCore.QRect(270, 570, 191, 91))
        self.btCheDoBaoDuong.setObjectName("btCheDoBaoDuong")
        self.btDoiMatKhau = QtWidgets.QPushButton(self.frame)
        self.btDoiMatKhau.setGeometry(QtCore.QRect(590, 570, 191, 91))
        self.btDoiMatKhau.setObjectName("btDoiMatKhau")
        self.btCdGoc = QtWidgets.QPushButton(self.frame)
        self.btCdGoc.setGeometry(QtCore.QRect(910, 570, 191, 91))
        self.btCdGoc.setObjectName("btCdGoc")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(1090, 690, 181, 91))
        self.btBack.setObjectName("btBack")
        self.btQuanLyTu = QtWidgets.QPushButton(self.frame)
        self.btQuanLyTu.setGeometry(QtCore.QRect(910, 450, 191, 91))
        self.btQuanLyTu.setObjectName("btQuanLyTu")
        self.btMoiTruongVH = QtWidgets.QPushButton(self.frame)
        self.btMoiTruongVH.setGeometry(QtCore.QRect(270, 450, 191, 91))
        self.btMoiTruongVH.setObjectName("btMoiTruongVH")
        self.btThongGio = QtWidgets.QPushButton(self.frame)
        self.btThongGio.setGeometry(QtCore.QRect(590, 450, 191, 91))
        self.btThongGio.setObjectName("btThongGio")

        self.retranslateUi(SVCaiDatNangCao)
        QtCore.QMetaObject.connectSlotsByName(SVCaiDatNangCao)

    def retranslateUi(self, SVCaiDatNangCao):
        _translate = QtCore.QCoreApplication.translate
        SVCaiDatNangCao.setWindowTitle(_translate("SVCaiDatNangCao", "Form"))
        self.lbtitle.setText(_translate("SVCaiDatNangCao", "Cài đặt nâng cao"))
        self.btLucKet.setText(_translate("SVCaiDatNangCao", "Cấp độ Lực\n"
"chống kẹt"))
        self.btChieuDC.setText(_translate("SVCaiDatNangCao", "Chiều quay\n"
" Động cơ"))
        self.btTocDoDC.setText(_translate("SVCaiDatNangCao", "Tốc độ\n"
" Động cơ"))
        self.btKCMotu.setText(_translate("SVCaiDatNangCao", "Khoảng cách\n"
" Mở tủ"))
        self.btKCGiamToc.setText(_translate("SVCaiDatNangCao", "Khoảng cách\n"
" giảm tốc"))
        self.btTatCamBien.setText(_translate("SVCaiDatNangCao", "Tắt\n"
" Cảm biến"))
        self.btCheDoBaoDuong.setText(_translate("SVCaiDatNangCao", "Chế độ\n"
" Bảo dưỡng"))
        self.btDoiMatKhau.setText(_translate("SVCaiDatNangCao", "Đổi\n"
" Mật khẩu"))
        self.btCdGoc.setText(_translate("SVCaiDatNangCao", "Khôi Phục\n"
" Cài đặt gốc"))
        self.btBack.setText(_translate("SVCaiDatNangCao", "Quay lại"))
        self.btQuanLyTu.setText(_translate("SVCaiDatNangCao", "Quản lý tủ"))
        self.btMoiTruongVH.setText(_translate("SVCaiDatNangCao", "Môi Trường\n"
" vận hành"))
        self.btThongGio.setText(_translate("SVCaiDatNangCao", "Thông gió"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVCaiDatNangCao = QtWidgets.QWidget()
    ui = Ui_SVCaiDatNangCao()
    ui.setupUi(SVCaiDatNangCao)
    SVCaiDatNangCao.show()
    sys.exit(app.exec_())

