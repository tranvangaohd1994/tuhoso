import threading
import sys
import socket
import logging
import time
import server
import uart

IPSERVER = "192.168.0.100"
PORT = 24595

class ServerPC(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self): 
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.soc.bind((IPSERVER, PORT))
        self.soc.listen(5)
        self.logger = logging.getLogger("ServerThreadMain")
        self.isLeft = True
        print("socket is running")
        #self.logger.debug("socket is running - server bat dau hoat dong")
        while server.isListenCL:
            conn, addr = self.soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            print('Accepting connection from ',ip ,':',port)
            while True:
                try :
                    data = conn.recv(3)
                    dt = conn.recv(2)
                    if len(data) == 3 and data[0] == 0xff:
                        if data[1] == 1 : # chon tu ben trai:
                            nameTu = "Left_"
                            server.tuTraiPhai = 'L'
                        elif data[1] == 2 :
                            nameTu = "Right_"
                            server.tuTraiPhai = 'R'
                        else :
                            print("recive Frame tu server bi sai form", data)
                            continue
                        numberTu = int(data[2])
                        if (numberTu <= server.numClientLeft and data[1] == 1 ) or (numberTu <= server.numClientRight and data[1] == 2) :
                            
                            if numberTu == 0x00: # 00 la tu Master
                                if len(dt)==2 and dt[0] ==0xab and dt[1]== 0xab: #cap nhat thong tin tu
                                    dtSend = b'\xaa\xaa'+ bytearray(uart.dataReceved.myList)+ b'\x00\x00'
                                    conn.send(dtSend)
                            else:
                                nameTu = nameTu + str(numberTu)
                                if len(dt)==2 and dt[0] ==0xAA: #nhom chuc nang co ban dong mo dung khoa dien tu
                                    if dt[1] == 0x01 :
                                        server.dongMoTuFunction(0,0)
                                    elif dt[1] == 0x02 :
                                        if server.isWaiting == 2:
                                            server.dongMoTuFunction(2,nameTu)
                                        elif server.isWaiting == 0 :
                                            server.dongMoTuFunction(1,nameTu)
                                    elif dt[1] == 0x03:
                                        server.serverMain.sentStop2AllClient()
                                    elif dt[1] == 0x04 :
                                        #khoa dien tu khoa dong co
                                        server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc\x00')
                                    elif dt[1] == 0x05 :
                                        server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc\x01')
                                
                                elif len(dt)==2 and dt[0] ==0xab and dt[1]== 0xab:  #cap nhat thong tin tu trai phai
                                    dtSend = b'\xaa\xaa'+ bytearray(server.dataReceivedSer[nameTu].myList)+ b'\x00\x00'
                                    conn.send(dtSend)
                                elif len(dt) == 2 and dt[0] == 0xbb and ( dt[1] == 0x01 or dt[1] == 0x02 or dt[1] == 0x03):#bao an toan
                                    print("Pc bao an toan-nhom chuc nang su co")
                                    pass
                                elif len(dt)==2 and dt[0] ==0xcc : #nhom chuc nang bao duong
                                    if dt[1]== 0x01:  #bat dau qua trinh bao duong
                                        pass
                                    elif dt[1]== 0x02 :# tiep tuc bao duong
                                        pass
                                    elif dt[1]==0x03: #ket thuc qua trinh bao duong
                                        pass
                                elif len(dt)==2 and dt[0] == 0xdd : # nhom chuc nang dieu khien dieu hoa
                                    if dt[1]== 0x30:  #bat dieu hoa
                                        pass
                                    elif dt[1]== 0x31 :# tat dieu hoa
                                        pass
                                    elif dt[1]==0x32: # bat quat gio dieu hoa
                                        pass
                                    elif dt[1]== 0x33 :# tat quat gio dieu hoa
                                        pass
                                    elif dt[1] >= 0x10 and dt[1] <= 0x1f: # bat nhiet do tuong ung tu 16-31 do
                                        pass
                                elif len(dt)==2 and dt[0] == 0xee : # nhom chuc nang phu tro
                                    if dt[1]== 0x30:  #bat den chieu sang
                                        pass
                                    elif dt[1]== 0x31 :# tat den chieu sang
                                        pass
                                    elif dt[1]==0x32: # tham do ket noi master va PC
                                        pass
                                    elif dt[1]== 0x33 :# bat quat thong gio
                                        pass
                                     elif dt[1]== 0x34 :# tat quat thong gio
                                        pass
                                    elif dt[1] >= 0x01 and dt[1] <= 0x0A : # dieu chinh cuong do am thanh ung voi 10 muc do
                                        pass
                                    elif dt[1] >= 0x0B and dt[1] <= 0x0F : # 5 loai giong noi
                                        pass
                                    elif dt[1] >= 0x11 and dt[1] <= 0x1A : # 10 muc dieu chinh do sang man hinh
                                        pass
                                elif len(dt)==2 and dt[0] == 0xff : # nhom chuc nang cai dat
                                    value = dt = conn.recv(1)
                                    if dt[1]== 0x01 :  # khoang cach mo tu
                                        pass
                                    elif dt[1]== 0x02 : # chieu quay mo tu
                                        pass
                                    elif dt[1]==0x03 : # to do dong co
                                        pass
                                    elif dt[1]== 0x04 :# khoang cach giam toc
                                        pass
                                    elif dt[1]== 0x05 :# luc chong ket
                                        pass
                                    elif dt[1]== 0x06 :# tat cam bien
                                        pass                                        
                                
                    if not data:
                        conn.close()
                        print("Client masterPC exit or connection error")
                        break

                except Exception as e:
                    print("Exception masterPC : ",str(e))
                    conn.close()
                    break

ServerPC = ServerPC()
ServerPC.start()