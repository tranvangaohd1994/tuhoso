
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
                    if len(data) == 3 and data[0] == 0xff:
                        if data[1] == 0x01 and data[2] <= server.numClientLeft :
                            dt = conn.recv(2)

                            if data[2] == 0x00:
                                if len(dt)==2 and dt[0] ==0xab and dt[1]== 0xab:
                                    dtSend = b'\xaa\xaa'+ bytearray(uart.dataReceved.myList)+ b'\x00\x00'
                                    conn.send(dtSend)
                            else:
                                nameTu = "Left_"+str(int(data[2]))
                                if len(dt)==2 and dt[0] ==0xAA:
                                    if dt[1] == 0x01 :
                                        server.dongMoTuFunction(0,0)
                                    elif dt[1] == 0x02 :
                                        if server.isWaiting == 2:
                                            server.dongMoTuFunction(2,nameTu)
                                        elif server.isWaiting == 0 :
                                            server.dongMoTuFunction(1,nameTu)
                                    elif dt[1] == 0x03:
                                        server.serverMain.sentStop2AllClient()
                                if len(dt)==2 and dt[0] ==0xab and dt[1]== 0xab:
                                    dtSend = b'\xaa\xaa'+ bytearray(server.dataReceivedSer[nameTu].myList)+ b'\x00\x00'
                                    conn.send(dtSend)
                    if not data:
                        conn.close()
                        print("Client masterPC exit")
                        break

                except Exception as e:
                    print("Exception masterPC : ",str(e))
                    conn.close()
                    break

ServerPC = ServerPC()
ServerPC.start()
                        
