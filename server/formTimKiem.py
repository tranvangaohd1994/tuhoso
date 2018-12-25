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
        self.frame.setStyleSheet(".QFrame{background-image:url(:/images/TraCuu.png);}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #4e9400;font: bold 18pt \"Arial\";color:#ffffff}.MyQLineEdit{border: 2px solid gray;border-radius: 10px;padding: 0 8px;font: bold 32px \"Arial\";text-align: center;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(460, 545, 161, 85))
        self.btExit.setObjectName("btExit")
        self.tbTimKiem = MyQLineEdit(self.frame)
        self.tbTimKiem.setGeometry(QtCore.QRect(350, 440, 581, 91))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.tbTimKiem.setFont(font)
        self.tbTimKiem.setObjectName("tbTimKiem")
        self.bttcKetQuaLanTruoc = QtWidgets.QPushButton(self.frame)
        self.bttcKetQuaLanTruoc.setGeometry(QtCore.QRect(630, 545, 371, 85))
        self.bttcKetQuaLanTruoc.setObjectName("bttcKetQuaLanTruoc")
        self.btTraCuu = QtWidgets.QPushButton(self.frame)
        self.btTraCuu.setGeometry(QtCore.QRect(290, 545, 161, 85))
        self.btTraCuu.setObjectName("btTraCuu")

        self.retranslateUi(formTimKiem)
        QtCore.QMetaObject.connectSlotsByName(formTimKiem)

    def retranslateUi(self, formTimKiem):
        _translate = QtCore.QCoreApplication.translate
        formTimKiem.setWindowTitle(_translate("formTimKiem", "Form"))
        self.bttcKetQuaLanTruoc.setText(_translate("formTimKiem", "Kết quả tra cứu lần trước"))
        self.btTraCuu.setText(_translate("formTimKiem", "Tra Cứu"))
        self.tbTimKiem.setText(_translate("formTimKiem", ""))
        self.btExit.setText(_translate("formTimKiem", "Thoát"))

        self.setEvent()

    def setEvent(self):
        self.btExit.clicked.connect(self.formTimKiem.close)
        self.btTraCuu.clicked.connect(self.btTraCuu_click)
        self.tbTimKiem.clicked.connect(self.tbTimKiem_click)
        

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