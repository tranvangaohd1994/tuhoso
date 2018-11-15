# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setPassword.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
from keyboard import Ui_Keyboard
import uart
from pyfingerprint.pyfingerprint import PyFingerprint
import time
import threading
import server

class MyQLineEdit(QtWidgets.QLineEdit):
    clicked = pyqtSignal()
    def mousePressEvent(self,event):
        self.clicked.emit()
        QtWidgets.QLineEdit.mousePressEvent(self, event)

class Ui_setPassword(object):
    def setupUi(self, setPassword):
        setPassword.setObjectName("setPassword")
        setPassword.resize(1280, 800)
        setPassword.setStyleSheet("")
        self.setPassword = setPassword
        self.frame = QtWidgets.QFrame(setPassword)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frame.setStyleSheet(".QFrame{background-image: url(:/images/darkbg.jpg);}#QPushButton:pressed { background-color:#FF6E40}.QPushButton{border-radius: 20px;background-color: #FFC107;font: 75 20pt \"Arial\";}.QLabel{color:#FF3D00;font: 75 24pt \"Arial\";}.MyQLineEdit{background-color:#B2FF59;font: 75 26pt \"Arial\";color:#0091EA}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 110, 1301, 61))
        self.label.setStyleSheet("font: 75 32pt \"Arial\";background-color: rgb(0, 0, 0);color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 250, 211, 41))
        self.label_2.setStyleSheet("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(50, 570, 361, 50))
        self.label_3.setStyleSheet("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(120, 400, 221, 50))
        self.label_4.setStyleSheet("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.btSave = QtWidgets.QPushButton(self.frame)
        self.btSave.setGeometry(QtCore.QRect(780, 630, 191, 101))
        self.btSave.setObjectName("btSave")
        self.btExit = QtWidgets.QPushButton(self.frame)
        self.btExit.setGeometry(QtCore.QRect(1060, 630, 191, 101))
        self.btExit.setObjectName("btExit")
        self.tbMkCu = MyQLineEdit(self.frame)
        self.tbMkCu.setGeometry(QtCore.QRect(60, 300, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.tbMkCu.setFont(font)
        self.tbMkCu.setText("")
        self.tbMkCu.setObjectName("tbMkCu")
        self.tbMkMoiVerify = MyQLineEdit(self.frame)
        self.tbMkMoiVerify.setGeometry(QtCore.QRect(60, 630, 361, 51))

        self.tbMkMoiVerify.setFont(font)
        self.tbMkMoiVerify.setText("")
        self.tbMkMoiVerify.setObjectName("tbMkMoiVerify")
        self.tbMkMoi = MyQLineEdit(self.frame)
        self.tbMkMoi.setGeometry(QtCore.QRect(60, 460, 361, 61))
       
        self.tbMkMoi.setFont(font)
        self.tbMkMoi.setText("")
        self.tbMkMoi.setObjectName("tbMkMoi")
        self.btThemVanTay = QtWidgets.QPushButton(self.frame)
        self.btThemVanTay.setGeometry(QtCore.QRect(780, 460, 191, 101))
        self.btThemVanTay.setObjectName("btThemVanTay")
        self.btXoaVanTay = QtWidgets.QPushButton(self.frame)
        self.btXoaVanTay.setGeometry(QtCore.QRect(1060, 460, 191, 101))
        self.btXoaVanTay.setObjectName("btXoaVanTay")
        self.lbThongBao = QtWidgets.QLabel(self.frame)
        self.lbThongBao.setGeometry(QtCore.QRect(760, 180, 501, 231))
        self.lbThongBao.setStyleSheet("")
        self.lbThongBao.setAlignment(QtCore.Qt.AlignCenter)
        self.lbThongBao.setWordWrap(True)
        self.lbThongBao.setObjectName("lbThongBao")

        self.retranslateUi(setPassword)
        QtCore.QMetaObject.connectSlotsByName(setPassword)

    def retranslateUi(self, setPassword):
        _translate = QtCore.QCoreApplication.translate
        setPassword.setWindowTitle(_translate("setPassword", "Form"))
        self.label.setText(_translate("setPassword", "Cài đặt mật khẩu"))
        self.label_2.setText(_translate("setPassword", "Mật khẩu cũ"))
        self.label_3.setText(_translate("setPassword", "Nhập lại mật khẩu mới"))
        self.label_4.setText(_translate("setPassword", "Mật khẩu mới"))
        self.btSave.setText(_translate("setPassword", "Lưu"))
        self.btExit.setText(_translate("setPassword", "Thoát"))
        self.btThemVanTay.setText(_translate("setPassword", "Thêm vân tay"))
        self.btXoaVanTay.setText(_translate("setPassword", "Xóa vân tay"))
        self.lbThongBao.setText(_translate("setPassword", "Thong bao"))

        self.setEvent()

    def setEvent(self):
        self.tbMkCu.clicked.connect(self.tbMkCu_click)
        self.tbMkMoiVerify.clicked.connect(self.tbMkMoiVerify_click)
        self.tbMkMoi.clicked.connect(self.tbMkMoi_click)

        self.btExit.clicked.connect(self.btExit_click)
        self.btSave.clicked.connect(self.btSave_click)
        self.btThemVanTay.clicked.connect(self.btThemVanTay_click)
        self.btXoaVanTay.clicked.connect(self.btXoaVanTay_click)

        self.USB = server.usbFinger
        self.threadIsRun = False
  
    def btExit_click(self):
        self.setPassword.close()
        pass
    def btSave_click(self):
        if self.tbMkCu.text() != uart.dtMK:
            self.lbThongBao.setText("Mật khẩu hiện tại không đúng!")
            return
        elif self.tbMkMoi.text() != self.tbMkMoiVerify.text():
            self.lbThongBao.setText("Không khớp mật khẩu!")
            return
        else:
            uart.dtMK = self.tbMkMoi.text()
            uart.saveConfig()
            self.lbThongBao.setText("Lưu mật khẩu thành công!")


        pass
    def btThemVanTay_click(self):
        if self.threadIsRun == True : 
            return
        self.threadIsRun = True
        t1 = threading.Thread(target=self.threadAddFinger)
        t1.start()
        pass
    def threadAddFinger(self):
        ## Enrolls new finger
        ## Tries to initialize the sensor
        try:
            f = PyFingerprint(self.USB, 57600, 0xFFFFFFFF, 0x00000000)

            if ( f.verifyPassword() == False ):
                raise ValueError('The given fingerprint sensor password is wrong!')

        except Exception as e:
            self.lbThongBao.setText("Lỗi kết nối với cảm biên vân tay")
            self.threadIsRun = False
            return
        ## Tries to enroll new finger
        try:
            self.lbThongBao.setText("Đặt ngón tay vào cảm biến vân tay")
            ## Wait that finger is read
            while ( f.readImage() == False ):
                pass
            ## Converts read image to characteristics and stores it in charbuffer 1
            f.convertImage(0x01)
            ## Checks if finger is already enrolled
            result = f.searchTemplate()
            positionNumber = result[0]
            if ( positionNumber >= 0 ):
                self.lbThongBao.setText("Vân tay đã tồn tại")
                self.threadIsRun = False
                return

            self.lbThongBao.setText("Nhấc tay ra khỏi cảm biến")
            time.sleep(2)

            self.lbThongBao.setText("Đặt lại ngón tay lần 2 để xác thực")

            ## Wait that finger is read again
            while ( f.readImage() == False ):
                pass

            ## Converts read image to characteristics and stores it in charbuffer 2
            f.convertImage(0x02)

            ## Compares the charbuffers
            if ( f.compareCharacteristics() == 0 ):
                self.lbThongBao.setText("Ngón tay 2 lần không khớp nhau! Lấy Vân tay thât bại")
                self.threadIsRun = False
                return
            ## Creates a template
            f.createTemplate()
            ## Saves template at new position number
            positionNumber = f.storeTemplate()
            self.lbThongBao.setText("Thêm văn tay thành công!")
            self.threadIsRun = False

        except Exception as e:
            print('Operation failed!')
            print('Exception message: ' + str(e))
            self.lbThongBao.setText("Lỗi trong qúa trình thêm vân tay")
            self.threadIsRun = False
            return


    def btXoaVanTay_click(self):
        dialogKey = Ui_Keyboard()
        value = dialogKey.exec_()
        if (value == uart.dtMK or value == uart.dtMKHard):
            ## Tries to initialize the sensor
            try:
                f = PyFingerprint(self.USB, 57600, 0xFFFFFFFF, 0x00000000)
                if ( f.verifyPassword() == False ):
                    raise ValueError('The given fingerprint sensor password is wrong!')

            except Exception as e:
                self.lbThongBao.setText("Lỗi kết nối cảm biến vân tay!")
                return

            ## Gets some sensor information
            #print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))
            ## Tries to delete the template of the finger
            numVantay = int(f.getTemplateCount())
            while numVantay > 0:
                try:
                    if ( f.deleteTemplate(numVantay-1) == True ):
                        print('Template deleted!', numVantay)

                except Exception as e:
                    self.lbThongBao.setText("Xóa vân tay có lỗi!")
                    return
                numVantay -= 1
            self.lbThongBao.setText("Xóa hết vân tay thành công!")

    def tbMkCu_click(self):
        dialogKey = Ui_Keyboard()
        value = dialogKey.exec_()
        self.tbMkCu.setText(value)

    def tbMkMoi_click(self):
        dialogKey = Ui_Keyboard()
        value = dialogKey.exec_()
        self.tbMkMoi.setText(value)
    def tbMkMoiVerify_click(self):
        dialogKey = Ui_Keyboard()
        value = dialogKey.exec_()
        self.tbMkMoiVerify.setText(value)


import resources

"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    setPassword = QtWidgets.QWidget()
    ui = Ui_setPassword()
    ui.setupUi(setPassword)
    setPassword.show()
    sys.exit(app.exec_())

"""