# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainDisplay.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMouseEvent


class Ui_SV_mainDisplay(QMainWindow):
    def __init__(self):
        super(Ui_SV_mainDisplay,self).__init__()
    def setupUi(self):
        SV_mainDisplay = self
        SV_mainDisplay.setObjectName("SV_mainDisplay")
        SV_mainDisplay.resize(1280, 800)
        SV_mainDisplay.setStyleSheet(".QFrame{background-image: url(:/images/mainLayout.png);}")
        self.centralwidget = QtWidgets.QWidget(SV_mainDisplay)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet("#grTopMain{background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);}QGroupBox {border-radius: 10px;}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 10px;background-color: #4e9400;font: bold 20pt \"Arial\";color:#ffffff}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.grTempOut = QtWidgets.QGroupBox(self.frame)
        self.grTempOut.setGeometry(QtCore.QRect(620, 550, 581, 111))
        self.grTempOut.setStyleSheet(".QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Ubuntu\";}#lbTempOutValue{color: rgb(255, 0,0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiOutValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbTempInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}#lbHumiInValue{color: rgb(255, 0, 0);font: 75 Bold 22pt \"Ubuntu\";}")
        self.grTempOut.setTitle("")
        self.grTempOut.setObjectName("grTempOut")
        self.lbTempOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempOutValue.setGeometry(QtCore.QRect(210, 60, 81, 45))
        self.lbTempOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempOutValue.setObjectName("lbTempOutValue")
        self.lbHumiOutValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiOutValue.setGeometry(QtCore.QRect(460, 60, 91, 45))
        self.lbHumiOutValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiOutValue.setObjectName("lbHumiOutValue")
        self.lbTempInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbTempInValue.setGeometry(QtCore.QRect(210, 20, 81, 45))
        self.lbTempInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTempInValue.setObjectName("lbTempInValue")
        self.lbHumiInValue = QtWidgets.QLabel(self.grTempOut)
        self.lbHumiInValue.setGeometry(QtCore.QRect(460, 20, 91, 45))
        self.lbHumiInValue.setAlignment(QtCore.Qt.AlignCenter)
        self.lbHumiInValue.setObjectName("lbHumiInValue")
        self.grStatusMotor = QtWidgets.QGroupBox(self.frame)
        self.grStatusMotor.setGeometry(QtCore.QRect(100, 250, 481, 171))
        self.grStatusMotor.setStyleSheet(".QLabel{color :#ff0000;font: bold 22pt \"Arial\";}")
        self.grStatusMotor.setTitle("")
        self.grStatusMotor.setObjectName("grStatusMotor")
        self.lbTrongKho = QtWidgets.QLabel(self.grStatusMotor)
        self.lbTrongKho.setGeometry(QtCore.QRect(160, 50, 101, 45))
        self.lbTrongKho.setAlignment(QtCore.Qt.AlignCenter)
        self.lbTrongKho.setObjectName("lbTrongKho")
        self.lbChoMuon = QtWidgets.QLabel(self.grStatusMotor)
        self.lbChoMuon.setGeometry(QtCore.QRect(160, 100, 101, 45))
        self.lbChoMuon.setAlignment(QtCore.Qt.AlignCenter)
        self.lbChoMuon.setObjectName("lbChoMuon")
        self.btKiemTra = QtWidgets.QPushButton(self.grStatusMotor)
        self.btKiemTra.setGeometry(QtCore.QRect(280, 60, 161, 81))
        self.btKiemTra.setObjectName("btKiemTra")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(5, 5, 101, 81))
        self.btExit.setStyleSheet("border: none;background-color: none;")
        self.btExit.setText("")
        self.btExit.setObjectName("btExit")
        self.grControl = QtWidgets.QGroupBox(self.frame)
        self.grControl.setGeometry(QtCore.QRect(90, 370, 461, 411))
        self.grControl.setStyleSheet("#grControl{ border: 0px solid gray; border-radius: 0px; } ")
        self.grControl.setTitle("")
        self.grControl.setObjectName("grControl")
        self.btTroGiup = QtWidgets.QPushButton(self.grControl)
        self.btTroGiup.setGeometry(QtCore.QRect(54, 248, 161, 80))
        self.btTroGiup.setObjectName("btTroGiup")
        self.btQuanLy = QtWidgets.QPushButton(self.grControl)
        self.btQuanLy.setGeometry(QtCore.QRect(254, 248, 161, 80))
        self.btQuanLy.setObjectName("btQuanLy")
        self.btDongTu = QtWidgets.QPushButton(self.grControl)
        self.btDongTu.setGeometry(QtCore.QRect(254, 50, 161, 80))
        self.btDongTu.setObjectName("btDongTu")
        self.btKhoaDC = QtWidgets.QPushButton(self.grControl)
        self.btKhoaDC.setGeometry(QtCore.QRect(54, 150, 161, 80))
        self.btKhoaDC.setObjectName("btKhoaDC")
        self.btTraCuu = QtWidgets.QPushButton(self.grControl)
        self.btTraCuu.setGeometry(QtCore.QRect(254, 150, 161, 80))
        self.btTraCuu.setObjectName("btTraCuu")
        self.btMoTu = QtWidgets.QPushButton(self.grControl)
        self.btMoTu.setGeometry(QtCore.QRect(54, 50, 161, 80))
        self.btMoTu.setObjectName("btMoTu")
        self.grWarning = QtWidgets.QGroupBox(self.frame)
        self.grWarning.setGeometry(QtCore.QRect(610, 230, 581, 301))
        self.grWarning.setStyleSheet(".QLabel{color: rgb(255, 0, 0);font: Bold 22pt \"Arial\";}")
        self.grWarning.setTitle("")
        self.grWarning.setObjectName("grWarning")
        self.lbKhoangCach = QtWidgets.QLabel(self.grWarning)
        self.lbKhoangCach.setGeometry(QtCore.QRect(260, 135, 111, 45))
        self.lbKhoangCach.setAlignment(QtCore.Qt.AlignCenter)
        self.lbKhoangCach.setObjectName("lbKhoangCach")
        self.lbstatusMotor = QtWidgets.QLabel(self.grWarning)
        self.lbstatusMotor.setGeometry(QtCore.QRect(200, 55, 281, 45))
        self.lbstatusMotor.setAlignment(QtCore.Qt.AlignCenter)
        self.lbstatusMotor.setObjectName("lbstatusMotor")
        self.lbSoNguoi = QtWidgets.QLabel(self.grWarning)
        self.lbSoNguoi.setGeometry(QtCore.QRect(260, 100, 101, 41))
        self.lbSoNguoi.setAlignment(QtCore.Qt.AlignCenter)
        self.lbSoNguoi.setObjectName("lbSoNguoi")
        self.lbWarning = QtWidgets.QLabel(self.grWarning)
        self.lbWarning.setGeometry(QtCore.QRect(220, 200, 341, 71))
        self.lbWarning.setAlignment(QtCore.Qt.AlignCenter)
        self.lbWarning.setObjectName("lbWarning")
        self.btXemChiTiet = QtWidgets.QPushButton(self.frame)
        self.btXemChiTiet.setGeometry(QtCore.QRect(788, 660, 241, 61))
        self.btXemChiTiet.setObjectName("btXemChiTiet")

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        

    def retranslateUi(self, SV_mainDisplay):

        _translate = QtCore.QCoreApplication.translate
        SV_mainDisplay.setWindowTitle(_translate("SV_mainDisplay", "MainWindow"))
        self.SV_mainDisplay = SV_mainDisplay        
        self.lbTempOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiOutValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTempInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbHumiInValue.setText(_translate("SV_mainDisplay", "0"))
        self.lbTrongKho.setText(_translate("SV_mainDisplay", "0"))
        self.lbChoMuon.setText(_translate("SV_mainDisplay", "0"))
        self.btKhoaDC.setText(_translate("SV_mainDisplay", "Khóa ĐC"))
        self.btKiemTra.setText(_translate("SV_mainDisplay", "Kiểm tra"))
        self.btTroGiup.setText(_translate("SV_mainDisplay", "Trợ giúp"))
        self.btQuanLy.setText(_translate("SV_mainDisplay", "Cài đặt"))
        self.btDongTu.setText(_translate("SV_mainDisplay", "Đóng giá"))
        self.btTraCuu.setText(_translate("SV_mainDisplay", "Tra cứu"))
        self.btMoTu.setText(_translate("SV_mainDisplay", "Mở giá"))
        self.lbKhoangCach.setText(_translate("SV_mainDisplay", "0"))
        self.lbstatusMotor.setText(_translate("SV_mainDisplay", "Đóng"))
        self.lbSoNguoi.setText(_translate("SV_mainDisplay", "0"))
        self.lbWarning.setText(_translate("SV_mainDisplay", "a"))
        self.btXemChiTiet.setText(_translate("SV_mainDisplay", "Xem chi tiết"))

            
import resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SV_mainDisplay = QtWidgets.QMainWindow()
    ui = Ui_SV_mainDisplay()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())

