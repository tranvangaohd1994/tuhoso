import threading
import sys
import socket
import logging
import time
import struct


IPSERVER = "192.168.0.102"
PORT = 24595

class ServerPC(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.daemon = True

    self.inforConfig={'KhoangCach':3,'LucCK':4,'KCGiamToc':7,'ChieuQuayDC':1,'TocDoDC':6}
  def run(self): 
    global isListenCL
    self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.soc.bind((IPSERVER, PORT))
    self.soc.listen(5)
    self.logger = logging.getLogger("ServerThreadMain")
    self.isLeft = True
    self.conn = None
    self.csdl = ''
    
    print("socket is running")
    #self.logger.debug("socket is running - server bat dau hoat dong")
    while isListenCL:
      self.conn, addr = self.soc.accept()
      ip, port = str(addr[0]), str(addr[1])
      print('Accepting connection from ',ip ,':',port)
      while isListenCL:
        try :
          data = self.conn.recv(3)
          dt = self.conn.recv(2)
          print(dt)
          if len(data) == 3 and data[0] == 0xff:
            if data[1] == 1 : # chon tu ben trai:
                nameTu = "Left_"
            elif data[1] == 2 :
                nameTu = "Right_"
            else :
                print("recive Frame tu server bi sai form", data)
                continue
            numberTu = int(data[2]) # neu numberTu = 255 tat ca cac tu

            if (numberTu <= server.numClientLeft and data[1] == 1 ) or (numberTu <= server.numClientRight and data[1] == 2) or numberTu == 255:
              if numberTu == 0x00: # 00 la tu Master
                if len(dt)==2 and dt[0] ==0xab and dt[1]== 0xab: #cap nhat thong tin tu
                  dtSend = b'\xaa\xaa'+ bytearray(uart.dataReceved.myList)+ b'\x00\x00'
                  self.conn.send(dtSend)
              else:
                nameTu = nameTu + str(numberTu)
                
                
                elif len(dt) == 2 and dt[0] == 0xbb and ( dt[1] == 0x01 or dt[1] == 0x02 or dt[1] == 0x03):#bao an toan
                    print("Pc bao an toan-nhom chuc nang su co")
                    pass
                elif len(dt)==2 and dt[0] == 0xdd : # nhom chuc nang dieu khien dieu hoa
                    
                    print('van Hanh dieu hoa ' , dt[1] )
                    
                elif len(dt)==2 and dt[0] == 0xee : # nhom chuc nang phu tro
                    print(dt)
                
                elif len(dt)==2 and dt[0] == 0xff : # nhom chuc nang cai dat
                    value = self.conn.recv(1)[0]
                    print('dt', dt, '  value', value)                                      
          
          elif len(data) == 3 and data[0] == 0x23 and data[1] == 0x23 and data[2] == 0x23: #truyen nhan du lieu hton gtin tu
            #dt 2byte luc nay la ID master hien tai chua can dung toi
            header = self.conn.recv(7) # theo header la doc 7 byte tiep theo
            print('header : ', header)
            if len(header) == 7 : # neu nhan du 7 byte 
              maLenh = int(header[0])
              lengthAfter = int(header[4]<<24) + int(header[3]<<16) + int(header[2]<<8) + int(header[1])
              print('maLenh=',maLenh , '   lengthAfter=',lengthAfter)
              #doc du so byte gui toi
              lengthByteReaded = 0
              self.csdl = b''
              while (len(self.csdl) < lengthAfter):
                self.csdl += self.conn.recv(1024)
              print('dattaInfor = ' ,len(self.csdl))

              dataString = self.csdl.decode('utf-8') #decode('ISO-8859-1')

              kq = dataString.split('$$$')
              for dt in kq :
                online = dt.split('&&&')
                print('length=', len(online), '   ', online)

              print('da phan tich xong du lieu')

          elif not data or not dt:
              print('data', data , '   dt=',dt)
              self.conn.close()
              print("Client masterPC exit or connection error")
              break
              
        except Exception as e:
            print("Exception masterPC : ",str(e))
            self.conn.close()
            break

def sentTimKiem2PC(data): # tam toi send tim kiem tong quat den PC
    
    header = b'\x23\x23\x23\x31\x32\x61'
    lenData = struct.pack('I', int(len(data)))
    header = header + lenData + b'\x00\x00' # 2 byte cuoi la CRC
    if len(header) == 12 :
        header += data.encode()
        ServerPC.conn.send(header)
        print("sent yeu cau den PC : ", header )


'''
dataInfor =  b'32&&&123&&&B\xc3\xa1o c\xc3\xa1o t\xc3\xacnh h\xc3\xacnh th\xe1\xbb\xb1c hi\xe1\xbb\x87n c\xc3\xb4ng t\xc3\xa1c thu BHXH c\xe1\xbb\xa7aBHXH huy\xe1\xbb\x87n Minh H\xc3\xb3a qu\xc3\xbd II n\xc4\x83m 2001&&&3&&&3&&&0&&&14'
  '$$$33&&&128&&&B\xc3\xa1o c\xc3\xa1o thu BHXH c\xe1\xbb\xa7a BHXH t\xe1\xbb\x89nh Qu\xe1\xba\xa3ng B\xc3\xacnh qu\xc3\xbd I- IV n\xc4\x83m 2001 (04 quy\xe1\xbb\x83n)&&&2&&&1&&&0&&&32$$$123&&&429&&&Ch\xe1\xbb\xa9ng t\xe1\xbb\xab ti\xe1\xbb\x81n m\xe1\xba\xb7t phi\xe1\xba\xbfu chi 1096-1268 c\xe1\xbb\xa7a BHXH t\xe1\xbb\x89nh Qu\xe1\xba\xa3ng B\xc3\xacnh th\xc3\xa1ng 08 n\xc4\x83m 2008 (02 t\xe1\xba\xadp)&&&1&&&2&&&0&&&66$$$344&&&1123&&&B\xc3\xa1o c\xc3\xa1o chi l\xc6\xb0\xc6\xa1ng h\xc6\xb0u, tr\xe1\xbb\xa3 c\xe1\xba\xa5p BHXH do qu\xe1\xbb\xb9 BHXH, ngu\xe1\xbb\x93n NSNN \xc4\x91\xe1\xba\xa3m b\xe1\xba\xa3o c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n Minh H\xc3\xb3a th\xc3\xa1ng 01-12 n\xc4\x83m 2012&&&3&&&1&&&0&&&46$$$369&&&1230&&&B\xc3\xa1o c\xc3\xa1o th\xe1\xbb\x91ng k\xc3\xaa k\xe1\xba\xbft qu\xe1\xba\xa3 thu, chi BHXH,BHYT, BHTN c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n Tuy\xc3\xaan H\xc3\xb3a th\xc3\xa1ng 09-11 n\xc4\x83m 2013&&&1&&&2&&&0&&&26$$$369&&&1231&&&B\xc3\xa1o c\xc3\xa1o th\xe1\xbb\x91ng k\xc3\xaa k\xe1\xba\xbft qu\xe1\xba\xa3 thu, chi BHXH, BHYT, BHTN c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n Minh H\xc3\xb3a th\xc3\xa1ng 09-12 n\xc4\x83m 2013&&&1&&&3&&&0&&&12$$$369&&&1232&&&B\xc3\xa1o c\xc3\xa1o th\xe1\xbb\x91ng k\xc3\xaa k\xe1\xba\xbft qu\xe1\xba\xa3 thu, chi BHXH, BHYT, BHTN c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n Qu\xe1\xba\xa3ng Tr\xe1\xba\xa1ch th\xc3\xa1ng 09-12 n\xc4\x83m 2013&&&3&&&3&&&0&&&27$$$369&&&1233&&&B\xc3\xa1o c\xc3\xa1o th\xe1\xbb\x91ng k\xc3\xaa k\xe1\xba\xbft qu\xe1\xba\xa3 thu, chi BHXH, BHYT, BHTN c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n Qu\xe1\xba\xa3ng Ninh th\xc3\xa1ng 09-12 n\xc4\x83m 2013&&&3&&&1&&&0&&&33$$$369&&&1234&&&B\xc3\xa1o c\xc3\xa1o th\xe1\xbb\x91ng k\xc3\xaa k\xe1\xba\xbft qu\xe1\xba\xa3 thu, chi BHXH, BHYT, BHTN c\xe1\xbb\xa7a BHXH huy\xe1\xbb\x87n L\xe1\xbb\x87 Th\xe1\xbb\xa7y th\xc3\xa1ng 09-12 n\xc4\x83m 2013&&&3&&&1&&&0&&&45$$$369&&&1235&&&B\xc3\xa1o c\xc3\xa1o t\xc4\x83ng, gi\xe1\xba\xa3m chi BHXH h\xc3\xa0ng th\xc3\xa1ng cho c\xc3\xa1c \xc4\x91\xe1\xbb\x91i t\xc6\xb0\xe1\xbb\xa3ng do qu\xe1\xbb\xb9 BH th\xe1\xba\xa5t nghi\xe1\xbb\x87p \xc4\x91\xe1\xba\xa3m b\xe1\xba\xa3o c\xe1\xbb\xa7a BHXH t\xe1\xbb\x89nh Qu\xe1\xba\xa3ngB\xc3\xacn'
dataString = dataInfor.decode('utf-8')
kq = dataString.split('$$$')
for dt in kq :
  online = dt.split('&&&')
  print('length=', len(online), '   ', online)


'''
ServerPC = ServerPC()
ServerPC.start()
isListenCL = 10
isListenCL = input('tintin')
while isListenCL :
    try:
        sentTimKiem2PC(isListenCL)
        isListenCL = input('tintin')
    except Exception as e:
        print(e.__doc__())
        isListenCL = 0
        break

