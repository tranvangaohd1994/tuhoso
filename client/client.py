import ctypes
import serial
import threading
import json
import socket
import time
import logging
from pygame import mixer
from subprocess import call
from time import strftime
#cho 7s roi moi chay
#time.sleep(7)
#function to calculate code CRC checksum
def crc16(data: bytes):
    pass
#class save infor receive
class dataInfor():
    def __init__(self):
        self.myList=[]
        self.tempOut = 0
        self.humiOut = 0
        self.distanceSen_Real = 0
        for i in range(0,30):
            self.myList.append(0)
        self.setData(self.myList)

    def setData(self, arrData):
        for i in range(0,30):
            self.myList[i] = arrData[i]
        self.tempIn = int(arrData[0] + (arrData[1]<<8))/10
        self.humiIn = int(arrData[2] + (arrData[3]<<8))/10
        #self.tempOut = int(arrData[4] + (arrData[5]<<8))/10
        #self.humiOut = int(arrData[6] + (arrData[7]<<8))/10
        self.fireSenIn = int(arrData[8])
        self.fireSenOut = int(arrData[9])
        self.infrared_1 = int(arrData[10])
        self.infrared_2 = int(arrData[11])
        self.infrared_3 = int(arrData[12])
        self.infrared_4 = int(arrData[13])
        self.numPersonIn = int(arrData[14])
        self.numPersonOut = int(arrData[15])
        self.proximitySen_1=int(arrData[16])
        self.proximitySen_2=int(arrData[17])
        self.electricMotor = int(arrData[18])
        self.distanceSen_1 = int(arrData[19])
        self.distanceSen_2 = int(arrData[20])
        self.switchTrip_1 = int(arrData[21])
        self.switchTrip_2 = int(arrData[22])
        self.switchTrip_3 = int(arrData[23])
        self.lights = int(arrData[24])
        self.ventilator_1 = int(arrData[25]) 
        self.ventilator_2 = int(arrData[26])
        self.fingerprintSen = int(arrData[27])
        self.statusLight = int(arrData[28])
        self.statusMotor = int(arrData[29])
#class thread to read data 
class readUart(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.daemon = True
    def run(self):
        global dataCanhBao,isRead,caseBDIsACK,ser
        while isRead :
            try :      
                s=ser.read(2)
                if len(s) == 2 and s[0]==0xAA and s[1] == 0xAA :
                    #cap nhat thong tin cam bien tu Ar len Pi
                    data = ser.read(30)
                    crc  = ser.read(2)
                    if len(data) == 30 and len(crc) == 2 :
                        dataReceved.setData(data)
                        if isConnect2Ser == True :
                            try :
                                ThClientMain.sent2Server(b'\xaa\xaa'+bytes(bytearray(dataReceved.myList)))
                            except Exception as e:
                                print("ThClientMain.sent2Server ",e.__doc__)
                                loggerInfor.info("ThClientmain.sent2Server " + str(e.__doc__))
                    else :
                        pass
                        #self.respont2Arduino(0)
                #case warning incident 
                elif len(s) == 2 and s[0] == 0xBB and s[1] == 0xBB :
                    #call function warning incident
                    dataIncident = ser.read(4) 
                    dataCanhBao = int(dataIncident[1]<<8) + int(dataIncident[0])

                #nhan ACK va ERR
                elif len(s) == 2 and s[0] == 0x41 and s[1] == 0x43:
                    #ACK
                    s=ser.read(1)
                    caseBDIsACK = 2                
                elif len(s) ==2 and s[0] ==0x45 and s[1]==0x52 :
                    #ERR
                    s = ser.read(1)
                    caseBDIsACK = 1

                    
                    
            except KeyboardInterrupt:
                ser.close()
                print("ser.close()")
            except Exception as e:
                print("ERROR SERIAL : ",e.__doc__)
                loggerInfor.info("Error Serial "+ str(e.__doc__))
    
    def respont2Arduino(self,isOK):
        dt =b''
        if isOK > 0 : 
            dt = b'ACK'
        else :
            dt = b'ERR'
        try :
            threadLock.acquire()
            ser.write(dt)
            ser.flush()
            threadLock.release()
        except:
            pass
            #print ('respont2Arduino')
#statusSerial =0-available  =1 waiting respont from Arduino

class listeningServer(threading.Thread):
    def __init__(self,connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.daemon = True
        self.dataCamBien = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    def run(self):
        global isConnect2Ser,isActive2Ser,isListeningSer,isWaiting, isExitApp,statusSuCo,caseBD, DataCamBien
        self.logger = logging.getLogger("listeningServer")
        print("listen Server")
        while isListeningSer:
            try:
                #lang nghe du lieu tu client d\gui den
                data = self.connection.recv(2)
                #print(data)
                if not data :
                    isConnect2Ser =False
                    isActive2Ser = False
                    self.connection.close()
                    break
                else :
                    #print("in hear")
                    if len(data) == 2 and data[0] == 0x4f and data[1] == 0x4b:
                        isActive2Ser =True
                        dtBatDat = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
                        sentDataRandom(b'\xcc\xcc', bytes(dtBatDat))
                        print("actived ok ")
                    elif len(data) == 2 and data[0] == 78 and data[1] == 71:
                        isActive2Ser = False
                        print("server logout")
                    elif len(data) == 2 and data[0] == 0xdd and data[1] == 0xaa:
                        "sent data to server"
                        ThClientMain.sent2Server(b'\xaa\xaa'+bytes(bytearray(dataReceved.myList)))   

                    elif len(data) == 2 and data[0] == 0xbb and data[1] == 0xbb :
                        #cai dat 8 byte cho ARduino
                        data = self.connection.recv(8)
                        if len(data) == 8:
                            for i in range(0,8):
                                DataPi2Ar[i] = data[i]
                            sent2Arduino()
                    elif len(data) == 2 and data[0] == 0xee and data[1] == 0xee:
                        data = self.connection.recv(8)
                        print("Server sent file config to client")
                        if len(data) == 8:
                            for i in range(0,8):
                                DataPi2Ar[i] = data[i]
                            saveConfig()
                    elif len(data) == 2 and data[0] == 0xef and data[1] == 0xef:
                        "received waiting"
                        isWaiting = 1
                        DataPi2Ar[2] = 0x06 # trang thai chuan bi dong mo tu
                        dataReceved.statusMotor = 6 
                        sent2Arduino()
                    elif len(data) == 2 and data[0] == 0xef and data[1] == 0xee:
                        "received done waiting"
                        isWaiting = 0
                    elif len(data) == 2 and data[0] == 0xef and data[1] == 0xed:
                        "received dung khan cap"
                        print("server sent dung khan cap")
                        isWaiting = 2
                        DataPi2Ar[2] = 0x00
                        sent2Arduino()
                    elif len(data) == 2 and data[0] == 0xac and data[1] == 0xac:
                        isExitApp = True
                    elif len(data) == 2 and data[0] == 0xcb and data[1] == 0xcb:
                        dt = self.connection.recv(2)
                        statusSuCo = int(dt[0])
                        isWaiting = int(dt[1])
                        
                    elif len(data) == 2 and data[0] == 0xcb and data[1] == 0xcd:
                        "kiem tra su co thanh cong"
                        self.dataCamBien = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
                        if statusSuCo == 1: #co người trong tu
                            self.dataCamBien[3] = 0x31
                        elif statusSuCo == 2 or statusSuCo == 3 : # 2 chay trong 3 chay ngoai
                            self.dataCamBien[3] = 0x32
                        elif  statusSuCo == 4: #co vat can
                            self.dataCamBien[3] = 0x33
                        statusSuCo = 0
                        isWaiting = 0
                        print("kiem tra su co thanh cong", self.dataCamBien[3])
                        if self.dataCamBien[3] != 0:
                            dataCanhBao = 0
                            sentDataRandom(b'\xdd\xdd',bytes(self.dataCamBien))
                            
                    elif len(data) == 2 and data[0] == 0xcd and data[1] == 0xcd:
                        statusSuCo = 0
                        isWaiting = 0
                        
                    elif len(data) == 2 and data[0] == 0xbd and data[1] == 0xbd:
                        dt = self.connection.recv(1)
                        caseBD = int(dt[0])#doc 1 byte 
                    
                    elif len(data) == 2 and data[0] == 0xdc and data[1] == 0xdc :
                        #khoa Dong cơ
                        dt = self.connection.recv(1)
                        for i in range(0,8):
                            DataCamBien[i] = 0x00
                        if len(dt) == 1 and dt[0] == 0x01:
                            DataCamBien[5] = 0x30 # mo dc
                        elif len(dt) == 1 and dt[0] == 0x00:    
                            DataCamBien[5] = 0x31 #Khoa dc
                        sentCambien()

                    elif len(data) == 2 and data[0] == 0x10 and data[1] == 0x0a : #server bao client phat loa xxx
                        dt = self.connection.recv(3)
                        if len(dt) == 3:
                            filemp3 = folderMP3+ dt.decode() + ".mp3"
                            playmp3(filemp3)

                    elif len(data) == 2 and data[0] == 0x1d and data[1] == 0x1d :
                        #server bao thong gio
                        dt = self.connection.recv(2)
                        if len(dt) == 2:
                            for i in range(0,8):
                                DataCamBien[i] = 0x00
                            if dt[0] == 0x01 :# bat thong gio
                                DataCamBien[6] = dt[1]
                                DataCamBien[1] = 0x31
                            else : # tat thong gio
                                DataCamBien[1] = 0x30
                            sentCambien()
                    
                    elif len(data) == 2 and data[0] == 0xfa and data[1] == 0xfa :
                        dt = self.connection.recv(14)
                        da = dt.decode()
                        _date = "sudo date -s "
                        _date += '\"'+ da[0:4] + '-' + da[4:6] + '-' + da[6:8] + ' '
                        _date += da[8:10] + ':' + da[10:12] + ':' + da[12:14]+ '+0700\"'
                        call(_date ,shell=True)
                        _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
                        print(_date)
                    
                    elif len(data) == 2 and data[0] == 0xdd and data[1] == 0xdd : #server gui lenh bat den cho client
                        for i in range(0,8):
                            DataCamBien[i] = 0x00
                        DataCamBien[0]=0x31
                        sentCambien()

                    elif len(data) == 2 and data[0] == 0xdd and data[1] == 0xdf : #lenh tat den client    
                        for i in range(0,8):
                            DataCamBien[i] = 0x00
                        DataCamBien[0]=0x30
                        sentCambien()
                    elif len(data) == 2 and data[0] == 0xda and data[1] == 0xda : #lenh tat den client    
                        tempHumi = self.connection.recv(6)
                        if len(tempHumi) == 6 :
                            dataReceved.tempOut = int(tempHumi[0] + (tempHumi[1]<<8))/10
                            dataReceved.humiOut = int(tempHumi[2] + (tempHumi[3]<<8))/10
                            dataReceved.distanceSen_Real = int(tempHumi[4]+(tempHumi[5]<<8))
                            

            except Exception as e:
                print("Exception connection to server ",e.__doc__)
                self.connection.close()
                isConnect2Ser =False
                isActive2Ser = False
                break

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
                    
                    self.sent2Server(b'\xbb\xbb'+bytes(DataPi2Ar))
                except :
                    print("ko ket noi toi server")
                    loggerInfor.info("Khong ket noi toi server")
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
        global isConnect2Ser
        if isConnect2Ser :
            threadLock.acquire()
            self.soc.send(dataSent)
            threadLock.release()

def sent2Arduino():
    dataSent =b'\xcc\xcc' + bytes(DataPi2Ar) + b'\x00\x00'
    threadLock.acquire()
    ser.write(dataSent)
    ser.flush()
    threadLock.release()
    print("sent 2 Arduino ", dataSent)

def sentCambien():
    dataSent = b'\xdd\xdd' + bytes(DataCamBien) + b'\x00\x00'
    threadLock.acquire()
    ser.write(dataSent)
    ser.flush()
    threadLock.release()
    print("sent 2 ar sentCambien ", dataSent)

def sentDataRandom(header2,data2):
    dataSent = header2 + data2 + b'\x00\x00'
    threadLock.acquire()
    ser.write(dataSent)
    ser.flush()
    threadLock.release()
    print("sentDataRandom :", dataSent)

def saveConfig():
    dataAllJsonConfig["data0"] = int(DataPi2Ar[0])
    dataAllJsonConfig["data1"] = int(DataPi2Ar[1])
    dataAllJsonConfig["data2"] = int(DataPi2Ar[2])
    dataAllJsonConfig["data3"] = int(DataPi2Ar[3])
    dataAllJsonConfig["data4"] = int(DataPi2Ar[4])
    dataAllJsonConfig["data5"] = int(DataPi2Ar[5])
    dataAllJsonConfig["data6"] = int(DataPi2Ar[6])
    dataAllJsonConfig["data7"] = int(DataPi2Ar[7])
    with open('/home/pi/Desktop/client/config.json', 'w') as outfile:
        json.dump(dataAllJsonConfig, outfile) 
def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger

#setup logger
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# first file logger
loggerInfor = setup_logger('Infor_logger', '/home/pi/Desktop/Infor.log')
loggerInfor.info('--------------Phien Hoat Dong Moi--------------------')

try :
        
    ser = serial.Serial(
        port = '/dev/ttyAMA0',
        baudrate = 9600,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        bytesize = serial.EIGHTBITS,
        timeout = 1
    )
except Exception as e :
    loggerInfor.info("Error init serial -- " + str(e.__doc__))

dataCanhBao = 0
isRead = True
statusSerial = 0
isReadAvailable = False
isMotorOpen = False
caseBDIsACK = 0

#lock de dong bo thread
threadLock = threading.Lock()

#{0:{1:"dieu  khien tu dong",0:"dieu khien bang tay"},  1:{0:"chua cai",1:"Motu dong co quay thuan",2:"motu quay nghich"}
# 2:{0:"dung",1:"Mo tu",2:"Dong tu"},   3:{khoang cach mo tu}   4:{Luc chong ket}   
# 5:{Tat tin hieu cam bien}   6:{Toc do dong co}  7:{khoang cach giam toc do dong co}
DataPi2Ar = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
DataCamBien = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

dataReceved = dataInfor()

dataAllJsonConfig={}

listCanhBao = [" ","Cháy trong","Cháy Ngoài","Cháy trong và ngoài","Giá sách nhô","Có vật cản","Có người trong tủ"]
#load file config when start
with open('/home/pi/Desktop/client/config.json') as json_data:
    datajs = json.load(json_data)
    dataAllJsonConfig=datajs
    DataPi2Ar[0]= int(datajs["data0"])
    DataPi2Ar[1]= int(datajs["data1"])
    DataPi2Ar[2]= int(datajs["data2"])
    DataPi2Ar[3]= int(datajs["data3"])
    DataPi2Ar[4]= int(datajs["data4"])
    DataPi2Ar[5]= int(datajs["data5"])
    DataPi2Ar[6]= int(datajs["data6"])
    DataPi2Ar[7]= int(datajs["data7"])

################################################################## Client ##########################################
folderMP3 = "/home/pi/backup/02/"

IPSERVER = "192.168.0.100"
PORTSERVER = 24594
BUFFER = 1024
global soc, isConnect2Ser,isActive2Ser,isListeningSer
isActive2Ser = False
isConnect2Ser =False
isListeningSer =True
isSent2Ser=True
isWaiting = 0
isFullScreen = False
isExitApp = False
statusSuCo = 0
threadLock = threading.Lock()
caseBD = -1
mixer.init()

def saveNhietDoDoAm():
    global myNumberTu
    H = strftime("%H")
    M = strftime("%M")#minute
    S = strftime("%S")
    d = strftime("%d")
    m = strftime("%m")#month
    Y = strftime("%Y")
    fileLog = '/home/pi/backup/temp/'+ Y + m + d + '.txt'
    file = open(fileLog,"a")
    s =  H + ':' + M + ' ' + '0' + " "+str(dataReceved.tempIn )+" " +str(dataReceved.humiIn )+" "+str(dataReceved.tempOut )+ " "+str(dataReceved.humiOut )+'\n'
    file.write(s) 
    file.close()

def playmp3(nameFile):
    try:
        mixer.music.load(nameFile)
        mixer.music.play()
    except Exception as e :
        print("error in playmp3" + str(e))
        loggerInfor.info("Error play mp3")

ThClientMain = ClientThread()
ThClientMain.start() 

threadRead = readUart(1,"readUart",1)
threadRead.start()

#{"data2": 6, "data0": 1, "data3": 80, "data1": 2, "data6": 8, "data7": 60, "data4": 8, "data5": 0}