import threading
import sys
import socket
import logging
import time
import serial
import server
import uart
import struct
from subprocess import call

IPSERVER = "192.168.0.100"
PORT = 24595

class ServerPC(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True

    self.inforConfig={'KhoangCach':3,'LucCK':4,'KCGiamToc':7,'ChieuQuayDC':1,'TocDoDC':6}
  
  def run(self): 
    self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.soc.bind((IPSERVER, PORT))
    self.soc.listen(5)
    self.logger = logging.getLogger("ServerThreadMain")
    self.isLeft = True
    self.conn = None
    self.csdl = []
    self.isConnectPC = False

    print("socket is running")
    #self.logger.debug("socket is running - server bat dau hoat dong")
    while server.isListenCL:
      self.isConnectPC = False

      self.conn, addr = self.soc.accept()
      ip, port = str(addr[0]), str(addr[1])
      print('Accepting connection from ',ip ,':',port)
      self.isConnectPC = True
      while server.isListenCL:
        try :
          data = self.conn.recv(3)
          dt = self.conn.recv(2)
          print('pc:',data,dt)
          if len(data) == 3 and len(dt) == 2 and data[0] == 0xff:
            traiOrPhai = '0'
            if data[1] == 1 : # chon tu ben trai:
              nameTu = "Left_"
              traiOrPhai = 'L'
            elif data[1] == 2 :
              nameTu = "Right_"
              traiOrPhai = 'R'
            elif data[1] == 0xff :
              nameTu = 'All_'
              traiOrPhai = 'A'
            else:
                print("recive Frame tu server bi sai form", data , dt)  
                continue
            numberTu = int(data[2]) # neu numberTu = 255 tat ca cac tu
            nameTu = nameTu + str(numberTu) #Left_2 Right_3
            if dt[0] == 0xAA: #nhom chuc nang co ban dong, mo, dung, khoa dien tu
              if dt[1] == 0x01 :
                server.tuTraiPhai = traiOrPhai
                server.dongMoTuFunction(0,0)
              elif dt[1] == 0x02 and numberTu < 255 and numberTu > 0  and traiOrPhai != 'A': #mo tu nao do
                if server.isWaiting == 2:
                    server.dongMoTuFunction(2,nameTu)
                elif server.isWaiting == 0 :
                    server.dongMoTuFunction(1,nameTu)
              elif dt[1] == 0x03: # dung khan cap deo can quan tam nhung thang kia la cai me gi
                  server.serverMain.sentStop2AllClient()
              elif dt[1] == 0x04 : #khoa dien tu khoa dong co
                self.khoaDC(nameTu,numberTu,b'\x00')  
              elif dt[1] == 0x05 :
                self.khoaDC(nameTu,numberTu,b'\x01') 
            
            elif dt[0] == 0xbb and ( dt[1] == 0x01 or dt[1] == 0x02 or dt[1] == 0x03):#bao an toan
              print("Pc bao an toan-nhom chuc nang su co")
            
            elif dt[0] == 0xcc : #nhom chuc nang bao duong
              print('pc gui lenh bao duong he thong')
              if dt[1]== 0x01:  #bat dau qua trinh bao duong
                  server.statusVanHanh = 40
              elif dt[1]== 0x02 :# tiep tuc bao duong
                  server.caseBD += 1
              elif dt[1]==0x03: #ket thuc qua trinh bao duong
                  server.statusVanHanh = 42

            elif dt[0] == 0xdd : # nhom chuc nang dieu khien dieu hoa
              value = self.conn.recv(1)[0]
              server.statusVanHanh = value #0x30-0x35 0x10 - 0x1f
              print('PC van Hanh dieu hoa ' , server.statusVanHanh )

            elif dt[0] == 0xee : # nhom chuc nang phu tro
              if dt[1]== 0x30:  #bat den chieu sang
                  self.batTatDen(nameTu,numberTu,b'\xdd')
              elif dt[1]== 0x31 :# tat den chieu sang
                  self.batTatDen(nameTu,numberTu,b'\xdf')

              elif dt[1] == 0x32: # gui lai thong tin so tu tren moi day
                print("sent to PC numTu ")
                header = b'\xff\x01\x01\xee\x32\x32'
                trai = struct.pack('B',server.numClientLeft)
                phai = struct.pack('B',server.numClientRight)
                header =header + trai + phai
                self.conn.send(header)
                
              elif dt[1] == 0x33 and server.executeThongGio == 0:# bat quat thong gio neu thong gio chua thuc thi
                server.serverMain.thongGioFuction()
              elif dt[1] == 0x34 and server.executeThongGio == 1:# tat quat thong gio neu thong gio dang thuc thi
                server.serverMain.thongGioFuction()
              elif dt[1] == 0x35 : #cai dat thoi gian tu Pc
                ddate = self.conn.recv(6)
                self.configTime(ddate)
                self.conn.send(data + dt + ddate + b'\x32')# phan hoi lai PC cai dat thanh cong

              elif dt[1] >= 0x01 and dt[1] <= 0x0A : # dieu chinh cuong do am thanh ung voi 10 muc do
                  pass
              elif dt[1] >= 0x0B and dt[1] <= 0x0F : # 5 loai giong noi
                  pass
              elif dt[1] >= 0x11 and dt[1] <= 0x1A : # 10 muc dieu chinh do sang man hinh
                  pass

            elif dt[0] == 0xff : # nhom chuc nang cai dat
              value = self.conn.recv(1)[0]
              if dt[1]== 0x01 :  # khoang cach mo tu
                self.saveConfig(nameTu, 255,'KhoangCach', value)
              elif dt[1]== 0x02 : # chieu quay mo tu
                self.saveConfig(nameTu,255,'ChieuQuayDC',value)
              elif dt[1]==0x03 : # toc do dong co
                self.saveConfig(nameTu,numberTu,'TocDoDC',value)
              elif dt[1]== 0x04 :# khoang cach giam toc
                self.saveConfig(nameTu, 255, 'KCGiamToc', value)
              elif dt[1]== 0x05 :# luc chong ket
                self.saveConfig(nameTu,numberTu,'LucCK', value)
              elif dt[1]== 0x06 :# tat cam bien
                  pass                                        
            
            elif dt[0] == 0xab and dt[1] == 0xab: #update thong tin len PC
              self.sendPCInfor(nameTu,numberTu)
                  
          elif len(data) == 3 and data[0] == 0x23 and data[1] == 0x23 and data[2] == 0x23: #truyen nhan du lieu tra cuu thong tin tu
            #dt 2byte luc nay la ID master hien tai chua can dung toi
            header = self.conn.recv(7) # theo header la doc 7 byte tiep theo
            if len(header) == 7 : # neu nhan du 7 byte 
              maLenh = int(header[0])
              lengthAfter = int(header[4]<<24) + int(header[3]<<16) + int(header[2]<<8) + int(header[1])
              print('maLenh=',maLenh , '   lengthAfter=',lengthAfter)
              #doc du so byte gui toi
              self.csdl = []
              dtByte = b''
              while (len(dtByte) < lengthAfter):
                dtByte += self.conn.recv(1024)
              dataString = dtByte.decode('utf-8') #decode('ISO-8859-1')
              kq = dataString.split('$$$')
              for dt in kq :
                online = dt.split('&&&')
                if(len(online) == 8):
                  self.csdl.append(online)
              print('phan tich xong data nhan duoc')
          
          elif not data or not dt:
              print('data', data , '   dt=',dt)
              self.conn.close()
              print("Client masterPC exit or connection error")
              break

        except Exception as e:
            print("Exception masterPC : ",str(e))
            self.conn.close()
            break
  #done
  def standDataForPC(self,nameTu):
    
    server.dataReceivedSer[nameTu].setdataPC()
    server.dataReceivedSer[nameTu].dtForPC[4] = uart.dataReceved.myList[4]
    server.dataReceivedSer[nameTu].dtForPC[5] = uart.dataReceved.myList[5]
    server.dataReceivedSer[nameTu].dtForPC[6] = uart.dataReceved.myList[6]
    server.dataReceivedSer[nameTu].dtForPC[7] = uart.dataReceved.myList[7]
    indexTu = int(nameTu.split('_')[1])
    firstName = nameTu.split('_')[0]
    if indexTu > 1:
      tuTruoc = firstName+'_'+str(indexTu-1)
      kc = server.dataReceivedSer[nameTu].distanceSen_1 - server.dataReceivedSer[tuTruoc].distanceSen_1
      if kc < 0 : 
        kc = 0
      byteKC = struct.pack('B',kc)
      server.dataReceivedSer[nameTu].dtForPC[20] = byteKC[0]

  def sendPCInfor(self,nameTu,numberTu):
    if numberTu == 0: # get data off master
      dtSend = b'\xaa\xaa'+ bytearray(uart.dataReceved.myList)+ b'\x00\x00'
      self.conn.send(dtSend)
      return

    if nameTu[0] == 'A' : #lay thon tin tat ca cac tu
      for tu in server.allConnection:
        self.standDataForPC(tu)
        dtSend = b'\xaa\xaa'+ bytearray(server.dataReceivedSer[tu].dtForPC)+ b'\x00\x00'
        self.conn.send(dtSend)
    else :
      firstName, maxTu = self.checkTuTraiPhai(nameTu)
      if numberTu == 255 : #tat ca cac tu
        for i in range(1,maxTu+1):
          nameTu = firstName + str(i)
          self.standDataForPC(nameTu)
          dtSend = b'\xaa\xaa'+ bytearray(server.dataReceivedSer[nameTu].dtForPC)+ b'\x00\x00'
          self.conn.send(dtSend)
      elif numberTu < maxTu  and numberTu > 0:
        self.standDataForPC(nameTu)
        dtSend = b'\xaa\xaa'+ bytearray(server.dataReceivedSer[nameTu].dtForPC)+ b'\x00\x00'
        self.conn.send(dtSend)

  def configTime(self,ddate):
    print('pc update time : ', ddate)
    _date = "sudo hwclock --set --date "
    _date += '\"20'+  str(int(ddate[5])) + '-' + str(int(ddate[4])) + '-' + str(int(ddate[3])) + ' '
    _date += str(int(ddate[0])) + ':' + str(int(ddate[1])) + ':' + str(int(ddate[2]))+ '+0700\"'
    print('write to system : ',_date)
    call(_date ,shell=True)
    call('sudo hwclock -r',shell=True)
    call('sudo hwclock -s',shell=True)
    server.serverMain.sendDate2Client()

    pass
  
  def batTatDen(self,nameTu,numberTu,dataSent):
    if nameTu[0] == 'A' : #tat ca cac tu
      for tu in server.allConnection:
        server.serverMain.sendMes2Client(tu , b'\xdd'+dataSent)
    else :
      firstName, maxTu = self.checkTuTraiPhai(nameTu)
      if numberTu == 255 : #tat ca cac  tu
        for i in range(1,maxTu+1):
          nameTu = firstName + str(i)
          server.serverMain.sendMes2Client(nameTu , b'\xdd'+dataSent)
      elif numberTu < maxTu and numberTu > 0:
          server.serverMain.sendMes2Client(nameTu , b'\xdd'+dataSent)
  
  def saveConfig(self,firstNameTu,numberTu, itemSent, dataSent):
    if firstNameTu[0] == 'A':
      for tu in server.allConnection:
        server.dataSent2Client[tu].dt2Pi2Ar[self.inforConfig[itemSent]] = int(dataSent)
        server.serverMain.sendMes2Client(tu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
    else:
      firstName, maxTu = self.checkTuTraiPhai(firstNameTu)
      if numberTu == 255 :
        for i in range(1,maxTu+1):
          nameTu = firstName + str(i)
          server.dataSent2Client[nameTu].dt2Pi2Ar[self.inforConfig[itemSent]] = int(dataSent)
          server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))
      elif numberTu <= maxTu and numberTu > 0:
        nameTu = firstName + str(numberTu)
        server.dataSent2Client[nameTu].dt2Pi2Ar[self.inforConfig[itemSent]] = int(dataSent)
        server.serverMain.sendMes2Client(nameTu , b'\xee\xee'+bytes(server.dataSent2Client[nameTu].dt2Pi2Ar))

  def khoaDC(self,nameTu,numberTu,data):
    if nameTu[0] == 'A' : #tat ca cac tu
      for tu in server.allConnection:
        server.serverMain.sendMes2Client(tu , b'\xdc\xdc'+data)
    else:
      firstName, maxTu = self.checkTuTraiPhai(nameTu)
      if numberTu == 255 : #tat ca cac  tu
        for i in range(1,maxTu+1):
          nameTu = firstName + str(i)
          server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc'+data)
      elif numberTu < maxTu and numberTu > 0:
          server.serverMain.sendMes2Client(nameTu , b'\xdc\xdc'+data)

  def checkTuTraiPhai(self,nameTu):
    if nameTu[0] == 'L':
      firstNameTu = 'Left_'
      maxTu = server.numClientLeft
    else :
      firstNameTu = 'Right_'
      maxTu = server.numClientRight
    return firstNameTu, maxTu

ServerPC = ServerPC()
ServerPC.start()