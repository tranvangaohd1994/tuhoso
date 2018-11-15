# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setLucChongKet.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_setLucChongKet(object):
    def setupUi(self, setLucChongKet):
        setLucChongKet.setObjectName("setLucChongKet")
        setLucChongKet.resize(1280, 800)
        setLucChongKet.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setLucChongKet)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}.QLabel{color:#FF8F00;font: 75 32pt \"Ubuntu\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Ubuntu\";}#lbHuongDan{font: 75 18pt \"Ubuntu\";color:#ffff35}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 120, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Ubuntu\";\n"
                "background-color: rgb(0, 0, 0);\n"
                "color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 370, 421, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(30, 630, 421, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 520, 421, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(860, 670, 151, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1110, 670, 151, 101))
        self.btExit.setObjectName("btExit")
        self.tbLCKHienTai = QtWidgets.QLineEdit(self.frame)
        self.tbLCKHienTai.setGeometry(QtCore.QRect(30, 420, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbLCKHienTai.setFont(font)
        self.tbLCKHienTai.setObjectName("tbLCKHienTai")
        self.tbLCKCaiDat = QtWidgets.QLineEdit(self.frame)
        self.tbLCKCaiDat.setGeometry(QtCore.QRect(30, 570, 421, 61))
      
        self.tbLCKCaiDat.setFont(font)
        self.tbLCKCaiDat.setObjectName("tbLCKCaiDat")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(810, 210, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lbHuongDan = QtWidgets.QLabel(self.frame)
        self.lbHuongDan.setGeometry(QtCore.QRect(750, 270, 511, 311))
        self.lbHuongDan.setWordWrap(True)
        self.lbHuongDan.setObjectName("lbHuongDan")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(30, 220, 421, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbChonTu = QtWidgets.QLineEdit(self.frame)
        self.tbChonTu.setGeometry(QtCore.QRect(30, 270, 421, 61))
        
        self.tbChonTu.setFont(font)
        self.tbChonTu.setObjectName("tbChonTu")

        self.retranslateUi(setLucChongKet)
        QtCore.QMetaObject.connectSlotsByName(setLucChongKet)

    def retranslateUi(self, setLucChongKet):
        _translate = QtCore.QCoreApplication.translate
        setLucChongKet.setWindowTitle(_translate("setLucChongKet", "Form"))
        self.label.setText(_translate("setLucChongKet", "Cài đặt lực chống kẹt"))
        self.label_2.setText(_translate("setLucChongKet", "Hiện đang cài đặt"))
        self.label_3.setText(_translate("setLucChongKet", "Giá trị : 0-10"))
        self.label_4.setText(_translate("setLucChongKet", "Nhập cấp độ lực kẹt"))
        self.btSave.setText(_translate("setLucChongKet", "Lưu"))
        self.btExit.setText(_translate("setLucChongKet", "Thoát"))
        self.tbLCKHienTai.setText(_translate("setLucChongKet", "5"))
        self.label_5.setText(_translate("setLucChongKet", "Hướng dẫn"))
        self.lbHuongDan.setText(_translate("setLucChongKet", "- Khi cài đặt hiển thị số cột di dộng, số Seri bằng 0 nghĩa là cài đặt đồng bộ giá trị cho toàn bộ cột trong khu vực giống nhau\n"
                "- Cấp độ chống kẹt L\n"
                " + 0 là đóng chức năng chống kẹt\n"
                " + 1-3 là cấp độ nhỏ\n"
                " + 4-7 là cấp độ thường\n"
                " + 8-10 là cấp độ mạnh nhất ứng với tải lớn\n"
                " + 5 là cấp độ cài đặt mặc định"))
        self.label_6.setText(_translate("setLucChongKet", "Nhập tủ cài đặt"))
        self.tbChonTu.setText(_translate("setLucChongKet", "0"))

import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setLucChongKet = QtWidgets.QWidget()
    ui = Ui_setLucChongKet()
    ui.setupUi(setLucChongKet)
    setLucChongKet.show()
    sys.exit(app.exec_())

