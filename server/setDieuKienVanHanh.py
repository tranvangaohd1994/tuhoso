# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setDieuKienVanHanh.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from kbNumber import Ui_Dialog

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setDieuKienVanHanh(object):
    def setupUi(self, setDieuKienVanHanh):
        setDieuKienVanHanh.setObjectName("setDieuKienVanHanh")
        setDieuKienVanHanh.resize(1280, 800)
        setDieuKienVanHanh.setStyleSheet("")
        self.setDieuKienVanHanh = setDieuKienVanHanh
        self.frame = QtWidgets.QFrame(setDieuKienVanHanh)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}.QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 32pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}#lbHuongDan{font: 75 22pt \"Arial\";color:#ffff35}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-7, 110, 1291, 71))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 460, 221, 50))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(270, 650, 181, 111))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(960, 650, 161, 111))
        self.btExit.setObjectName("btExit")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(880, 200, 301, 51))
        self.label_5.setStyleSheet("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.lbHuongDan = QtWidgets.QLabel(self.frame)
        self.lbHuongDan.setGeometry(QtCore.QRect(840, 260, 411, 371))
        self.lbHuongDan.setWordWrap(True)
        self.lbHuongDan.setObjectName("lbHuongDan")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(70, 290, 231, 50))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.tbTempFrom = MyQLineEdit(self.frame)
        self.tbTempFrom.setGeometry(QtCore.QRect(330, 280, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(32)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbTempFrom.setFont(font)
        self.tbTempFrom.setObjectName("tbTempFrom")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(460, 290, 101, 50))
        self.label_7.setStyleSheet("")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(460, 460, 101, 50))
        self.label_8.setStyleSheet("")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.tbTempTo = MyQLineEdit(self.frame)
        self.tbTempTo.setGeometry(QtCore.QRect(600, 280, 91, 61))
        self.tbTempTo.setFont(font)
        self.tbTempTo.setObjectName("tbTempTo")
        self.tbHumiTo = MyQLineEdit(self.frame)
        self.tbHumiTo.setGeometry(QtCore.QRect(600, 450, 91, 61))
        self.tbHumiTo.setFont(font)
        self.tbHumiTo.setObjectName("tbHumiTo")
        self.tbHumiFrom = MyQLineEdit(self.frame)
        self.tbHumiFrom.setGeometry(QtCore.QRect(330, 450, 91, 61))
        self.tbHumiFrom.setFont(font)
        self.tbHumiFrom.setObjectName("tbHumiFrom")

        self.retranslateUi(setDieuKienVanHanh)
        QtCore.QMetaObject.connectSlotsByName(setDieuKienVanHanh)

    def retranslateUi(self, setDieuKienVanHanh):
        _translate = QtCore.QCoreApplication.translate
        setDieuKienVanHanh.setWindowTitle(_translate("setDieuKienVanHanh", "Form"))
        self.label.setText(_translate("setDieuKienVanHanh", "Thiết lập môi trường vận hành"))
        self.label_2.setText(_translate("setDieuKienVanHanh", "Độ ẩm(%)"))
        self.btSave.setText(_translate("setDieuKienVanHanh", "Lưu"))
        self.btExit.setText(_translate("setDieuKienVanHanh", "Thoát"))
        self.label_5.setText(_translate("setDieuKienVanHanh", "Mô tả thông số"))
        self.lbHuongDan.setText(_translate("setDieuKienVanHanh", "Đây là thông số cài đặt cho môi trường vận hành bình thường của hệ thống lưu trữ.\n"
"Trong quá trình vận hành nếu nhiệt độ hoặc độ ẩm vượt ra ngoài dải cho phép thì hệ thống sẽ tự động kích hoạt các thiết bị điều hòa, hút ẩm để đưa hệ thống về nhiệt độ cho phép hoạt động."))
        self.label_6.setText(_translate("setDieuKienVanHanh", "Nhiệt độ(C)"))
        self.tbTempFrom.setText(_translate("setDieuKienVanHanh", "20"))
        self.label_7.setText(_translate("setDieuKienVanHanh", "Đến"))
        self.label_8.setText(_translate("setDieuKienVanHanh", "Đến"))
        self.tbTempTo.setText(_translate("setDieuKienVanHanh", "20"))
        self.tbHumiTo.setText(_translate("setDieuKienVanHanh", "20"))
        self.tbHumiFrom.setText(_translate("setDieuKienVanHanh", "20"))

        self.setEvent()

    def setEvent(self) :
        self.btExit.clicked.connect(self.setDieuKienVanHanh.close)

        self.tbTempTo.clicked.connect(self.tbTempTo_click)
        self.tbTempFrom.clicked.connect(self.tbTempFrom_click)
        self.tbHumiTo.clicked.connect(self.tbHumiTo_click)
        self.tbHumiFrom.clicked.connect(self.tbHumiFrom_click)

        self.btSave.clicked.connect(self.btSave_click)
        self.kichHoat = False

    def tbTempTo_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbTempTo.setText(value)

    def tbTempFrom_click(self):
        dialogKey= Ui_Dialog(60)
        value = dialogKey.exec_()
        if value :
            self.tbTempFrom.setText(value)

    def tbHumiTo_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbHumiTo.setText(value)
    
    def tbHumiFrom_click(self):
        dialogKey= Ui_Dialog(100)
        value = dialogKey.exec_()
        if value :
            self.tbHumiFrom.setText(value)


    def btSave_click(self):
        pass



import resources

"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setDieuKienVanHanh = QtWidgets.QWidget()
    ui = Ui_setDieuKienVanHanh()
    ui.setupUi(setDieuKienVanHanh)
    setDieuKienVanHanh.show()
    sys.exit(app.exec_())

"""