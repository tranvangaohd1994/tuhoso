# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formTimKiem.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,pyqtSignal,QEventLoop
import struct
import time

import server
import masterPC

from keyboardVN import Ui_KeyboardVN
from fKetQuaTraCuu import Ui_fKetQuaTraCuu
from kbNumber import Ui_Dialog


class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_formTimKiem(object):
    def setupUi(self, formTimKiem):
        formTimKiem.setObjectName("formTimKiem")
        formTimKiem.resize(1280, 800)
        formTimKiem.setStyleSheet("")
        self.formTimKiem = formTimKiem
        self.frame = QtWidgets.QFrame(formTimKiem)
        self.frame.setGeometry(QtCore.QRect(0, 0, 12800, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}.QPushButton:pressed { background-color: #4164ff}.QPushButton{border-radius: 18px;background-color: #FFC107;font: 75 18pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 30pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1271, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.bttcTenTapHS = QtWidgets.QPushButton(self.frame)
        self.bttcTenTapHS.setGeometry(QtCore.QRect(20, 270, 391, 71))
        self.bttcTenTapHS.setObjectName("bttcTenTapHS")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1020, 640, 161, 111))
        self.btExit.setObjectName("btExit")
        self.tbTimKiem = MyQLineEdit(self.frame)
        self.tbTimKiem.setGeometry(QtCore.QRect(590, 530, 671, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbTimKiem.setFont(font)
        self.tbTimKiem.setObjectName("tbTimKiem")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(90, 190, 281, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbNam = MyQLineEdit(self.frame)
        self.tbNam.setGeometry(QtCore.QRect(1020, 270, 101, 61))
        
        self.tbNam.setFont(font)
        self.tbNam.setObjectName("tbNam")
        self.bttcSeriTapHS = QtWidgets.QPushButton(self.frame)
        self.bttcSeriTapHS.setGeometry(QtCore.QRect(20, 380, 391, 71))
        self.bttcSeriTapHS.setObjectName("bttcSeriTapHS")
        self.bttcKetQuaLanTruoc = QtWidgets.QPushButton(self.frame)
        self.bttcKetQuaLanTruoc.setGeometry(QtCore.QRect(20, 490, 401, 71))
        self.bttcKetQuaLanTruoc.setObjectName("bttcKetQuaLanTruoc")
        self.bttcBanGhiDaThaotac = QtWidgets.QPushButton(self.frame)
        self.bttcBanGhiDaThaotac.setGeometry(QtCore.QRect(20, 590, 401, 71))
        self.bttcBanGhiDaThaotac.setObjectName("bttcBanGhiDaThaotac")
        self.bttcGhiNhoQuanLy = QtWidgets.QPushButton(self.frame)
        self.bttcGhiNhoQuanLy.setGeometry(QtCore.QRect(20, 690, 401, 61))
        self.bttcGhiNhoQuanLy.setObjectName("bttcGhiNhoQuanLy")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(590, 190, 671, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(730, 270, 211, 61))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(580, 350, 691, 50))
        self.label_9.setStyleSheet("")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(650, 460, 551, 50))
        self.lbThongBao.setStyleSheet("")
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setObjectName("lbThongBao")
        self.btTraCuu = QtWidgets.QPushButton(self.frame)
        self.btTraCuu.setGeometry(QtCore.QRect(650, 640, 171, 111))
        self.btTraCuu.setObjectName("btTraCuu")

        self.retranslateUi(formTimKiem)
        QtCore.QMetaObject.connectSlotsByName(formTimKiem)

    def retranslateUi(self, formTimKiem):
        _translate = QtCore.QCoreApplication.translate
        formTimKiem.setWindowTitle(_translate("formTimKiem", "Form"))
        self.label.setText(_translate("formTimKiem", "Tra Cứu"))
        self.bttcTenTapHS.setText(_translate("formTimKiem", "Tra cứu tên tập hồ sơ"))
        self.btExit.setText(_translate("formTimKiem", "Thoát"))
        self.tbTimKiem.setText(_translate("formTimKiem", "10"))
        self.label_6.setText(_translate("formTimKiem", "Tra cứu hồ sơ"))
        self.tbNam.setText(_translate("formTimKiem", "10"))
        self.bttcSeriTapHS.setText(_translate("formTimKiem", "Tra cứu số Seri tập hồ sơ"))
        self.bttcKetQuaLanTruoc.setText(_translate("formTimKiem", "Kết quả tra cứu lần trước"))
        self.bttcBanGhiDaThaotac.setText(_translate("formTimKiem", "Tra cứu bản ghi đã thao tác"))
        self.bttcGhiNhoQuanLy.setText(_translate("formTimKiem", "Tra cứu ghi nhớ người quản lý"))
        self.label_7.setText(_translate("formTimKiem", "Tra cứu bản ghi người dùng thao tác"))
        self.label_8.setText(_translate("formTimKiem", "Nhập năm"))
        self.label_9.setText(_translate("formTimKiem", "Số năm có hiệu lực là 10 năm gần đây"))
        self.lbThongBao.setText(_translate("formTimKiem", "Nhập từ khóa tra cứu"))
        self.btTraCuu.setText(_translate("formTimKiem", "Tra Cứu"))

        self.setEvent()

    def setEvent(self):
        self.btExit.clicked.connect(self.formTimKiem.close)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.tbTimKiem.clicked.connect(self.tbTimKiem_click)
        self.tbNam.clicked.connect(self.tbNam_click)
        
    def tbNam_click(self):
        dialogKey = Ui_Dialog(20,False)
        value = dialogKey.exec_()
        self.tbTimKiem.setText(value)

    def tbTimKiem_click(self):
        dialogKey = Ui_KeyboardVN()
        value = dialogKey.exec_()
        self.tbTimKiem.setText(value)
    
    def setWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        if server.isFullSceen:
            self.window.showFullScreen()

    def btTraCuu_click(self):
        self.sentTimKiem2PC()

        self.ui = Ui_fKetQuaTraCuu()
        self.setWindow()

    def sentTimKiem2PC(self): # tam toi send tim kiem tong quat den PC
        if masterPC.ServerPC.isConnectPC :
            masterPC.ServerPC.csdl = []
            header = b'\x23\x23\x23\x31\x32\x61'
            data = str(self.tbTimKiem.text())
            dt = data.encode('utf8')
            lenData = struct.pack('I', int(len(dt)))
            header = header + lenData + b'\x00\x00' # 2 byte cuoi la CRC
            if len(header) == 12 :
                header += dt
                masterPC.ServerPC.conn.send(header)
                print("sent yeu cau den PC : ", header )
                time.sleep(0.2)
        

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formTimKiem = QtWidgets.QWidget()
    ui = Ui_formTimKiem()
    ui.setupUi(formTimKiem)
    formTimKiem.show()
    sys.exit(app.exec_())

"""