import threading
import sys
import socket
import logging
import time
from uart import DataInforSer
from pygame import mixer
import struct
from time import strftime
import uart

#cai dat tu master la tu so may
myNumberTu = 4
folderMP3 = "/home/pi/backup/02/"
IPSERVER = "192.168.0.100"
PORT = 24594
usbFinger = "/dev/ttyUSB0"
usbDieuHoa = "/dev/ttyUSB1"
numClientLeft = 0
numClientRight = 0
arrIPArrdressLeft = {}
arrIPArrdressRight = {}

def loadConfigIP():
    global arrIPArrdressRight, arrIPArrdressLeft, numClientRight, numClientLeft
    numClientLeft = uart.dataAllJsonConfig["IPLeft"]["numLeftActive"]
    numClientRight = uart.dataAllJsonConfig["IPRight"]["numRightActive"]

    for i in range(1, numClientLeft + 1):
        tu = "Left_" + str(i)
        arrIPArrdressLeft[tu] = uart.dataAllJsonConfig["IPLeft"][tu]
    for i in range(1, numClientRight + 1):
        tu = "Right_" + str(i)
        arrIPArrdressRight[tu] = uart.dataAllJsonConfig["IPRight"][tu]

loadConfigIP()

#setup logger
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger
# first file logger
loggerInfor = setup_logger('Infor_logger', '/home/pi/Desktop/Infor.log')
loggerInfor.info('--------------Phien Hoat Dong Moi--------------------')
# second file logger
suCo_logger = setup_logger('suCo_logger', '/home/pi/Desktop/SuCo.log')
suCo_logger.error('--------------Phien Hoat Dong Moi--------------------')

numThongGio, executeThongGio, countThongGio = 0,0,60 # tham so cho thong gio
#giao dien
isFullScreen = False
isFullSceen = False
# bien kiem tra xem tu nao dang duoc mo
tuOpenedRight = tuOpenedLeft = tuActive = '0'
tuTraiPhai = 'A' #chon tu nao de thuc hien dong mo tu, A-all ca 2 ben, L-left, R-right
haveSucoClient = False

isGetDataFromClient = True
isFlag2906 = False
#lock de dong bo thread
threadLock = threading.Lock()
#mang de luu tat ca cac ket noi den server
dataReceivedSer = {}
dataSent2Client = {}
allConnection = {}
userLogin = False
isListenCL=True
isWaiting = 0
isExitApp = False
debugg = False
#caseBaoDuong
caseBD = 0
checkBDok = False

#danh cho dong tu lan dau
doneDongTuLanDau = False
statusVanHanh = 0 # 0-mainDisplay 1-waitingForm 2-svDieuKhienDieuHoa 3-BaoDuongServer
statusSuCo = 0
#mang de kiem tra xem su co thuoc loai nao 0-co nguoi trong tu 1-chay trong 2-chay ngoai 3-gia sach nho co vat can 4-dong co khoa
arraySuCo = ['0','0','0','0','0'] 
mixer.init()

threadDongMoTu = None

#class data sent to client
class DataSent2Client :
    def __init__(self):
        self.dt2Pi2Ar=bytearray([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
    def setData(self,data):
        for i in range (0,8):
            self.dt2Pi2Ar[i] = data[i]

class DongMoTu :
    def __init__(self):
        self.stopped = False
        self.timeSleepp = 0.05
        self.timeMiliSecond = 0.01
        self.timeDelayTu = 0.5

    def checkSuCo(self,ishuman):
        "ham kiem tra co su co hay khong truoc khi van hanh va kiem tra theo timer"
        global statusSuCo,isWaiting, tuTraiPhai
        threadLock.acquire()
        #reset mang su co
        statusSuCo = 0
        for i in range(5):
            arraySuCo[i] = '0'

        if uart.dataReceved.fireSenIn == 1 :
            arraySuCo[1] = 'Master'
            statusSuCo = 2 #== la bao chay trong
            msg = "Master có cháy trong"
            suCo_logger.error(msg)
        if uart.dataReceved.fireSenOut == 1 :
            arraySuCo[2] = 'Master'
            statusSuCo = 3
            msg = "Master có cháy ngoai"
            suCo_logger.error(msg)

        for dt in dataReceivedSer:
            if statusSuCo != 0 :
                break
            if tuTraiPhai == 'A' or  tuTraiPhai == dt[0] : #chi check tu ben trai hoac ben phai
                if dataReceivedSer[dt].fireSenOut == 1 :
                    statusSuCo = 3 # bao chay ngoai
                    arraySuCo[2] = dt
                    msg = str(dt) + " có cháy ngoài"
                    suCo_logger.error(msg)
                    break
                if dataReceivedSer[dt].fireSenIn == 1:
                    arraySuCo[1] = dt
                    statusSuCo = 2 #== la bao chay trong
                    msg = str(dt) + " có cháy trong"
                    suCo_logger.error(msg)
                    break
        for dt in dataReceivedSer:
            if statusSuCo != 0 :
                break
            if tuTraiPhai == 'A' or  tuTraiPhai == dt[0] : #chi check tu ben trai hoac ben phai
                if dataReceivedSer[dt].numPersonIn == 1 :
                    statusSuCo = 1 # co nguoi trong tu
                    arraySuCo[0] = dt
                    msg = str(dt) + " có người trong tủ"
                    suCo_logger.error(msg)
                    break
        for dt in dataReceivedSer:
            if statusSuCo != 0 :
                break
            if tuTraiPhai == 'A' or  tuTraiPhai == dt[0] : #chi check tu ben trai hoac ben phai
                if dataReceivedSer[dt].infrared_1 == 1 or dataReceivedSer[dt].infrared_2 != 0 or dataReceivedSer[dt].infrared_3 != 0 or dataReceivedSer[dt].infrared_4 != 0 : 
                    statusSuCo = 4 #gia sach nho co vat can
                    arraySuCo[3] = dt 
                    msg = str(dt) + " giá sách nhô có vật cản"
                    suCo_logger.error(msg)
                    break
        for dt in dataReceivedSer:
            if statusSuCo != 0 :
                break
            if tuTraiPhai == 'A' or  tuTraiPhai == dt[0] : #chi check tu ben trai hoac ben phai
                if dataReceivedSer[dt].khoaDC == 1:
                    arraySuCo[4] = dt
                    statusSuCo = 5
                    print('Khoa dong co tai tu,', dt)
                    break
        
        if statusSuCo != 0 or (statusSuCo == 0 and isWaiting == 0): # isWaiting == 0 tuc la ko trong qua trinh van hanh
            byteSuCo = struct.pack('bb',statusSuCo,isWaiting)
            for sock in allConnection:
                allConnection[sock].send(b'\xcb\xcb'+byteSuCo)#sent waiting
        threadLock.release()
        return statusSuCo
    
    def DoneSuCo(self,isPut):
        "kiem tra khong con su co nao nua"
        global statusSuCo,isWaiting, arraySuCo
        print("done su co")
        threadLock.acquire()
        statusSuCo = 0
        isWaiting = 0
        for sock in allConnection:
            if isPut == False :
                allConnection[sock].send(b'\xcd\xcd')
            else :
                #cgi sent reset cam bien cho tu nao bi xay ra su co
                if sock == arraySuCo[0] or sock == arraySuCo[1] or sock ==arraySuCo[2] or sock == arraySuCo[3]:
                    allConnection[sock].send(b'\xcb\xcd')#
                    print(sock, "reset")
                else :
                    allConnection[sock].send(b'\xcd\xcd')#
                    print(sock, "no reset")
        if isPut and (uart.dataReceved.fireSenIn == 1 or uart.dataReceved.fireSenOut == 1 ) :
            dataUartCamBien = bytearray([0x00, 0x00, 0x00, 0x32, 0x00, 0x00, 0x00, 0x00])
            uart.sentDataRandom(b'\xdd\xdd',bytes(dataUartCamBien))
            uart.dataReceved.fireSenIn = 0
            uart.dataReceved.fireSenOut = 0
        #cho cho den khi nao update xong
        for dt in dataReceivedSer:
            dataReceivedSer[dt].fireSenOut = 0
            dataReceivedSer[dt].fireSenIn = 0
            dataReceivedSer[dt].numPersonIn = 0

        threadLock.release()
      
    def sendMes2Client(self,numTu,dataSent):
        "ham send du lieu den client"
        threadLock.acquire()
        try:
            allConnection[numTu].send(dataSent)
            print(threading.get_ident()," sent 2 client ",numTu," ", dataSent)
        except:
            print("exception sent 2 client" , numTu)
        threadLock.release()

    def sentWaiting2AllClient(self):
        global isWaiting
        if isWaiting == 1:
            for dt in dataSent2Client:
                dataSent2Client[dt].dt2Pi2Ar[2] = 0x06

        for sock in allConnection:
            if isWaiting == 1 :
                allConnection[sock].send(b'\xef\xef')#sent waiting

            elif isWaiting == 0 :
                allConnection[sock].send(b'\xef\xee')#sent done waiting

    def waitingData_29_06(self):
        "cho cho cac client cap nhat du cac trang thai 0x06 -- chuan bi di chuyen "
        global isFlag2906
        for dt in dataReceivedSer:
            if dataReceivedSer[dt].statusMotor != 6 :
                #print('tu chua nhan 06 ', dt )
                return True
        #khi nay cac client da cap nhat het trang thai 0x06 chuan bi di chuyen
        isFlag2906 = True
        print("cac tu da nhan duoc lenh chuan bi van hanh 0x06")
        return False

    def sentStop2AllClient(self):
        threadLock.acquire()
        global isWaiting
        isWaiting = 2
        print("sent stop 2 all client")
        ss = " DUNG KHAN CAP"
        loggerInfor.info(ss)
        for sock in allConnection:
            allConnection[sock].send(b'\xef\xed')#sent stop to all client

        threadLock.release()

    def checkTuisOpened(self):
        global tuOpenedLeft, tuOpenedRight
        tuOpenedLeft = tuOpenedRight = '0'
        for dt in dataReceivedSer:
            if dataReceivedSer[dt].statusMotor == 2 :
                if dt[0] == 'L' :
                    tuOpenedLeft = dt
                elif dt[0] == 'R' :
                    tuOpenedRight = dt
        print("check tu is opened done tuLeft = " , tuOpenedLeft, '   tuRight = ',tuOpenedRight)

    def checkAllTuIsClosed(self):

        for dt in dataReceivedSer:
            if dataReceivedSer[dt].statusMotor != 4 :# check cac tu co deu dong khong
               return False
        return True

    def sentLogin2AllClient(self):
        threadLock.acquire()
        global userLogin
        for sock in allConnection:
            if isExitApp == True :
                allConnection[sock].send(b'\xac\xac')
            elif userLogin == True :
                allConnection[sock].send(b'OK')
            else :
                allConnection[sock].send(b'NG')

        threadLock.release()
       
    def checkQuaDong(self):
        for dt in dataReceivedSer:
            if dataReceivedSer[dt].electricMotor != 0 :
                #phat hien qua dong
                return True
        
        return False

    def sendDate2Client(self):
        H = strftime("%H")
        M = strftime("%M")
        S = strftime("%S")
        d = strftime("%d")
        m = strftime("%m")
        Y = strftime("%Y")
        dstr = Y+m+d+H+M+S #20171620092018  destr = dbyte.decode()
        dbyte = b'\xfa\xfa' + dstr.encode()
        print(dbyte, "    ", len(dbyte))

        if len(dbyte) == 16 :
            for sock in allConnection :   
                self.sendMes2Client(sock,dbyte)
        else :
            print("Error in sendDate2Client ")
    
    def thongGioFuction(self):
        global dataSent2Client, numClientLeft, numClientRight, folderMP3,tuTraiPhai,numThongGio, executeThongGio, countThongGio

        if numClientLeft > 0 :
            byKC = dataSent2Client["Left_1"].dt2Pi2Ar[3]
            disAvgLeft = int( byKC/numClientLeft )
        if numClientRight > 0:
            byKC = dataSent2Client["Right_1"].dt2Pi2Ar[3]
            disAvgRight = int( byKC/numClientRight )
        print('numThongGio Hien Tai,' , numThongGio)
        if numThongGio == 0 :
            executeThongGio = 1
            numThongGio = 1
                        
        elif numThongGio == -2 : #bat che do thong gio
            print("bat che do thong gio")
            linkFile = folderMP3 + "019.mp3"
            playmp3(linkFile)    
            #sent waiting de hien man hinh cho
            isWaiting = 1
            self.sentWaiting2AllClient()
            time.sleep(0.3)
            for i in range(1,numClientLeft+1):
                nameTu = "Left_"+str(i)
                byteKC = struct.pack('B',disAvgLeft*i)
                self.sendMes2Client(nameTu,b'\x1d\x1d\x01'+byteKC)
            for i in range(1,numClientRight+1):
                nameTu = "Right_"+str(i)
                byteKC = struct.pack('B',disAvgRight*i)
                self.sendMes2Client(nameTu,b'\x1d\x1d\x01'+byteKC)
            numThongGio = -3

        elif numThongGio == -3 : #tat de do thong gio
            linkFile = folderMP3 + "020.mp3"
            playmp3(linkFile)
            for i in range(1,numClientLeft+1):
                nameTu = "Left_"+str(i)
                byteKC = struct.pack('B',disAvgLeft*i)
                self.sendMes2Client(nameTu,b'\x1d\x1d\x00'+byteKC)
            for i in range(1,numClientRight+1):
                nameTu = "Right_"+str(i)
                byteKC = struct.pack('B',disAvgRight*i)
                self.sendMes2Client(nameTu,b'\x1d\x1d\x00'+byteKC)

            time.sleep(1)
            #sau khi thong gio xong gui lenh dong tu
            tuTraiPhai = 'A'
            dongMoTuFunction(0,0)
            numThongGio = 0
            executeThongGio = 0
            countThongGio = 60

    def sendTempOut(self):
        threadLock.acquire()
        temp = int(uart.dataReceved.tempOut * 10)
        humi = int(uart.dataReceved.humiOut * 10)
        daHT = struct.pack('H',temp) + struct.pack('H',humi)
        dtKC1={}
        dtkc={}
        for dt in dataReceivedSer:
            dtKC1[dt] = dataReceivedSer[dt].distanceSen_1
        for i in range(1,numClientLeft+1):
            nameTu = 'Left_'+str(i)
            if i == 1 :
                dtkc[nameTu] = dtKC1[nameTu]
            else :
                nameTuTruoc = 'Left_' + str(i-1)
                dtkc[nameTu] = dtKC1[nameTu] - dtKC1[nameTuTruoc]
            if dtkc[nameTu] < 0 :
                dtkc[nameTu] = 0

        for i in range(1,numClientRight+1):
            nameTu = 'Right_'+str(i)
            if i == 1 :
                dtkc[nameTu] = dtKC1[nameTu]
            else :
                nameTuTruoc = 'Right_' + str(i-1)
                dtkc[nameTu] = dtKC1[nameTu] - dtKC1[nameTuTruoc]
            if dtkc[nameTu] < 0 :
                dtkc[nameTu] = 0
            
        if len(daHT) == 4:
            for sock in allConnection:
                byteKC = struct.pack('H',dtkc[sock])
                allConnection[sock].send(b'\xda\xda' + daHT + byteKC)
        threadLock.release()
    
    def getNameOfTu(self, number):
        global myNumberTu , numClientLeft, numClientRight
        stt = number - myNumberTu
        if stt < 0 and (-stt) <= numClientLeft:
            nameTu = 'Left_' + str(-stt)
        elif stt > 0 and stt <= numClientRight:
            nameTu = 'Right_' +str(stt)
        else:
            nameTu='H'
        return nameTu
    
    def getStatusOfAllTu(self): #kiem tra trang thai cac tu truoc khi dong mo de qua trinh dong mo duoc toi uu nhat
        dtStatusAllTu = {}
        for tu in dataReceivedSer :
            dtStatusAllTu[tu] = dataReceivedSer[tu].statusMotor
        return dtStatusAllTu
    
    def checkTuCoVanHanhKhong(self):
        for tu in dataReceivedSer :
            if dataReceivedSer[tu].statusMotor == 1 or dataReceivedSer[tu].statusMotor == 3 or dataReceivedSer[tu].statusMotor == 6:
                return True #tu dang van hanh
        return False

    def sendDongMo(self,nameTu,dm): #gui lenh dong mo tu den client nao
        dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
        dataSent2Client[nameTu].dt2Pi2Ar[2] = dm #dong cac tu nho hon tu can mo
        self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))

    def checkHumen(self): #kiem tra so luong nguoi trong moi tu co thay doi ko neu co thay doi thong bao co nguoi vao tu
        isHumenIn=False
        for nameTu in dataReceivedSer:
            if dataReceivedSer[nameTu].numPersonOld < dataReceivedSer[nameTu].numPersonIn:
                isHumenIn=True
                dataReceivedSer[nameTu].numPersonOld = dataReceivedSer[nameTu].numPersonIn
                return nameTu,isHumenIn,dataReceivedSer[nameTu].numPersonIn
            else:
                dataReceivedSer[nameTu].numPersonOld = dataReceivedSer[nameTu].numPersonIn
        return "0",isHumenIn,0
    
    def doneExecute(self, ss):   # dong mo tu da xong gui lai cho cac client de xac nhan thoat form waiting
        global  isWaiting
        threadLock.acquire()
        if isWaiting == 1:# thoat do mo thanh cong ko co dung khan cap
            isWaiting = 0
            self.sentWaiting2AllClient() 
        threadLock.release()
        loggerInfor.info(ss)
        print(ss)

    def checkError(self,fileSound): #kiem tra su co gi truoc khi mo tu
        global isWaiting, statusSuCo, arraySuCo
        self.checkSuCo(True)
        threadLock.acquire()
        isWaiting = 3 #set co su co co nguoi trong tu va yeu cau dong mo tu
        threadLock.release()
        if statusSuCo == 1 :# co nguoi trong tu
            linkFile = folderMP3 + "008.mp3"
            playmp3(linkFile)
            return False
        elif statusSuCo == 4 :# co nguoi trong tu
            linkFile = folderMP3 + "015.mp3"
            playmp3(linkFile)
            return False
        elif statusSuCo == 5 :
            linkFile = folderMP3 + 'kdc_' + arraySuCo[4].split('_')[1] + '.mp3'
            playmp3(linkFile)
            return False

        if len(fileSound) > 0:
            linkFile = folderMP3 + fileSound
            playmp3(linkFile)
        return True
#tao ra 1 thread client khi co 1 client ket noi den server
class ListenClientThread(threading.Thread,DongMoTu):
    def __init__(self,idThreadIP,connection,soTu):
        threading.Thread.__init__(self)
        self.threadIP = idThreadIP
        self.connection = connection
        self.tu = soTu
        self.numberOfTu = int(soTu.split('_')[1]) #Left_1
        self.daemon = True

    def run(self):
        "thread nay co nhiem vu chinh la lang nghe du lieu tu client gui den server"
        sLog = self.tu + " ClientThread is running"
        print(sLog)
        global isWaiting,tuTraiPhai, haveSucoClient, isFlag2906, caseBD,checkBDok
        while isListenCL:
            try:
                data = self.connection.recv(2)
                if not data :
                    self.connection.close()
                    sLog = "ListenClientThread-mat ket noi voi  " + self.threadIP
                    print(sLog)
                    if self.tu in allConnection:
                        del allConnection[self.tu]
                else :
                    if len(data) == 2 and data[0] == 0xAA and data[1] == 0xAA: #nhan 30byte data cua client
                        data = self.connection.recv(30)
                        if len(data) == 30 :
                            if isFlag2906 == False and data[29] == 0x06 :
                                "cho den khi client "
                                dataReceivedSer[self.tu].setData(data)
                            elif isFlag2906 :
                                dataReceivedSer[self.tu].setData(data)
                            
                            if data[29] == 0x05 and isFlag2906 and isWaiting != 1:
                                "trong trang thai binh thuong khong van hanh neu co isFlag2906 = true ma data[29] =0x05 thi co su co "
                                haveSucoClient = True

                    #receive data setting from Client sent to server
                    elif len(data) == 2 and data[0] ==0xbb and data[1] == 0xbb : #data setting cuar client
                        data = self.connection.recv(8)
                        if len(data) == 8:
                            dataSent2Client[self.tu].setData(data)
                            #print(self.tu + " CLIENT SENT 0xBBBB--datasetting")
                    
                    elif len(data) == 2 and data[0] == 0xef and data[1] == 0xed: #dung khan cap sent all dung khan cap
                        print("client gui lenh dung khan cap", self.tu)
                        isWaiting = 2

                    elif len(data) == 2 and data[0] == 0xee and data[1] == 0xee: #mo tu
                        if isWaiting == 0:
                            #khi dang dong khan cap thi ko mo tu
                            print("client yeu cau mo tu ",self.tu)
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(1,self.tu)

                        elif isWaiting == 2 :
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(2,self.tu) #mo tu tong quat

                    elif len(data) == 2 and data[0] == 0xee and data[1] == 0xff: #ddong tu
                        print("client yeu cau dong tu ", self.tu)
                        if isWaiting != 1 :
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(0,0)
                    
                    elif len(data) == 2 and data[0] == 0xcb and data[1] == 0xcb: #kiem tra su co da duoc gia quyet xong
                        print("receive checkDone SuCo tu client")
                        self.DoneSuCo(True)
                    elif len(data) == 2 and data[0] == 0xbd and data[1] == 0xbd: #trong che do bao duong an tiep tuc
                        caseBD +=1
                    
                    elif len(data) == 2 and data[0] == 0xbd and data[1] == 0xbc: #trong che do bao duong bao phan hoi OK
                        checkBDok = True
                    
                    elif len(data) == 2 and data[0] == 0xcc: #cac thao tac vuot man hinh client gui len
                        
                        if data[1] == 0xc2 : # xuong dong toan bo gia ca 2 phia
                            tuTraiPhai = 'A'
                            dongMoTuFunction(0,0)
                        elif data[1] == 0xc3 : # len bat tat thong gio
                            self.thongGioFuction()
                        elif (data[1] == 0xc0 and self.tu[0] == 'L') or (data[1] == 0xc1 and self.tu[0] == 'R'): #neu vuot phai tu trai vuot trai tu phai- thi mo o ben canh
                            if(self.tu[0]=='L' and self.numberOfTu == numClientLeft) or (self.tu[0]=='R' and self.numberOfTu == numClientRight):
                                tuTraiPhai = self.tu[0]
                                dongMoTuFunction(0,0)
                            else: #tu ben canh van co de mo
                                if dataReceivedSer[self.tu].statusMotor == 4: # neu dang dong thi thoi ko lam gi nua
                                    pass
                                else:
                                    nameTu = self.tu.split('_')[0]+ '_' + str(int(self.numberOfTu + 1))
                                    tuTraiPhai = nameTu[0]
                                    if isWaiting == 0:
                                        dongMoTuFunction(1,nameTu)
                                    elif isWaiting == 2 :
                                        dongMoTuFunction(2,nameTu) #mo tu tong quat

                        elif (data[1] == 0xc1 and self.tu[0] == 'L') or (data[1] == 0xc0 and self.tu[0] == 'R'): #vuot trai+tu trai  hoac vuotPhai+tuPhai se mo tu do
                                print(self.tu + " vuot trai")
                                tuTraiPhai = self.tu[0]
                                if isWaiting == 0 :
                                    dongMoTuFunction(1,self.tu)
                                elif isWaiting == 2 :
                                    dongMoTuFunction(2,self.tu) #mo tu tong quat
            
            except Exception as e:
                self.connection.close()
                print("len(allConnection) = ", len(allConnection))
                if self.tu in allConnection:
                    del allConnection[self.tu]
                print(str(e))
                break
        
#thread server lang nghe ket noi tu client
class ServerThreadMain(threading.Thread,DongMoTu):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
    def run(self): 
        global isListenCL
        self.soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #self.soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.soc.bind((IPSERVER, PORT))
        self.soc.listen(50)

        print("socket is running")
        while isListenCL:
            conn, addr = self.soc.accept()
            ip, port = str(addr[0]), str(addr[1])
            print('Accepting connection from ',ip ,':',port)
            #creat 1 thread danh ring cho client vua ket noi den
            Tu=""
            for tu in arrIPArrdressLeft :
                if arrIPArrdressLeft[tu] == ip :
                    Tu = tu
                    break
            for tu in arrIPArrdressRight :
                if arrIPArrdressRight[tu] == ip :
                    Tu = tu
                    break

            if len(Tu) > 2 :
                    allConnection[Tu]=conn
                    newClient = ListenClientThread(ip,conn,Tu)
                    newClient.start()
                    #neu client ket noi den ma server dang co user login thi gui OK de client vao main
                    if userLogin :
                        conn.send(b'OK')
                    time.sleep(0.05)
                    #gettime and send it to client
                    H = strftime("%H")
                    M = strftime("%M")
                    S = strftime("%S")
                    d = strftime("%d")
                    m = strftime("%m")
                    Y = strftime("%Y")
                    dstr = Y+m+d+H+M+S #20171620092018  destr = dbyte.decode()
                    dbyte = b'\xfa\xfa' + dstr.encode()
                    conn.send(dbyte)
                    #self.sendDate2Client()
            else : 
                conn.close()
                print("CLIENT's IP not in setup")
    def stop(self):
        for con in allConnection:
            allConnection[con].close()
            del allConnection[con]
        self.running = False
        self.soc.close()

#thread dung de mo tu
class OpenTuThread(threading.Thread,DongMoTu):

    def __init__(self,numTu):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.numTu = numTu #ex:: Left_1 Right_2
        self.daemon = True
        
    def run(self):
        global isWaiting,tuActive,haveSucoClient , isGetDataFromClient, isFlag2906,tuOpenedLeft,tuOpenedRight
        #kiem tra xem xtu da duoc mo hay chưa
        
        threadLock.acquire()
        self.checkTuisOpened()
        if tuOpenedLeft == self.numTu or tuOpenedRight == self.numTu:
            #neu tu nay dang mo roi thi thoi ko phai mo nua
            print("Tu Da Duoc Mo ", self.numTu)
            threadLock.release()
            return 
        threadLock.release()
        fileSound = 'mkg_' + str(converNameTu(self.numTu)) + '.mp3'
        if self.checkError(fileSound) == False :
            return
        #reset bien 
        threadLock.acquire()
        isWaiting = 1
        isFlag2906 = False
        isGetDataFromClient = False
        haveSucoClient = False
        self.sentWaiting2AllClient()
        #cho cho den khi nhan duoc trang thai cua tat ca cac client la ok se sap dong  mo
        isGetDataFromClient =True
        threadLock.release()
        print("start waiting")
        while self.waitingData_29_06() :
            if self.stopped:
                return
        time.sleep(self.timeSleepp)

        #send open tu
        if self.openTuLeft() == False :
            return
        self.doneExecute("Tủ " + str(self.numberTu) + " Mở")
        tuActive = self.numTu
        
    def openTuLeft(self):
        global isWaiting, tuOpenedLeft, tuTraiPhai,tuOpenedRight
        self.numberTu = int(self.numTu.split('_')[1])
        firstName = self.numTu.split('_')[0] + '_'
        #check tu nao dang mo
        if (firstName[0]=='L' and tuOpenedLeft != "0") or (firstName[0]=='R' and tuOpenedRight != "0") :#"co tu dang mo"
            if firstName[0]=='L' :
                numberTuOpened = int(tuOpenedLeft.split('_')[1])
            else:
                numberTuOpened = int(tuOpenedRight.split('_')[1])

            if self.numberTu < numberTuOpened :#"tu muon mo co nho hon tu dang mo ko?? neu co thi mo"
                tuK = numberTuOpened - 1
                while tuK >= self.numberTu :    
                    nameTu = firstName + str(tuK)
                    self.sendDongMo(nameTu, 0x01) # mo cac tu lon hon tu can mo
                    tuK-=1
                    if isWaiting == 2 :
                        return False
                    time.sleep(self.timeDelayTu)
            else : #"tu muon mo lon hon tu dang mo thi dong "
                tuK = numberTuOpened
                while tuK < self.numberTu :    
                    nameTu = firstName + str(tuK)
                    self.sendDongMo(nameTu,0x02)
                    tuK+=1
                    if isWaiting == 2 : 
                        return False
                    time.sleep(self.timeDelayTu)
        else: #"ko co tu nao dang mo tat ca cac tu deu dong"
            if firstName[0]=='L' :
                tuK = numClientLeft
            else :
                tuK = numClientRight
            while tuK >= self.numberTu :    
                nameTu = firstName + str(tuK)
                self.sendDongMo(nameTu,0x01)
                tuK-=1
                if isWaiting == 2 : 
                    return False
                time.sleep(self.timeDelayTu)
        #waiting cac tu dong xong
        print('cho he thong van hanh xong')
        while self.checkTuCoVanHanhKhong() :
            if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                return False
        time.sleep(self.timeMiliSecond)
        return True

class MoTuTongQuat(threading.Thread,DongMoTu):
    def __init__(self,numTu,isCheckingError):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.daemon = True
        self.numTu = numTu
        self.isCheckedError = isCheckingError

    def run(self):
        global isWaiting,  haveSucoClient , isGetDataFromClient, isFlag2906,tuActive
        if self.isCheckedError :
            fileSound = 'mkg_' + str(converNameTu(self.numTu)) + '.mp3'
            if self.checkError(fileSound) == False : 
                return
        threadLock.acquire()
        #send wating form
        isWaiting = 1
        isFlag2906 = False
        isGetDataFromClient = False
        haveSucoClient = False
        self.sentWaiting2AllClient()
        #cho cho den khi nhan duoc trang thai cua tat ca cac client la ok se sap dong  mo
        isGetDataFromClient =True
        threadLock.release()
        print("start waiting")
        while self.waitingData_29_06() :
            if self.stopped :
                return
        #send open tu
        if self.openTuLeft() == False :
            return 
        self.doneExecute("Tủ " + str(self.numberTu) + " Mở")
        tuActive = self.numTu
    
    def openTuLeft(self):
        "mo cac tu ben trai - mo tu numberTu "
        global isWaiting,tuTraiPhai
        #check tu nao dang mo
        self.numberTu = int(self.numTu.split('_')[1])
        tuDauClose = 1 
        tuKClose = 1
        if tuTraiPhai == 'L':
            firstName = 'Left_'
            tuDauOpen = numClientLeft
        elif tuTraiPhai == 'R':
            firstName = 'Right_'
            tuDauOpen = numClientRight
        else :
            print("MO tu tong quat FAILE tuTraiPhai = ", tuTraiPhai)
            return False
        tuKOpen = tuDauOpen
        flagLoop = True
        #gui du lieu den cac tu 
        while flagLoop:
            flagLoop = False
            if tuKClose < self.numberTu :#Dong cac tu nho hon tu can mo
                flagLoop = True
                nameTu = firstName + str(tuKClose)
                self.sendDongMo(nameTu,0x02)
                tuKClose +=1
            if tuKOpen >= self.numberTu : # Mo cac tu lon hon tu can mo
                flagLoop = True
                nameTu = firstName + str(tuKOpen)
                self.sendDongMo(nameTu,0x01)
                tuKOpen -=1
            if (isWaiting == 2 and self.isCheckedError) or self.stopped :
                return False
            time.sleep(self.timeDelayTu)
        #waiting cac tu dong xong
        while self.checkTuCoVanHanhKhong() :
            if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                return False
        return True

class MoCaHaiPhiaTongQuat(threading.Thread,DongMoTu): #de mo 2 tu gan master khi co chay tai master
    def __init__(self,numTu,isCheckingError):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.daemon = True
        self.numTu = numTu
        self.isCheckedError = isCheckingError
        
    def run(self):
        global isWaiting,  haveSucoClient , isGetDataFromClient, isFlag2906,statusSuCo,tuActive
        if self.isCheckedError :
            print("---OPEN START---bat dau thuc hien luong mo tu tong quat")
            if self.checkError("") == False : 
                return
        threadLock.acquire()
        #send wating form
        isWaiting = 1
        isFlag2906 = False
        isGetDataFromClient = False
        haveSucoClient = False
        self.sentWaiting2AllClient()
        #cho cho den khi nhan duoc trang thai cua tat ca cac client la ok se sap dong  mo
        isGetDataFromClient =True
        threadLock.release()
        print("start waiting")
        while self.waitingData_29_06() :
            if self.stopped :
                return
        time.sleep(self.timeSleepp)
        #send open tu
        if self.openTuLeft() == False :
            return 
        self.doneExecute("Tủ " + str(self.numberTu) + " Mở")
        
    def openTuLeft(self):
        "mo cac tu ben trai - mo tu numberTu "
        global isWaiting
        #check tu nao dang mo
        self.numberTu = int(self.numTu.split('_')[1])
        tuDauClose_Left , tuDauClose_Right = 1 , 1 
        tuNowClose_Left , tuNowClose_Right = 1 , 1
        tuDauOpen_Left , tuDauOpen_Right = numClientLeft, numClientRight
        tuNowOpen_Left , tuNowOpen_Right = numClientLeft , numClientRight
        firstName_Left , firstName_Right = 'Left_' , 'Right_'
        flagLoop = True
        #gui du lieu den cac tu 
        while flagLoop:
            flagLoop = False
            #Dong cac tu nho hon tu can mo
            if tuNowClose_Left < self.numberTu and self.numberTu <= numClientLeft:
                flagLoop = True
                nameTu = firstName_Left + str(tuNowClose_Left)
                self.sendDongMo(nameTu,0x02)
                tuNowClose_Left +=1
            if tuNowClose_Right < self.numberTu and self.numberTu <= numClientRight :
                flagLoop = True
                nameTu = firstName_Right + str(tuNowClose_Right)
                self.sendDongMo(nameTu,0x02)
                tuNowClose_Right +=1

            if tuNowOpen_Left >= self.numberTu and self.numberTu <= numClientLeft :
                flagLoop = True
                nameTu = firstName_Left + str(tuNowOpen_Left)
                self.sendDongMo(nameTu,0x01)
                tuNowOpen_Left -=1
            if tuNowOpen_Right >= self.numberTu and self.numberTu <= numClientRight :
                flagLoop = True
                nameTu = firstName_Right + str(tuNowOpen_Right)
                self.sendDongMo(nameTu,0x01)
                tuNowOpen_Right -=1
                
            if isWaiting == 2 and self.isCheckedError :
                return False
            time.sleep(self.timeDelayTu)
        #gui xong la xong khong cho gi nua
        return True

#thread dung de dong tu version 2
class CloseTuThreadVer2(threading.Thread,DongMoTu):
    def __init__(self, isCheckError):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.daemon=True
        #bien kiem tra xem co can check su co de dong tu khong
        self.isCheckedError = isCheckError

    def run(self) : 
        global isWaiting,haveSucoClient, isGetDataFromClient, isFlag2906,statusSuCo, tuTraiPhai, doneDongTuLanDau
        self.dtStatusAllTu = self.getStatusOfAllTu()
        print("Start Dong TU")
        if self.isCheckedError : # neu co kiem tra dieu kien
            if tuTraiPhai == 'A':
                fileSound = '005.mp3'
            else :
                fileSound = '004.mp3'

            if self.checkError(fileSound) == False : #neu dieu kien khong thoa man
                return 
            threadLock.acquire()
            isGetDataFromClient = False
            #send wating form
            isFlag2906 = False
            isWaiting = 1
            self.sentWaiting2AllClient()
            #cho cho den khi nhan duoc trang thai cua tat ca cac client la ok se sap dong  mo
            isGetDataFromClient = True
            haveSucoClient = False
            threadLock.release()
            print("---waiting 06")
            while self.waitingData_29_06() :
                if self.stopped:
                    return
            time.sleep(self.timeSleepp)
            print("+++Done waiting 06")
        if doneDongTuLanDau :
            if  self.closeTuLeft() == False : #chua dong tu xong
                return
        else :
            if  self.closeTuLanDau() == False : #chua dong tu xong
                return
        if self.isCheckedError :
            self.doneExecute("Dong Tu")


    def closeTuLeft(self):
        global numClientLeft,numClientRight, isWaiting, dataReceivedSer, tuTraiPhai
        tuKLeft , tuKRight= 1, 1
        flagDongTuLeft , flagDongTuRight = True , True
        print("close tu start--", tuTraiPhai)
        #kiem tra cac tu gan master dong roi thi thoi ko phai gui lenh dong nua
        while flagDongTuLeft or flagDongTuRight:
            if flagDongTuLeft:
                nameTu = 'Left_'+ str(tuKLeft)
                if self.dtStatusAllTu[nameTu] == 4 :
                    tuKLeft+=1
                    if tuKLeft > numClientLeft : flagDongTuLeft = False
                else :
                    flagDongTuLeft = False
            if flagDongTuRight:
                nameTu = 'Right_'+ str(tuKRight)
                if self.dtStatusAllTu[nameTu] == 4 :
                    tuKRight+=1
                    if tuKRight > numClientRight: flagDongTuRight = False
                else :
                    flagDongTuRight = False
        #dong cac tu chua dong
        flagDongTuLeft = True
        while flagDongTuLeft :  
            flagDongTuLeft = False
            if tuKLeft <= numClientLeft and (tuTraiPhai == 'A' or tuTraiPhai =='L') :
                nameTu = "Left_" + str(tuKLeft) 
                self.sendDongMo(nameTu,0x02)
                tuKLeft+=1
                flagDongTuLeft = True
            if  tuKRight <= numClientRight and (tuTraiPhai == 'A' or tuTraiPhai =='R') :
                nameTu = "Right_" + str(tuKRight)
                self.sendDongMo(nameTu,0x02)
                tuKRight+=1
                flagDongTuLeft = True
            if isWaiting == 2 and self.isCheckedError : #neu waiting==2(dung khan cap) trong truong hop co kiem tra su co
                    return False
            if flagDongTuLeft: time.sleep(self.timeDelayTu)
        #waiting cac tu dong xong
        while self.checkTuCoVanHanhKhong() :
            if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                return False
        time.sleep(self.timeMiliSecond)
        return True

    def closeTuLanDau(self):
        global numClientLeft,numClientRight, isWaiting, dataReceivedSer, doneDongTuLanDau
        tuKLeft , tuKRight, tuDauLeft, tuDauRight = 1, 1 , 1, 1
        flagDongTu = True
        while flagDongTu :
            flagDongTu = False
            if tuKLeft <= numClientLeft :  
                flagDongTu = True
                nameTu = "Left_" + str(tuKLeft) 
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
                if tuKLeft == tuDauLeft : # khong gui lenh dong tu khong check cam bien cho tuDau
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00
                else :
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x01 # 01 dong tu binh thuong(khong check cam bien) 0x00 dong tu check cam bien)
                
                self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                tuKLeft+=1
            if tuKRight <= numClientRight :  
                flagDongTu = True
                nameTu = "Right_" + str(tuKRight) 
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
                if tuKRight == tuDauRight : # khong gui lenh dong tu khong check cam bien cho tuDau
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00
                else :
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x01 # 01 dong tu binh thuong(khong check cam bien) 0x00 dong tu check cam bien)
                self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                tuKRight+=1

            if isWaiting == 2 and self.isCheckedError :
                return False
            time.sleep(self.timeSleepp)
        #cho tu dau dong xong thi gui lenh check cam bien cho tu tiep theo
        while tuDauLeft < numClientLeft or  tuDauRight < numClientRight :
            nameTu = "Left_" + str(tuDauLeft) 
            if tuDauLeft < numClientLeft and dataReceivedSer[nameTu].statusMotor == 4 :
                tuDauLeft += 1
                nameTu = "Left_" + str(tuDauLeft) 
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
                dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00
                self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))

            nameTu = "Right_" + str(tuDauRight) 
            if tuDauRight < numClientRight and dataReceivedSer[nameTu].statusMotor == 4 :
                tuDauRight += 1
                nameTu = "Right_" + str(tuDauRight) 
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
                dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00
                self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))

            if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                return False
            time.sleep(self.timeMiliSecond)
        #waiting cac tu dong xong
        while self.checkTuCoVanHanhKhong() :
            if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                return False
        doneDongTuLanDau = True        
        return True
     
def dongMoTuFunction(inCase,numTu) :
    global threadDongMoTu,tuActive
    tuActive = '0'
    if threadDongMoTu != None:
        threadDongMoTu.stopped = True
        threadDongMoTu.join()
        threadDongMoTu = None

    if threadDongMoTu == None:
        if inCase == 0: # dong tu
            if numTu == 0:
                threadDongMoTu = CloseTuThreadVer2(True)#co kiem tra cam bien
            else : 
                threadDongMoTu = CloseTuThreadVer2(False)# khong kiem tra cam bien
            threadDongMoTu.start()
        elif inCase == 1 :# mo tu
            threadDongMoTu = OpenTuThread(numTu)
            threadDongMoTu.start()
        elif inCase == 2:
            threadDongMoTu = MoTuTongQuat(numTu,True)#co kiem tra cam bien
            threadDongMoTu.start()
        elif inCase == 3:
            threadDongMoTu = MoTuTongQuat(numTu,False)#khong kiem tra cam bien
            threadDongMoTu.start()
        elif inCase == 4 :
            threadDongMoTu = MoCaHaiPhiaTongQuat(numTu,False)#khong kiem tra cam bien
            threadDongMoTu.start()

def converNameTu(nameTu):# Left_3 Right_2 
    global myNumberTu
    numberTu = int(nameTu.split('_')[1])
    if nameTu[0] == 'L': #tu ben trai
        numberTu = myNumberTu - numberTu
    else:
        numberTu = myNumberTu + numberTu
    return numberTu

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
    s=''
    for tu in dataReceivedSer:
        # 22:05 1 23 22 24 24
        s += H + ':' + M + ' ' + str(converNameTu(tu)) + " "+str(dataReceivedSer[tu].tempIn )+" " +str(dataReceivedSer[tu].humiIn )+" "+str(uart.dataReceved.tempOut )+ " "+str(uart.dataReceved.humiOut )+'\n'
    s +=  H + ':' + M + ' ' + str(myNumberTu) + " "+str(dataReceivedSer[tu].tempIn )+" " +str(dataReceivedSer[tu].humiIn )+" "+str(uart.dataReceved.tempOut )+ " "+str(uart.dataReceved.humiOut )+'\n'
    file.write(s) 
    file.close()

def InitData():
    #khoi tao cac mang lu gia tri gui di va data nhan ve cho cac client ben trai va ben phai
    for i in range(1,numClientLeft+1):
        obj = DataInforSer()
        dataReceivedSer["Left_"+str(i)] = obj
        obj2 = DataSent2Client()
        dataSent2Client["Left_"+str(i)] = obj2

    for i in range(1,numClientRight+1):
        obj = DataInforSer()
        dataReceivedSer["Right_"+str(i)] = obj
        obj2 = DataSent2Client()
        dataSent2Client["Right_"+str(i)] = obj2

def playmp3(nameFile):
    try:
        mixer.music.load(nameFile)
        mixer.music.play()
        #phan gui play sound cho cac tu client
        lent = len(nameFile)
        filemp3 = nameFile[lent-7 : lent-4]
        for sock in allConnection:
            allConnection[sock].send(b'\x10\x0a' +filemp3.encode() )#sent stop

    except Exception as e :
        print("error in playmp3" + str(e))

#check usb cua dieu va va van tay
def checkComVanTay():
    global usbFinger, usbDieuHoa
    import serial 
    try :
        ser = serial.Serial(
            port = usbDieuHoa,
            baudrate = 9600,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 1
        )
        print("Innit ok")
        dataSent = b'\xaa\xaa'
        ser.write(dataSent)
        ser.flush()
        dt = ser.read(3)
        print(dt)
        if len(dt) == 3 and dt[0] == 0x41 and dt[1] == 0x43 and dt[2] == 0x4b:
            pass
        else :
            print("change port")
            tempUSB = usbDieuHoa
            usbDieuHoa =  usbFinger
            usbFinger = tempUSB
        ser.close()
    except Exception as e:
        print("Exception in InitUSB : ",e)
#check cam bien van tay ngay khi van hanh de doi cong com
thCheckVanTay = threading.Thread(target=checkComVanTay)
thCheckVanTay.start()

InitData()
#print(dataSent2Client)
serverMain = ServerThreadMain()
serverMain.start()
