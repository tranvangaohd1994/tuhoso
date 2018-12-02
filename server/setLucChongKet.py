# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setLucChongKet.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from kbNumber import Ui_Dialog , MSG_Dialog
from PyQt5.QtCore import pyqtSignal
import server

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setLucChongKet(object):
    def setupUi(self, setLucChongKet):
        setLucChongKet.setObjectName("setLucChongKet")
        setLucChongKet.resize(1280, 800)
        setLucChongKet.setStyleSheet("")
        self.setLucChongKet = setLucChongKet
        self.frame = QtWidgets.QFrame(setLucChongKet)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}#lbHuongDan{font: 75 18pt \"Arial\";color:#ffff35}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
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
        self.tbLCKHienTai = MyQLineEdit(self.frame)
        self.tbLCKHienTai.setGeometry(QtCore.QRect(30, 420, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbLCKHienTai.setFont(font)
        self.tbLCKHienTai.setObjectName("tbLCKHienTai")

        self.tbLCKCaiDat = MyQLineEdit(self.frame)
        self.tbLCKCaiDat.setGeometry(QtCore.QRect(30, 570, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbLCKCaiDat.setFont(font)
        self.tbLCKCaiDat.setObjectName("tbLCKCaiDat")

        self.tbChonTu = MyQLineEdit(self.frame)
        self.tbChonTu.setGeometry(QtCore.QRect(30, 270, 421, 61))
        self.tbChonTu.setFont(font)
        self.tbChonTu.setObjectName("tbChonTu")

        self.label_chontu = QtWidgets.QLabel(self.frame)
        self.label_chontu.setGeometry(QtCore.QRect(30, 220, 421, 50))
        self.label_chontu.setStyleSheet("")
        self.label_chontu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chontu.setObjectName("label_chontu")


        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(810, 210, 361, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lbHuongDan = QtWidgets.QLabel(self.frame)
        self.lbHuongDan.setGeometry(QtCore.QRect(750, 270, 511, 311))
        self.lbHuongDan.setWordWrap(True)
        self.lbHuongDan.setObjectName("lbHuongDan")

        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(10, 670, 481, 121))
        self.grcdControl.setStyleSheet(".QRadioButton{font: 75 Bold 26pt \"Ubuntu\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbTuPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuPhai.setGeometry(QtCore.QRect(260, 10, 181, 100))
        self.rbTuPhai.setObjectName("rbTuPhai")
        self.rbTuTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbTuTrai.setGeometry(QtCore.QRect(20, 10, 181, 100))
        self.rbTuTrai.setChecked(True)
        self.rbTuTrai.setObjectName("rbTuTrai")

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
        self.tbChonTu.setText(_translate("setLucChongKet", "0"))
        self.label_5.setText(_translate("setLucChongKet", "Hướng dẫn"))
        self.label_chontu.setText(_translate("setLucChongKet", "Chọn tủ cài đặt"))
        self.lbHuongDan.setText(_translate("setLucChongKet", "- Khi cài đặt hiển thị số cột di dộng, số Seri bằng 0 nghĩa là cài đặt đồng bộ giá trị cho toàn bộ cột trong khu vực giống nhau\n"
            "- Cấp độ chống kẹt L\n"
            " + 0 là đóng chức năng chống kẹt\n"
            " + 1-3 là cấp độ nhỏ\n"
            " + 4-7 là cấp độ thường\n"
            " + 8-10 là cấp độ mạnh nhất ứng với tải lớn\n"
            " + 5 là cấp độ cài đặt mặc định"))
        self.rbTuPhai.setText(_translate("setLucChongKet", "Tủ phải"))
        self.rbTuTrai.setText(_translate("setLucChongKet", "Tủ trái"))
        self.setEvent()

    def setEvent(self):
        self.tbLCKHienTai.setText(str(int(server.dataSent2Client["Left_1"].dt2Pi2Ar[4])))

        self.tbChonTu.clicked.connect(self.tbChonTu_click)
        self.tbLCKHienTai.clicked.connect(self.tbLCKHienTai_click)
        self.tbLCKCaiDat.clicked.connect(self.tbLCKCaiDat_click)
        self.btSave.clicked.connect(self.btSave_click)
        self.btExit.clicked.connect(self.btExit_click)

    def tbChonTu_click(self):
        dialogKey= Ui_Dialog(server.numClientLeft)
        value = dialogKey.exec_()
        if value :
            self.tbChonTu.setText(value)
        if self.rbTuTrai.isChecked():
            firstName = 'Left_'
        else :
            firstName = 'Right_'

        if self.tbChonTu.text() == '0': #neu bang khong thi luc chong ket cac tu la nhu nhau
            if firstName[0] == 'L' and server.numClientLeft > 0 :
                self.tbLCKHienTai.setText(str(int(server.dataSent2Client["Left_1"].dt2Pi2Ar[4])))
            elif firstName[0] == 'R' and server.numClientRight > 0:
                self.tbLCKHienTai.setText(str(int(server.dataSent2Client["Right_1"].dt2Pi2Ar[4])))
            else :
                self.tbLCKHienTai.setText('0')
        else :
            self.tbLCKHienTai.setText(str(int(server.dataSent2Client[firstName+self.tbChonTu.text()].dt2Pi2Ar[4])))

    def btExit_click(self):
        self.setLucChongKet.close()
        pass
    def btSave_click(self):
        if len(self.tbLCKCaiDat.text()) > 0:
            if self.rbTuTrai.isChecked() :
                firstName = 'Left_'
                maxTu = server.numClientLeft
            else :
                firstName = 'Right_'
                maxTu = server.numClientRight

            if self.tbChonTu.text() == '0':
                for i in range(1,maxTu+1):
                    nameTu = firstName+str(i)
                    server.dataSent2Client[nameTu].dt2Pi2Ar[4] = int(self.tbLCKCaiDat.text())
                    server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
            else :
                nameTu = firstName+self.tbChonTu.text()
                server.dataSent2Client[nameTu].dt2Pi2Ar[4] = int(self.tbLCKCaiDat.text())
                server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
            
            dialog = MSG_Dialog()
            dialog.exec_()
        
    def tbLCKHienTai_click(self):
        pass
    def tbLCKCaiDat_click(self):
        dialogKey= Ui_Dialog(10)
        value = dialogKey.exec_()
        if value :
            self.tbLCKCaiDat.setText(value)

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setLucChongKet = QtWidgets.QWidget()
    ui = Ui_setLucChongKet()
    ui.setupUi(setLucChongKet)
    setLucChongKet.show()
    sys.exit(app.exec_())

"""