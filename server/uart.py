import ctypes
import serial
import threading
import json
#function to calculate code CRC checksum
def crc16(data: bytes):
    pass

#class save infor receive
class DataInforSer():
    def __init__(self):
        self.myList=[]
        for i in range(0,30):
            self.myList.append(0)
        self.setData(self.myList)
        self.numPersonOld = 0
    
    def setData(self, arrData):
        for i in range(0,30):
            self.myList[i] = arrData[i]
        self.tempIn = int(arrData[0] + (arrData[1]<<8))/10
        self.humiIn = int(arrData[2] + (arrData[3]<<8))/10
        self.tempOut = int(arrData[4] + (arrData[5]<<8))/10
        self.humiOut = int(arrData[6] + (arrData[7]<<8))/10
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
        
#ttyAMA0
ser = serial.Serial(
	port = '/dev/ttyAMA0',
	baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
	timeout = 1
)
#class thread to read data 
class readUart(threading.Thread):
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.daemon = True
    def run(self):
        global dataCanhBao,isRead, caseBDIsACK
        while isRead :
            try :      

                s=ser.read(2)# read 2 byte header
                #print(s)

                #case data
                if len(s) == 2 and s[0]==0xAA and s[1] == 0xAA :
                    data = ser.read(30)
                    crc  = ser.read(2)
                    if len(data) ==30 and len(crc) == 2 :
                        dataReceved.setData(data)
                        
                        #mycrc = crc16(data)
                        #if mycrc == crc :
                        if True:
                            #update data and respont to Arduino
                            self.respont2Arduino(1)
                        else :
                            self.respont2Arduino(0)
                    else :
                        self.respont2Arduino(0)
                #case warning incident 
                elif len(s) == 2 and s[0] == 0xBB and s[1] == 0xBB :
                    #call function warning incident
                    dataIncident = ser.read(4) 
                    dataCanhBao = int(dataIncident[1]<<8) + int(dataIncident[0])
                    #print(dataCanhBao)

                elif len(s) == 2 and s[0] == 0x41 and s[1] == 0x43:
                    #ACK
                    s=ser.read(1)
                    statusSerial = 0
                    caseBDIsACK = 2
                
                elif len(s) ==2 and s[0] ==0x45 and s[1]==0x52 :
                    #ERR
                    s = ser.read(1)
                    caseBDIsACK = 1
                    pass
                    
            except KeyboardInterrupt:
                ser.close()
                print("ser.close()")
            except Exception as e:
                print("ERROR SERIAL : ",e.__doc__)
    
    def respont2Arduino(self,isOK):
        dt =b''
        if isOK > 0 : 
            dt = b'ACK'
        else :
            dt = b'ERR'
        try :
            while isWriteAvailable == False :
                #wating neu serial van dang gui
                pass
            #set flag isWriteAvailable = false  to an other process don't use serial
            isWriteAvailable =False
            ser.write(dt)
            ser.flush()
            isWriteAvailable =True
        except:
            pass
            #print ('respont2Arduino')
#statusSerial =0-available  =1 waiting respont from Arduino

def sent2Arduino():
    crcData = b'\x00\x00'
    #strEncode = data.encode()
    dataSent = HeaderPi2Ar + bytes(DataPi2Ar) + crcData
    ser.write(dataSent)
    ser.flush()
    #print("sent 2 Arduino ", dataSent)

def sentCambien():
    crcData = b'\x00\x00'
    dataSent = b'\xdd\xdd' + bytes(DataCamBien) + crcData
    ser.write(dataSent)
    ser.flush()
    #print("sentCambien 2 Arduino -- sentCambien", dataSent)
def sentDataRandom(header2,data2):
    crcData = b'\x00\x00'
    dataSent = header2 + data2 + crcData
    ser.write(dataSent)
    ser.flush()
    #print("sentDataRandom 2 Arduino ", dataSent)


def saveConfig():
    dataAllJsonConfig["data0"] = int(DataPi2Ar[0])
    dataAllJsonConfig["data1"] = int(DataPi2Ar[1])
    dataAllJsonConfig["data2"] = int(DataPi2Ar[2])
    dataAllJsonConfig["data3"] = int(DataPi2Ar[3])
    dataAllJsonConfig["data4"] = int(DataPi2Ar[4])
    dataAllJsonConfig["data5"] = int(DataPi2Ar[5])
    dataAllJsonConfig["data6"] = int(DataPi2Ar[6])
    dataAllJsonConfig["data7"] = int(DataPi2Ar[7])
    dataAllJsonConfig["dtMK"] = dtMK
    dataAllJsonConfig["dtMKHard"] = dtMKHard
    #/home/pi/Desktop/server/
    with open('/home/pi/Desktop/server/config.json', 'w') as outfile:
        json.dump(dataAllJsonConfig, outfile) 

dataCanhBao = 0
isRead = True
statusSerial = 0
isReadAvailable = False
isWriteAvailable = True
dtMK = ''
dtMKHard = ''
threadRead = readUart(1,"readUart",1)
threadRead.start()
isMotorOpen = False
caseBDIsACK = 0

HeaderPi2Ar = b'\xCC\xCC'
#{0:{1:"dieu  khien tu dong",0:"dieu khien bang tay"},  1:{0:"chua cai",1:"Motu dong co quay thuan",2:"motu quay nghich"}
# 2:{0:"dung",1:"Mo tu",2:"Dong tu"},   3:{khoang cach mo tu}   4:{Luc chong ket}   
# 5:{Tat tin hieu cam bien}   6:{Toc do dong co}  7:{khoang cach giam toc do dong co}
DataPi2Ar = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
DataCamBien = bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
crcPi2Ar = b'\x00\x00'

msgPi2Ar = HeaderPi2Ar+DataPi2Ar+crcPi2Ar
dataReceved = DataInforSer()

dataAllJsonConfig={}

listCanhBao = [" ","Cháy trong","Cháy Ngoài","Cháy trong và ngoài","Giá sách nhô","Có vật cản","Có người trong tủ"]
#load file config when start
#/home/pi/Desktop/server/
with open('/home/pi/Desktop/server/config.json') as json_data:
    #global dtMK, dtMKHard
    datajs = json.load(json_data)
    dataAllJsonConfig=datajs
    print("dataJson", datajs)
    print(datajs["data0"])
    DataPi2Ar[0]= int(datajs["data0"])
    DataPi2Ar[1]= int(datajs["data1"])
    DataPi2Ar[2]= int(datajs["data2"])
    DataPi2Ar[3]= int(datajs["data3"])
    DataPi2Ar[4]= int(datajs["data4"])
    DataPi2Ar[5]= int(datajs["data5"])
    DataPi2Ar[6]= int(datajs["data6"])
    DataPi2Ar[7]= int(datajs["data7"])
    dtMK = str(datajs["dtMK"])
    dtMKHard = str(datajs["dtMKHard"])
    

print(dtMK, "    ", dtMKHard)



