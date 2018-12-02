# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaoDuongClient.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
import client
import time
import struct

class Ui_BaoDuongClient(object):
    def setupUi(self, BaoDuongClient):
        BaoDuongClient.setObjectName("BaoDuongClient")
        BaoDuongClient.resize(1280, 800)
        self.BaoDuongClient = BaoDuongClient
        self.frame = QtWidgets.QFrame(BaoDuongClient)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#lbtitle{color:red ;font: 75  30pt bold \"Ubuntu\";}QPushButton:pressed { background-color: #FF6E40}QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt bold \"Ubuntu\";}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(340, 130, 661, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btTiepTuc = QtWidgets.QPushButton(self.frame)
        self.btTiepTuc.setGeometry(QtCore.QRect(570, 650, 161, 111))
        self.btTiepTuc.setObjectName("btTiepTuc")
        self.grLeft = QtWidgets.QGroupBox(self.frame)
        self.grLeft.setGeometry(QtCore.QRect(120, 220, 361, 441))
        self.grLeft.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Ubuntu\";}")
        self.grLeft.setTitle("")
        self.grLeft.setObjectName("grLeft")
        self.lbTempIn = QtWidgets.QLabel(self.grLeft)
        self.lbTempIn.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.lbTempIn.setObjectName("lbTempIn")
        self.lbTempOut = QtWidgets.QLabel(self.grLeft)
        self.lbTempOut.setGeometry(QtCore.QRect(10, 60, 341, 41))
        self.lbTempOut.setObjectName("lbTempOut")
        self.lbKhoangCach = QtWidgets.QLabel(self.grLeft)
        self.lbKhoangCach.setGeometry(QtCore.QRect(10, 110, 341, 41))
        self.lbKhoangCach.setObjectName("lbKhoangCach")
        self.lbDongCo = QtWidgets.QLabel(self.grLeft)
        self.lbDongCo.setGeometry(QtCore.QRect(10, 160, 341, 41))
        self.lbDongCo.setObjectName("lbDongCo")
        self.lbDen = QtWidgets.QLabel(self.grLeft)
        self.lbDen.setGeometry(QtCore.QRect(10, 210, 211, 41))
        self.lbDen.setObjectName("lbDen")
        self.lbCoi = QtWidgets.QLabel(self.grLeft)
        self.lbCoi.setGeometry(QtCore.QRect(10, 260, 211, 41))
        self.lbCoi.setObjectName("lbCoi")
        self.lbValue = QtWidgets.QLabel(self.grLeft)
        self.lbValue.setGeometry(QtCore.QRect(130, 380, 131, 41))
        self.lbValue.setObjectName("lbValue")
        self.grRight = QtWidgets.QGroupBox(self.frame)
        self.grRight.setGeometry(QtCore.QRect(810, 220, 391, 441))
        self.grRight.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Ubuntu\";}")
        self.grRight.setTitle("")
        self.grRight.setObjectName("grRight")
        self.lbChayTrong = QtWidgets.QLabel(self.grRight)
        self.lbChayTrong.setGeometry(QtCore.QRect(10, 10, 271, 41))
        self.lbChayTrong.setObjectName("lbChayTrong")
        self.lbChayNgoai = QtWidgets.QLabel(self.grRight)
        self.lbChayNgoai.setGeometry(QtCore.QRect(10, 60, 301, 41))
        self.lbChayNgoai.setObjectName("lbChayNgoai")
        self.lbHongNgoai_1 = QtWidgets.QLabel(self.grRight)
        self.lbHongNgoai_1.setGeometry(QtCore.QRect(10, 110, 371, 41))
        self.lbHongNgoai_1.setObjectName("lbHongNgoai_1")
        self.lbTiemCanTrai = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanTrai.setGeometry(QtCore.QRect(10, 260, 331, 41))
        self.lbTiemCanTrai.setObjectName("lbTiemCanTrai")
        self.lbTiemCanPhai = QtWidgets.QLabel(self.grRight)
        self.lbTiemCanPhai.setGeometry(QtCore.QRect(10, 310, 331, 41))
        self.lbTiemCanPhai.setObjectName("lbTiemCanPhai")
        self.lbDemNguoi = QtWidgets.QLabel(self.grRight)
        self.lbDemNguoi.setGeometry(QtCore.QRect(10, 360, 301, 41))
        self.lbDemNguoi.setObjectName("lbDemNguoi")
        self.lbHongNgoai_2 = QtWidgets.QLabel(self.grRight)
        self.lbHongNgoai_2.setGeometry(QtCore.QRect(10, 160, 371, 41))
        self.lbHongNgoai_2.setObjectName("lbHongNgoai_2")
        self.lbHongNgoai_3 = QtWidgets.QLabel(self.grRight)
        self.lbHongNgoai_3.setGeometry(QtCore.QRect(10, 210, 371, 41))
        self.lbHongNgoai_3.setObjectName("lbHongNgoai_3")


        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(140,530,130,50))
        self.lbValue.setObjectName("lbValue")
        self.lbValue.setStyleSheet("#lbValue{color:#FFFF00; font : 75 24pt \"Arial\";}")
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(BaoDuongClient)
        QtCore.QMetaObject.connectSlotsByName(BaoDuongClient)

    def retranslateUi(self, BaoDuongClient):
        _translate = QtCore.QCoreApplication.translate
        BaoDuongClient.setWindowTitle(_translate("BaoDuongClient", "Form"))
        self.lbtitle.setText(_translate("BaoDuongClient", "Thông tin bảo dưỡng"))
        self.btTiepTuc.setText(_translate("BaoDuongClient", "Tiếp tục"))
        self.lbTempIn.setText(_translate("BaoDuongClient", "Cảm biến nhiệt độ trong"))
        self.lbTempOut.setText(_translate("BaoDuongClient", "Cảm biến nhiệt độ ngoài"))
        self.lbKhoangCach.setText(_translate("BaoDuongClient", "Cảm biến khoảng cách"))
        self.lbDongCo.setText(_translate("BaoDuongClient", "Động cơ"))
        self.lbDen.setText(_translate("BaoDuongClient", "Đèn chiếu sáng"))
        self.lbCoi.setText(_translate("BaoDuongClient", "Còi chíp"))
        self.lbChayTrong.setText(_translate("BaoDuongClient", "Cảm biến cháy trong"))
        self.lbChayNgoai.setText(_translate("BaoDuongClient", "Cảm biến cháy ngoài"))
        self.lbHongNgoai_1.setText(_translate("BaoDuongClient", "Cảm biến hồng ngoại dọc 1"))
        self.lbTiemCanTrai.setText(_translate("BaoDuongClient", "Cảm biến tiệm cận trái"))
        self.lbTiemCanPhai.setText(_translate("BaoDuongClient", "Cảm biến tiệm cận phải"))
        self.lbDemNguoi.setText(_translate("BaoDuongClient", "Cảm biến đếm người"))
        self.lbHongNgoai_2.setText(_translate("BaoDuongClient", "Cảm biến hồng ngoại dọc 2"))
        self.lbHongNgoai_3.setText(_translate("BaoDuongClient", "Cảm biến hồng ngoại dọc 3"))

        self.setEvent()

    def setEvent(self):
        
        self.caseBD = 0
        self.listlb = []
        #dong cac tu lai truoc da cai nay se kiem tra sau - mac dinh khi vao che do bao duong phai dong tu
        #lb tu dong: 0-13
        self.listdata2Ar=[b'\x01',b'\x02',b'\x03',b'\x04',b'\x05',b'\x06',b'\x09',b'\x0a',b'\x0b',b'\x0c',b'\x0d',b'\x0e',b'\x0f',b'\x10']
        self.listlb.append(self.lbTempIn)
        self.listlb.append(self.lbTempOut)
        self.listlb.append(self.lbKhoangCach)
        self.listlb.append(self.lbDongCo)

        self.listlb.append(self.lbDen)
        self.listlb.append(self.lbCoi)
        
        self.listlb.append(self.lbChayTrong)
        self.listlb.append(self.lbChayNgoai)

        self.listlb.append(self.lbHongNgoai_1)
        self.listlb.append(self.lbHongNgoai_2)#hn2
        self.listlb.append(self.lbHongNgoai_3)#hn3

        self.listlb.append(self.lbTiemCanTrai)
        self.listlb.append(self.lbTiemCanPhai)
        self.listlb.append(self.lbDemNguoi)

        for lb in self.listlb :
            lb.hide()
        self.btTiepTuc.clicked.connect(self.btTiepTuc_click)

        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkTimer)
        self.ctimer.start(400)

        self.checkBDok = False

    def checkTimer(self):
        try :
            if client.caseBD == 5 and client.dataReceved.statusMotor != 2:
                "cho client mo tu xong moi thuc hien lenh"
                return

            if client.caseBD != self.caseBD :
                #ket thuc qua trinh bao duong
                if client.caseBD == 255:
                    client.sentDataRandom(b'\xbd\xbd',b'\x1f\x00\x00\x00\x00\x00\x00\x00')
                    time.sleep(0.5)
                    client.sentDataRandom(b'\xbd\xbd',b'\xff\x00\x00\x00\x00\x00\x00\x00')
                    client.caseBD = -1
                    self.ctimer.stop()
                    self.BaoDuongClient.close()
                    return
                    
                if client.caseBDIsACK == 0 and self.caseBD > 0 and client.caseBD  != 7 and client.caseBD != 6 :
                    #neu nhan lenh tiep tuc ma chua check xong thi xet la ERROR
                    self.listlb[self.caseBD-1].setStyleSheet("color:#FF0000")

                self.caseBD = client.caseBD
                print("BaoDuong " , client.caseBD)
                client.caseBDIsACK = 0
                self.checkBDok = True

                client.sentDataRandom(b'\xbd\xbd',b'\x1f\x00\x00\x00\x00\x00\x00\x00')
                time.sleep(0.5)
                client.sentDataRandom(b'\xbd\xbd',self.listdata2Ar[self.caseBD-1] + b'\x00\x00\x00\x00\x00\x00\x00')
                self.listlb[self.caseBD-1].show()
                
            if self.caseBD > 0 :
                if client.caseBDIsACK == 2 :
                    self.lbValue.setText("PASS")
                    self.listlb[self.caseBD -1].setStyleSheet("color:#00FF00")
                elif client.caseBDIsACK == 1 :
                    self.listlb[self.caseBD -1].setStyleSheet("color:#FF0000")
                    self.lbValue.setText("ERROR")
                elif client.caseBDIsACK == 0 :
                    self.lbValue.setText("Waiting")
            
            #neu co phan hoi ve thi gui cho server de thong bao loa la da kiem tra xong
            if client.caseBDIsACK != 0 and self.checkBDok :
                client.ThClientMain.sent2Server(b'\xbd\xbc')
                self.checkBDok = False
        
        except Exception as e:
            print("ERROR in BaoDuongCL", str(e))


    def btTiepTuc_click(self):
        client.ThClientMain.sent2Server(b'\xbd\xbd')
        pass 
       
import resources
"""

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaoDuongClient = QtWidgets.QWidget()
    ui = Ui_BaoDuongClient()
    ui.setupUi(BaoDuongClient)
    BaoDuongClient.show()
    sys.exit(app.exec_())

"""
