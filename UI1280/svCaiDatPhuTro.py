# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SV_CaiDatPhuTro1280.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SVCaiDatPhuTro(object):
    def setupUi(self, SVCaiDatPhuTro):
        SVCaiDatPhuTro.setObjectName("SVCaiDatPhuTro")
        SVCaiDatPhuTro.resize(1280, 800)
        self.SVCaiDatPhuTro = SVCaiDatPhuTro
        self.frame = QtWidgets.QFrame(SVCaiDatPhuTro)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#lbtitle{color:red ;font: 75  30pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}#btBack{color:white;border-image: url(:/images/back.png);}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}")
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
        self.btMoKhoa = QtWidgets.QPushButton(self.frame)
        self.btMoKhoa.setGeometry(QtCore.QRect(560, 460, 181, 81))
        self.btMoKhoa.setObjectName("btMoKhoa")
        self.btCdGoc = QtWidgets.QPushButton(self.frame)
        self.btCdGoc.setGeometry(QtCore.QRect(830, 460, 181, 81))
        self.btCdGoc.setObjectName("btCdGoc")
        self.btBack = QtWidgets.QPushButton(self.frame)
        self.btBack.setGeometry(QtCore.QRect(830, 580, 181, 81))
        self.btBack.setObjectName("btBack")
        self.btHocLenhDieuHoa = QtWidgets.QPushButton(self.frame)
        self.btHocLenhDieuHoa.setGeometry(QtCore.QRect(290, 580, 181, 81))
        self.btHocLenhDieuHoa.setObjectName("btHocLenhDieuHoa")
        self.btDkDieuHoa = QtWidgets.QPushButton(self.frame)
        self.btDkDieuHoa.setGeometry(QtCore.QRect(560, 580, 181, 81))
        self.btDkDieuHoa.setObjectName("btDkDieuHoa")

        self.retranslateUi(SVCaiDatPhuTro)
        QtCore.QMetaObject.connectSlotsByName(SVCaiDatPhuTro)

    def retranslateUi(self, SVCaiDatPhuTro):
        _translate = QtCore.QCoreApplication.translate
        SVCaiDatPhuTro.setWindowTitle(_translate("SVCaiDatPhuTro", "Form"))
        self.lbtitle.setText(_translate("SVCaiDatPhuTro", "Cài đặt phụ trợ"))
        self.btDcThoiGian.setText(_translate("SVCaiDatPhuTro", "Điều chỉnh\n"
" thời gian"))
        self.btCdTinhNang.setText(_translate("SVCaiDatPhuTro", "Cài đặt\n"
" tính năng"))
        self.btThamSlave.setText(_translate("SVCaiDatPhuTro", "Thăm dò\n"
" máy chủ"))
        self.btTietKiemNangLuong.setText(_translate("SVCaiDatPhuTro", "Tiết kiệm\n"
" năng lượng"))
        self.btAmBao.setText(_translate("SVCaiDatPhuTro", "Âm báo\n"
" nhắc nhở"))
        self.btHuyThongBao.setText(_translate("SVCaiDatPhuTro", "Hủy\n"
" thông báo"))
        self.btKhoa.setText(_translate("SVCaiDatPhuTro", "Khóa"))
        self.btMoKhoa.setText(_translate("SVCaiDatPhuTro", "Mở khóa"))
        self.btCdGoc.setText(_translate("SVCaiDatPhuTro", "Khôi phục\n"
" cài đặt gốc"))
        self.btBack.setText(_translate("SVCaiDatPhuTro", "Quay lại"))
        self.btHocLenhDieuHoa.setText(_translate("SVCaiDatPhuTro", "Học lệnh\n"
"điều hòa"))
        self.btDkDieuHoa.setText(_translate("SVCaiDatPhuTro", "Điều khiển\n"
"điều hòa"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SVCaiDatPhuTro = QtWidgets.QWidget()
    ui = Ui_SVCaiDatPhuTro()
    ui.setupUi(SVCaiDatPhuTro)
    SVCaiDatPhuTro.show()
    sys.exit(app.exec_())

