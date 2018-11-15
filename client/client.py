import socket
import threading
import time
import uart
import logging


IPSERVER = "192.168.0.100"
PORTSERVER = 24594
BUFFER = 1024
global soc, isConnect2Ser,isActive2Ser,isListeningSer
isActive2Ser = False
isConnect2Ser =False
isListeningSer =True
isSent2Ser=True
isWaiting = 0
isFullScreen = True
isExitApp = False

threadLock = threading.Lock()
class listeningServer(threading.Thread):
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.daemon = True
    def run(self):
        global isConnect2Ser,isActive2Ser,isListeningSer,isWaiting, isExitApp
        self.logger = logging.getLogger("listeningServer")
        print("listen Server")
        while isListeningSer:
            #lang nghe du lieu tu client d\gui den
            data = self.connection.recv(2)
            print(data)
            if not data :
                isConnect2Ser =False
                isActive2Ser = False
                self.connection.close()
                break
            else :
                print("in hear")
                if len(data) == 2 and data[0] == 0x4f and data[1] == 0x4b:
                    isActive2Ser =True
                    print("actived ok ")
                elif len(data) == 2 and data[0] == 78 and data[1] == 71:
                    isActive2Ser = False
                    print("server logout")
                elif len(data) == 2 and data[0] == 0xdd and data[1] == 0xaa:
                    "sent data to server"
                    ThClientMain.sent2Server(b'\xaa\xaa'+bytes(bytearray(uart.dataReceved.myList)))   

                elif len(data) == 2 and data[0] == 0xbb and data[1] == 0xbb :
                    data = self.connection.recv(8)
                    if len(data) == 8:
                        i=0
                        while i<8:
                            uart.DataPi2Ar[i] = data[i]
                            i+=1
                        uart.sent2Arduino()
                elif len(data) == 2 and data[0] == 0xee and data[1] == 0xee:
                    data = self.connection.recv(8)
                    if len(data) == 8:
                        i=0
                        while i<8:
                            uart.DataPi2Ar[i] = data[i]
                            i+=1
                        uart.saveConfig()
                elif len(data) == 2 and data[0] == 0xef and data[1] == 0xef:
                    "received waiting"
                    isWaiting = 1
                    uart.DataPi2Ar[2] = 0x06 # trang thai chuan bi dong mo tu
                    uart.sent2Arduino()
                elif len(data) == 2 and data[0] == 0xef and data[1] == 0xee:
                    "received done waiting"
                    isWaiting = 0
                elif len(data) == 2 and data[0] == 0xef and data[1] == 0xed:
                    "received dung khan cap"
                    isWaiting = 2
                    uart.DataPi2Ar[2] = 0x00
                    uart.sent2Arduino()
                elif len(data) == 2 and data[0] == 0xac and data[1] == 0xac:
                    isExitApp = True
                    


class ClientThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self):
        global isConnect2Ser
        print("ClientThreadMain is running")
        self.numClick2close = 0
        while isSent2Ser:
            if isConnect2Ser == False:
                try :
                    self.startConect2Ser()
                    time.sleep(1)
                    
                    self.sent2Server(b'\xbb\xbb'+bytes(uart.DataPi2Ar))
                except :
                    print("ko ket noi toi server")
            time.sleep(10)
            self.numClick2close = 0
                
    def startConect2Ser(self):
        global isConnect2Ser
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
        self.soc.connect((IPSERVER, PORTSERVER))
        isConnect2Ser = True
        print("connect thanh cong toi server")
        ThreadListenSer = listeningServer(self.soc)
        ThreadListenSer.start()
        

    def sent2Server(self,dataSent):
        threadLock.acquire()
        self.soc.send(dataSent)
        threadLock.release()
ThClientMain = ClientThread()
ThClientMain.start()