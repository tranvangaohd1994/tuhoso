# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fKetQuaTraCuu.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import server

import masterPC
class Ui_fKetQuaTraCuu(object):
    def setupUi(self, fKetQuaTraCuu):
        fKetQuaTraCuu.setObjectName("fKetQuaTraCuu")
        fKetQuaTraCuu.resize(1280, 800)
        fKetQuaTraCuu.setStyleSheet("")
        self.fKetQuaTraCuu = fKetQuaTraCuu

        self.frame = QtWidgets.QFrame(fKetQuaTraCuu)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}.QTextEdit{background-color:#E6DFEC;font: 75 32pt \"Arial\"; color: #ff0000}.QPushButton:pressed { background-color: #4164ff}.QPushButton{border-radius: 18px;background-color: #FFC107;font: 75 18pt  \"Arial\";}.QLabel{color:#FF8F00;font: 75 24pt \"Arial\";}.QLineEdit{background-color:#E6DFEC;font: 75 32pt \"Arial\"; color: #ff0000}.QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 110, 1281, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 0, 0);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btMo = QtWidgets.QPushButton(self.frame)
        self.btMo.setGeometry(QtCore.QRect(30, 200, 261, 61))
        self.btMo.setObjectName("btMo")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(100, 700, 131, 71))
        self.btExit.setObjectName("btExit")
        self.btTrangDau = QtWidgets.QPushButton(self.frame)
        self.btTrangDau.setGeometry(QtCore.QRect(30, 300, 261, 61))
        self.btTrangDau.setObjectName("btTrangDau")
        self.btTrangTruoc = QtWidgets.QPushButton(self.frame)
        self.btTrangTruoc.setGeometry(QtCore.QRect(30, 400, 261, 61))
        self.btTrangTruoc.setObjectName("btTrangTruoc")
        self.btTrangTiepTheo = QtWidgets.QPushButton(self.frame)
        self.btTrangTiepTheo.setGeometry(QtCore.QRect(30, 500, 261, 61))
        self.btTrangTiepTheo.setObjectName("btTrangTiepTheo")
        self.btTrangCuoi = QtWidgets.QPushButton(self.frame)
        self.btTrangCuoi.setGeometry(QtCore.QRect(30, 600, 261, 61))
        self.btTrangCuoi.setObjectName("btTrangCuoi")
        self.grRight = QtWidgets.QGroupBox(self.frame)
        self.grRight.setGeometry(QtCore.QRect(500, 190, 771, 231))
        self.grRight.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Arial\";}")
        self.grRight.setTitle("")
        self.grRight.setObjectName("grRight")
        self.lbTiemCanPhai = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai.setGeometry(QtCore.QRect(20, 65, 111, 41))
        self.lbTiemCanPhai.setObjectName("lbTiemCanPhai")
        self.lbTiemCanPhai_2 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_2.setGeometry(QtCore.QRect(20, 120, 111, 41))
        self.lbTiemCanPhai_2.setObjectName("lbTiemCanPhai_2")
        self.lbTiemCanPhai_3 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_3.setGeometry(QtCore.QRect(500, 65, 111, 41))
        self.lbTiemCanPhai_3.setObjectName("lbTiemCanPhai_3")
        self.lbTiemCanPhai_4 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_4.setGeometry(QtCore.QRect(500, 120, 111, 41))
        self.lbTiemCanPhai_4.setObjectName("lbTiemCanPhai_4")
        self.leDay = QtWidgets.QLineEdit(self.grRight)
        self.leDay.setGeometry(QtCore.QRect(160, 65, 113, 41))
        self.leDay.setText("")
        self.leDay.setObjectName("leDay")
        self.leGia = QtWidgets.QLineEdit(self.grRight)
        self.leGia.setGeometry(QtCore.QRect(160, 120, 113, 41))
        self.leGia.setText("")
        self.leGia.setObjectName("leGia")
        self.leKhoang = QtWidgets.QLineEdit(self.grRight)
        self.leKhoang.setGeometry(QtCore.QRect(620, 65, 113, 41))
        self.leKhoang.setText("")
        self.leKhoang.setObjectName("leKhoang")
        self.leTang = QtWidgets.QLineEdit(self.grRight)
        self.leTang.setGeometry(QtCore.QRect(620, 120, 113, 41))
        self.leTang.setText("")
        self.leTang.setObjectName("leTang")
        self.lbTiemCanPhai_7 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_7.setGeometry(QtCore.QRect(20, 10, 111, 41))
        self.lbTiemCanPhai_7.setObjectName("lbTiemCanPhai_7")
        self.leTong = QtWidgets.QLineEdit(self.grRight)
        self.leTong.setGeometry(QtCore.QRect(160, 10, 113, 41))
        self.leTong.setText("")
        self.leTong.setObjectName("leTong")
        self.lbTiemCanPhai_8 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_8.setGeometry(QtCore.QRect(500, 10, 91, 41))
        self.lbTiemCanPhai_8.setObjectName("lbTiemCanPhai_8")
        self.leThuTuNow = QtWidgets.QLineEdit(self.grRight)
        self.leThuTuNow.setGeometry(QtCore.QRect(620, 10, 113, 41))
        self.leThuTuNow.setText("")
        self.leThuTuNow.setObjectName("leThuTuNow")
        self.lbTiemCanPhai_9 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_9.setGeometry(QtCore.QRect(20, 175, 111, 41))
        self.lbTiemCanPhai_9.setObjectName("lbTiemCanPhai_9")
        self.leHop = QtWidgets.QLineEdit(self.grRight)
        self.leHop.setGeometry(QtCore.QRect(160, 175, 113, 41))
        self.leHop.setText("")
        self.leHop.setObjectName("leHop")
        self.lbTiemCanPhai_10 = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai_10.setGeometry(QtCore.QRect(510, 175, 81, 41))
        self.lbTiemCanPhai_10.setObjectName("lbTiemCanPhai_10")
        self.leBen = QtWidgets.QLineEdit(self.grRight)
        self.leBen.setGeometry(QtCore.QRect(620, 175, 113, 41))
        self.leBen.setText("")
        self.leBen.setObjectName("leBen")
        self.grRight_3 = QtWidgets.QGroupBox(self.frame)
        self.grRight_3.setGeometry(QtCore.QRect(500, 420, 771, 371))
        self.grRight_3.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Arial\";}")
        self.grRight_3.setTitle("")
        self.grRight_3.setObjectName("grRight_3")
        self.lbTiemCanPhai_6 = QtWidgets.QLabel(self.grRight_3)
        self.lbTiemCanPhai_6.setGeometry(QtCore.QRect(580, 20, 141, 41))
        self.lbTiemCanPhai_6.setObjectName("lbTiemCanPhai_6")
        self.leTen = QtWidgets.QTextEdit(self.grRight_3)
        self.leTen.setGeometry(QtCore.QRect(0, 90, 771, 281))
        self.leTen.setText("")
        self.leTen.setObjectName("leTen")
        self.leSeri = QtWidgets.QLineEdit(self.grRight_3)
        self.leSeri.setGeometry(QtCore.QRect(150, 10, 171, 51))
        self.leSeri.setText("")
        self.leSeri.setObjectName("leSeri")
        self.lbTiemCanPhai_5 = QtWidgets.QLabel(self.grRight_3)
        self.lbTiemCanPhai_5.setGeometry(QtCore.QRect(28, 20, 121, 41))
        self.lbTiemCanPhai_5.setObjectName("lbTiemCanPhai_5")

        self.retranslateUi(fKetQuaTraCuu)
        QtCore.QMetaObject.connectSlotsByName(fKetQuaTraCuu)

    def retranslateUi(self, fKetQuaTraCuu):
        _translate = QtCore.QCoreApplication.translate
        fKetQuaTraCuu.setWindowTitle(_translate("fKetQuaTraCuu", "Form"))
        self.label.setText(_translate("fKetQuaTraCuu", "Kết quả tra Cứu"))
        self.btMo.setText(_translate("fKetQuaTraCuu", "Mở"))
        self.btExit.setText(_translate("fKetQuaTraCuu", "Thoát"))
        self.btTrangDau.setText(_translate("fKetQuaTraCuu", "Trang đầu"))
        self.btTrangTruoc.setText(_translate("fKetQuaTraCuu", "Trang trước"))
        self.btTrangTiepTheo.setText(_translate("fKetQuaTraCuu", "Trang tiếp theo"))
        self.btTrangCuoi.setText(_translate("fKetQuaTraCuu", "Trang cuối"))
        self.lbTiemCanPhai.setText(_translate("fKetQuaTraCuu", "Dãy"))
        self.lbTiemCanPhai_2.setText(_translate("fKetQuaTraCuu", "Giá"))
        self.lbTiemCanPhai_3.setText(_translate("fKetQuaTraCuu", "Khoang :"))
        self.lbTiemCanPhai_4.setText(_translate("fKetQuaTraCuu", "Tầng : "))
        self.lbTiemCanPhai_7.setText(_translate("fKetQuaTraCuu", "Kết quả"))
        self.lbTiemCanPhai_8.setText(_translate("fKetQuaTraCuu", "Chỉ số"))
        self.lbTiemCanPhai_9.setText(_translate("fKetQuaTraCuu", "Hộp"))
        self.lbTiemCanPhai_10.setText(_translate("fKetQuaTraCuu", "Bên"))
        self.lbTiemCanPhai_6.setText(_translate("fKetQuaTraCuu", "Tên hồ sơ "))
        self.lbTiemCanPhai_5.setText(_translate("fKetQuaTraCuu", "Hồ sơ số:"))

        self.setEvent()
        

    def setEvent(self):
        if masterPC.ServerPC.isConnectPC == False :
            self.label.setText('Chưa kết nối đến PC')

        self.btExit.clicked.connect(self.fKetQuaTraCuu.close)
        self.btTrangTiepTheo.clicked.connect(self.btTrangTiepTheo_clicked)
        self.btTrangCuoi.clicked.connect(self.btTrangCuoi_clicked)
        self.btTrangDau.clicked.connect(self.btTrangDau_clicked)
        self.btTrangTruoc.clicked.connect(self.btTrangTruoc_clicked)
        self.btMo.clicked.connect(self.btMo_clicked)
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkDataLoad)
        self.ctimer.start(500)
        self.leTong.setText('0')
        self.indexNow = 0

    def btMo_clicked(self):
        if len(self.data) > 0:
            if self.data[self.indexNow][5] == '1':
                firstName = 'Left_'
            else :
                firstName = 'Right_'
            numTu = int(self.data[self.indexNow][4])
            if ( firstName[0] == 'L' and numTu <= server.numClientLeft ) or (firstName[0]=='R' and numTu <= server.numClientRight):
                nameTu = firstName + str(numTu)
                if server.isWaiting == 2:
                    server.dongMoTuFunction(2,nameTu)
                elif server.isWaiting == 0 :
                    server.dongMoTuFunction(1,nameTu)
            else:
                self.label.setText('Giá không tồn tại')
    def checkDataLoad(self):
        self.data = masterPC.ServerPC.csdl
        if len(self.data) > 0 :
            self.ctimer.stop()
            self.setData()
            self.leTong.setText(str(len(self.data)))

    def setData(self):
        if self.indexNow == len(self.data):
            self.indexNow = 0
        elif self.indexNow < 0 :
            self.indexNow = len(self.data) - 1
        if self.indexNow >= 0 and self.indexNow < len(self.data):
            index = self.indexNow
            self.leDay.setText(str(self.data[index][3]))
            self.leGia.setText(str(self.data[index][4]))
            self.leKhoang.setText(str(self.data[index][6]))
            self.leTang.setText(str(self.data[index][7]))
            self.leHop.setText(str(self.data[index][0]))
            self.leSeri.setText(str(self.data[index][1]))
            self.leTen.setText(str(self.data[index][2]))
            self.leThuTuNow.setText(str(index + 1))

            if self.data[index][5] == '1' :
                self.leBen.setText('Trái')
            else :
                self.leBen.setText('Phải')
        
    def btTrangCuoi_clicked(self):
        self.indexNow = len(self.data) - 1
        self.setData()
    def btTrangDau_clicked(self):
        self.indexNow = 0
        self.setData()
    def btTrangTiepTheo_clicked(self):
        self.indexNow += 1
        self.setData()
    def btTrangTruoc_clicked(self):
        self.indexNow -= 1 
        self.setData()
        
import resources


'''

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fKetQuaTraCuu = QtWidgets.QWidget()
    ui = Ui_fKetQuaTraCuu()
    ui.setupUi(fKetQuaTraCuu)
    fKetQuaTraCuu.show()
    sys.exit(app.exec_())

'''