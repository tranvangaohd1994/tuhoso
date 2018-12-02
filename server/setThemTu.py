# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setThemTu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import  QTimer
from kbNumber import MSG_Dialog
import server
import uart
import threading

class Ui_setThemTu(object):
    def setupUi(self, setThemTu):
        setThemTu.setObjectName("setThemTu")
        setThemTu.resize(1280, 800)
        setThemTu.setStyleSheet("")
        self.frame = QtWidgets.QFrame(setThemTu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}.QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF8F00;font: 75 34pt \"Arial\";}.QLineEdit{background-color:#B2FF59;font: 75 32pt \"Arial\";}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1280, 71))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btThem = QtWidgets.QPushButton(self.frame)
        self.btThem.setGeometry(QtCore.QRect(490, 600, 211, 101))
        self.btThem.setObjectName("btThem")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(20, 600, 171, 101))
        self.btExit.setObjectName("btExit")

        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(250, 600, 171, 101))
        self.btSave.setObjectName("btSave")

        self.grcdControl = QtWidgets.QGroupBox(self.frame)
        self.grcdControl.setGeometry(QtCore.QRect(460, 260, 661, 121))
        self.grcdControl.setStyleSheet("QLabel{color: rgb(255, 255, 255);font: 75 20pt \"Arial\";}.QRadioButton{font: 75 20pt \"Arial\";color: white;background-color: #55007f;}.QRadioButton::indicator{width: 20px;height: 20px;}")
        self.grcdControl.setTitle("")
        self.grcdControl.setObjectName("grcdControl")
        self.rbbenPhai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbbenPhai.setGeometry(QtCore.QRect(430, 10, 191, 100))
        self.rbbenPhai.setObjectName("rbbenPhai")
        self.rbBenTrai = QtWidgets.QRadioButton(self.grcdControl)
        self.rbBenTrai.setGeometry(QtCore.QRect(30, 10, 201, 100))
        self.rbBenTrai.setChecked(True)
        self.rbBenTrai.setObjectName("rbBenTrai")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(20, 340, 341, 191))
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.btXoa = QtWidgets.QPushButton(self.frame)
        self.btXoa.setGeometry(QtCore.QRect(890, 600, 191, 101))
        self.btXoa.setObjectName("btXoa")
        self.lbTrai = QtWidgets.QLabel(self.frame)
        self.lbTrai.setGeometry(QtCore.QRect(560, 410, 101, 61))
        self.lbTrai.setStyleSheet("")
        self.lbTrai.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbTrai.setObjectName("lbTrai")
        self.lbPhai = QtWidgets.QLabel(self.frame)
        self.lbPhai.setGeometry(QtCore.QRect(950, 410, 101, 61))
        self.lbPhai.setStyleSheet("")
        self.lbPhai.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbPhai.setObjectName("lbPhai")

        self.retranslateUi(setThemTu)
        QtCore.QMetaObject.connectSlotsByName(setThemTu)

    def retranslateUi(self, setThemTu):
        _translate = QtCore.QCoreApplication.translate
        setThemTu.setWindowTitle(_translate("setThemTu", "Form"))
        self.label.setText(_translate("setThemTu", "Quản lý hệ thống giá"))
        self.btThem.setText(_translate("setThemTu", "Thêm  1 cột"))
        self.btExit.setText(_translate("setThemTu", "Thoát"))
        self.btSave.setText(_translate("setThemTu", "Lưu"))
        self.rbbenPhai.setText(_translate("setThemTu", "Bên Phải"))
        self.rbBenTrai.setText(_translate("setThemTu", "Bên Trái"))
        self.label_6.setText(_translate("setThemTu", "Số cột hiện tại\nso với tủ Master:"))
        self.btXoa.setText(_translate("setThemTu", "Xóa 1 cột"))
        

        self.setEvent()
        self.btExit.clicked.connect(setThemTu.close)
    
    def setEvent(self):
        self.maxTu = 10
        self.minTu = 0

        self.numLeft = server.numClientLeft
        self.numRight = server.numClientRight
        self.lbTrai.setText(str(self.numLeft))
        self.lbPhai.setText(str(self.numRight))
        self.btThem.clicked.connect(self.btThem_click)
        self.btXoa.clicked.connect(self.btXoa_click)
        self.btSave.clicked.connect(self.btSave_click)
        self.btClickTimer = False

    def btThem_click(self):
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        if self.rbBenTrai.isChecked() :
            if self.numLeft < self.maxTu :
                self.numLeft += 1
                self.lbTrai.setText(str(self.numLeft))
        else :
            if self.numRight < self.maxTu:
                self.numRight += 1
                self.lbPhai.setText(str(self.numRight))
        pass
    def btXoa_click(self):
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        if self.rbBenTrai.isChecked() :
            if self.numLeft > self.minTu:
                self.numLeft -= 1
                self.lbTrai.setText(str(self.numLeft))
        else :
            if self.numRight > self.minTu:
                self.numRight -= 1
                self.lbPhai.setText(str(self.numRight))
        pass
    def btSave_click(self):
        if(self.btClickTimer):
            return
        else:
            self.buttonTimer()

        server.threadLock.acquire()
        if server.numClientLeft < self.numLeft :
            "tang so client ben trai len"
            for i in range(server.numClientLeft + 1, self.numLeft + 1):
                tu = "Left_" + str(i)
                server.arrIPArrdressLeft[tu] = uart.dataAllJsonConfig["IPLeft"][tu]
                server.dataReceivedSer[tu] = uart.DataInforSer()
                server.dataSent2Client[tu] = server.DataSent2Client()
            server.playmp3(server.folderMP3 + "045.mp3")
            print('them tu ben trai')
        elif server.numClientLeft > self.numLeft :
            "giam so client di"
            for i in range(self.numLeft+1, server.numClientLeft + 1):
                tu = "Left_" + str(i)
                server.allConnection[tu].send(b'NG')
                server.allConnection[tu].close()
                del server.allConnection[tu]
                del server.arrIPArrdressLeft[tu]
                del server.dataReceivedSer[tu]
                del server.dataSent2Client[tu]
            server.playmp3(server.folderMP3 + "044.mp3")
            print('xoa tu ben trai')
        if server.numClientRight < self.numRight :
            "tang so client ben phai len"
            for i in range(server.numClientRight + 1, self.numRight + 1):
                tu = "Right_" + str(i)
                server.arrIPArrdressRight[tu] = uart.dataAllJsonConfig["IPRight"][tu]
                server.dataReceivedSer[tu] = uart.DataInforSer()
                server.dataSent2Client[tu] = server.DataSent2Client()
            print('Them tu ben phai')
            server.playmp3(server.folderMP3 + "045.mp3")
        elif server.numClientRight > self.numRight :
            "giam so client ben phai"
            for i in range(self.numRight+1, server.numClientRight + 1):
                tu = "Right_" + str(i)
                server.allConnection[tu].send(b'NG')
                server.allConnection[tu].close()
                del server.allConnection[tu]
                del server.arrIPArrdressLeft[tu]
                del server.dataReceivedSer[tu]
                del server.dataSent2Client[tu]
            print('Xoa tu ben phai')
            server.playmp3(server.folderMP3 + "044.mp3")

        server.numClientLeft = self.numLeft
        uart.dataAllJsonConfig["IPLeft"]["numLeftActive"] = self.numLeft
        server.numClientRight = self.numRight
        uart.dataAllJsonConfig["IPRight"]["numRightActive"]
        uart.saveConfig()
        server.tuOpenedLeft = "0"
        server.tuOpenedRight = '0'
        server.tuActive = '0'
        server.threadLock.release()

        
        dialog = MSG_Dialog()
        dialog.exec_()
    #de chong doi phim bam
    def buttonTimer(self):
        self.btTimer = QTimer(self.frame)
        self.btTimer.timeout.connect(self.stopButtonTimer)
        self.btTimer.start(500)
        self.btClickTimer = True

    def stopButtonTimer(self):
        self.btTimer.stop()
        self.btClickTimer = False
        print("stopButtonTimer - button is actived")
import resources


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setThemTu = QtWidgets.QWidget()
    ui = Ui_setThemTu()
    ui.setupUi(setThemTu)
    setThemTu.show()
    sys.exit(app.exec_())

"""