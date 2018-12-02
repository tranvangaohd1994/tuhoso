# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaoDuongServer.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QSize, QTimer, pyqtSignal,QRect,QDateTime,QDate
import server
import time
import struct
import uart

class Ui_BaoDuongServer(object):
    def setupUi(self, BaoDuongServer):
        BaoDuongServer.setObjectName("BaoDuongServer")
        BaoDuongServer.resize(1280, 800)
        self.BaoDuongServer = BaoDuongServer
        self.frame = QtWidgets.QFrame(BaoDuongServer)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/BaoDuong.jpg);}#lbtitle{color:red ;font: 75  30pt \"Arial\";}.QPushButton:pressed { background-color: #FF6E40}.QPushButton{border-radius: 20px;background-color: #c9ffbc;font: 75 20pt \"Arial\";}QGroupBox {border: 2px solid #FFAB91;border-radius: 10px;}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.lbtitle = QtWidgets.QLabel(self.frame)
        self.lbtitle.setGeometry(QtCore.QRect(320, 130, 661, 61))
        self.lbtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbtitle.setObjectName("lbtitle")
        self.btTiepTuc = QtWidgets.QPushButton(self.frame)
        self.btTiepTuc.setGeometry(QtCore.QRect(930, 610, 161, 111))
        self.btTiepTuc.setObjectName("btTiepTuc")
        self.grRight = QtWidgets.QGroupBox(self.frame)
        self.grRight.setGeometry(QtCore.QRect(450, 210, 391, 391))
        self.grRight.setStyleSheet(".QLabel{color:#FFFF00 ;font: 75  22pt \"Arial\";}")
        self.grRight.setTitle("")
        self.grRight.setObjectName("grRight")
        self.lbCoichip = QtWidgets.QLabel(self.grRight)
        self.lbCoichip.setGeometry(QtCore.QRect(10, 110, 371, 41))
        self.lbCoichip.setObjectName("lbCoichip")
        self.lbCBChayTrong = QtWidgets.QLabel(self.grRight)
        self.lbCBChayTrong.setGeometry(QtCore.QRect(10, 260, 331, 41))
        self.lbCBChayTrong.setObjectName("lbCBChayTrong")
        self.lbCBChayNgoai = QtWidgets.QLabel(self.grRight)
        self.lbCBChayNgoai.setGeometry(QtCore.QRect(10, 320, 331, 41))
        self.lbCBChayNgoai.setObjectName("lbCBChayNgoai")
        self.lbQuatGio = QtWidgets.QLabel(self.grRight)
        self.lbQuatGio.setGeometry(QtCore.QRect(10, 160, 371, 41))
        self.lbQuatGio.setObjectName("lbQuatGio")
        self.lbDenThap = QtWidgets.QLabel(self.grRight)
        self.lbDenThap.setGeometry(QtCore.QRect(10, 210, 371, 41))
        self.lbDenThap.setObjectName("lbDenThap")
        self.lbTempIn = QtWidgets.QLabel(self.grRight)
        self.lbTempIn.setGeometry(QtCore.QRect(10, 10, 341, 41))
        self.lbTempIn.setObjectName("lbTempIn")
        self.lbTempOut = QtWidgets.QLabel(self.grRight)
        self.lbTempOut.setGeometry(QtCore.QRect(10, 60, 341, 41))
        self.lbTempOut.setObjectName("lbTempOut")
        self.btThoat = QtWidgets.QPushButton(self.frame)
        self.btThoat.setGeometry(QtCore.QRect(200, 600, 161, 111))
        self.btThoat.setObjectName("btThoat")


        self.lbValue = QtWidgets.QLabel(self.frame)
        self.lbValue.setGeometry(QtCore.QRect(490, 640, 330, 50))
        self.lbValue.setObjectName("lbValue")
        self.lbValue.setStyleSheet("#lbValue{color:#FFFF00; font : 75 26pt \"Arial\";}")
        self.lbValue.setAlignment(QtCore.Qt.AlignCenter)

        self.retranslateUi(BaoDuongServer)
        QtCore.QMetaObject.connectSlotsByName(BaoDuongServer)

    def retranslateUi(self, BaoDuongServer):
        _translate = QtCore.QCoreApplication.translate
        BaoDuongServer.setWindowTitle(_translate("BaoDuongServer", "Form"))
        self.lbtitle.setText(_translate("BaoDuongServer", "Thông tin bảo dưỡng"))
        self.btTiepTuc.setText(_translate("BaoDuongServer", "Tiếp tục"))
        self.lbCoichip.setText(_translate("BaoDuongServer", "Còi chip"))
        self.lbCBChayTrong.setText(_translate("BaoDuongServer", "Cảm biến cháy trong"))
        self.lbCBChayNgoai.setText(_translate("BaoDuongServer", "Cảm biến cháy ngoài"))
        self.lbQuatGio.setText(_translate("BaoDuongServer", "Quạt thông gió"))
        self.lbDenThap.setText(_translate("BaoDuongServer", "Đèn tháp 3 màu"))
        self.lbTempIn.setText(_translate("BaoDuongServer", "Cảm biến nhiệt độ trong"))
        self.lbTempOut.setText(_translate("BaoDuongServer", "Cảm biến nhiệt độ ngoài"))
        self.btThoat.setText(_translate("BaoDuongServer", "Thoát"))

        self.setEvent()

    def setEvent(self):
        server.statusVanHanh = 41 # da bat form bao duong

        linkFile = server.folderMP3 + "017.mp3"
        server.playmp3(linkFile)
        print("close tu left start")
        #lb tu dong: 1-7
        self.listlb=[]
        self.listlb.append(self.lbTempIn)
        self.listlb.append(self.lbTempOut)
        self.listlb.append(self.lbCoichip)
        self.listlb.append(self.lbQuatGio)
        self.listlb.append(self.lbDenThap)
        self.listlb.append(self.lbCBChayTrong)
        self.listlb.append(self.lbCBChayNgoai)
        self.listSoundServer=["030","031","035","036","037","038","039"]

        self.listSound=["030","031","032","033","034","035","038","039","040","040","040","041","042","043"]
        self.listdata2Ar=[b'\x01',b'\x02',b'\x06',b'\x07',b'\x08',b'\x09',b'\x0a']
        self.caseBD = 0
        server.caseBD = 0
        self.flagFirst = True
        #dong tat ca cac tu truoc khi bao duong
        server.tuTraiPhai = 'A'
        server.dongMoTuFunction(0,1)

        for lb in self.listlb :
            lb.hide()
        self.btThoat.clicked.connect(self.btExit_click)
        self.ctimer = QTimer(self.frame)
        self.ctimer.timeout.connect(self.checkTimer)
        self.ctimer.start(400)
        self.Tu = server.numClientLeft
        self.statusTu = 2 # 2 ben trai 1 ben phai 0 master
        if self.Tu == 0: #ko co tu ben trai
            self.Tu = server.numClientRight
            self.statusTu = 1 # 2 ben trai 1 ben phai 0 master
        

    def checkTimer(self):
        if self.flagFirst :
            if server.serverMain.checkAllTuIsClosed() == False:
                return
            self.flagFirst = False

            for i in range(1,server.numClientLeft+1):
                nameTu = "Left_"+str(i)
                server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd\x00')
            
            self.btTiepTuc.clicked.connect(self.btTiepTuc_click)
            
        
        try :
            #timer này để  check xem các client có bấm tiếp tục hay ko 
            if server.caseBD > self.caseBD :
                self.btTiepTuc_click()
            
            if self.caseBD == 1 or self.caseBD == 2 or (self.caseBD >= 6 and self.Tu == 0 and self.statusTu == 0): #bao duong tren master
                if uart.caseBDIsACK == 0 :
                    self.lbValue.setText("Waiting")
                elif uart.caseBDIsACK == 1 :
                    self.lbValue.setText("ERROR")
                    self.listlb[self.caseBD -1].setStyleSheet("color:#FF0000")
                elif uart.caseBDIsACK == 2 :
                    self.lbValue.setText("PASS")
                    self.listlb[self.caseBD -1].setStyleSheet("color:#00FF00")
            
            #check hoan thanh hay chua neu hoan thanh roi thi bao loa
            if server.checkBDok and self.caseBD >= 5:
                #thong bao kiem tra hoan tat
                linkFile = server.folderMP3 + "049.mp3"
                server.playmp3(linkFile)
                server.checkBDok = False
        except Exception as e:
            print("ERROR in BaoDuong checkTimer", str(e))
            self.btExit_click()

        if server.statusVanHanh == 42 : # ket thuc frm bao duong
            self.btExit_click()
            print("Ket thuc qua trinh bao duong PC sent to client")

    def btTiepTuc_click(self):
        #khi kiem tra xong het 1 tu
        if self.caseBD == 14 and self.Tu > 0:
            self.caseBD = 4
            server.caseBD = 4
            self.Tu -= 1
            if self.Tu == 0:
                if self.statusTu == 2:
                    self.statusTu -= 1
                    self.Tu = server.numClientRight #kiem tra xong tu ben trai chuyen sang tu ben phai
                elif self.statusTu == 1:
                    self.statusTu -= 1 
                    self.caseBD = 2
                    server.caseBD = 2
        
        self.caseBD += 1
        server.caseBD = self.caseBD
        
        if self.Tu == 0 and self.caseBD >= 8 :
            linkFile = server.folderMP3 +"050.mp3"
            server.playmp3(linkFile)
            return
        
        linkFile = server.folderMP3 + self.listSound[self.caseBD-1] +".mp3"
       
        #truong hop kiem tra tự động
        if self.caseBD == 1 or self.caseBD == 2: # 2 case kiem tra tự động cho cac client va sever
            self.listlb[self.caseBD-1].show()
            data = struct.pack('B',self.caseBD)
            for i in range(1,server.numClientLeft+1):
                nameTu = "Left_"+str(i)
                server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)
            for i in range(1,server.numClientRight+1):
                nameTu = "Right_"+str(i)
                server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)
            uart.caseBDIsACK = 0
            uart.sentDataRandom(b'\xbd\xbd',b'\x1f\x00\x00\x00\x00\x00\x00\x00')
            time.sleep(0.5)
            uart.sentDataRandom(b'\xbd\xbd',data + b'\x00\x00\x00\x00\x00\x00\x00')
        
        if self.caseBD == 3 or self.caseBD == 4 and self.Tu > 0:
            data = struct.pack('B',self.caseBD)
            for i in range(1,server.numClientLeft+1):
                nameTu = "Left_"+str(i)
                server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)
            for i in range(1,server.numClientRight+1):
                nameTu = "Right_"+str(i)
                server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)

        if self.caseBD == 5 and self.Tu > 0:
            #sent mo tu ngoai cung
            if self.statusTu == 2 :
                firstNameTu = "Left_"
            else :
                firstNameTu = "Right_"

            nameTu = firstNameTu + str(self.Tu) 
            
            server.tuTraiPhai = nameTu[0]
            server.dongMoTuFunction(3,nameTu)
            numInLoop = 0
            while server.dataReceivedSer[nameTu].statusMotor != 2:
                numInLoop+=1
                time.sleep(0.1)
                if numInLoop > 100 :
                    print("Tu eo biet da duoc mo hay chua time out mo tu")
                    break
                pass
            print(" tu da mo xong")
            server.playmp3(linkFile)
            time.sleep(2)
            data = struct.pack('B',self.caseBD)
            server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)
            return

        if self.caseBD >= 5 and self.Tu > 0:
            data = struct.pack('B',self.caseBD)
            if self.statusTu == 2 :
                firstNameTu = "Left_"
            else :
                firstNameTu = "Right_"
            nameTu = firstNameTu + str(self.Tu) 
            server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd'+data)

        if  self.Tu == 0:
            #check cac test khac co pass hay ko
            if self.caseBD == 2 or self.caseBD == 3 or self.caseBD == 7 and uart.caseBDIsACK ==1 :
                self.listlb[self.caseBD -2].setStyleSheet("color:#FF0000")

            linkFile = server.folderMP3 + self.listSoundServer[self.caseBD-1] +".mp3"
            if self.listSoundServer[self.caseBD-1] == '037' :
                server.playmp3(linkFile)
                time.sleep(2)
            self.listlb[self.caseBD-1].show()
            uart.caseBDIsACK = 0
            uart.sentDataRandom(b'\xbd\xbd',b'\x1f\x00\x00\x00\x00\x00\x00\x00')
            time.sleep(0.5)
            uart.sentDataRandom(b'\xbd\xbd',self.listdata2Ar[self.caseBD-1] + b'\x00\x00\x00\x00\x00\x00\x00')

            

        server.playmp3(linkFile)


    def btExit_click(self):
        self.ctimer.stop()
        #Kết thúc quá trình bảo dưỡng hệ thống.
        linkFile = server.folderMP3 + "050.mp3"
        server.playmp3(linkFile)

        server.caseBD = 0
        for i in range(1,server.numClientLeft+1):
            nameTu = "Left_"+str(i)
            server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd\xff')
        for i in range(1,server.numClientRight+1):
            nameTu = "Right_"+str(i)
            server.serverMain.sendMes2Client(nameTu ,b'\xbd\xbd\xff')

        uart.sentDataRandom(b'\xbd\xbd',b'\x1f\x00\x00\x00\x00\x00\x00\x00')
        time.sleep(0.5)
        uart.sentDataRandom(b'\xbd\xbd',b'\xff\x00\x00\x00\x00\x00\x00\x00')
        uart.caseBDIsACK = 0

        server.statusVanHanh = 0
        self.BaoDuongServer.close()
        

import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    BaoDuongServer = QtWidgets.QWidget()
    ui = Ui_BaoDuongServer()
    ui.setupUi(BaoDuongServer)
    BaoDuongServer.show()
    sys.exit(app.exec_())

"""
