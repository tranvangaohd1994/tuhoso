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
# Third file logger
temp_logger = setup_logger('temp_log', '/home/pi/Desktop/temp.log')

#giao dien
isFullScreen = False
isFullSceen = False
# bien kiem tra xem tu nao dang duoc mo
tuOpenedRight = "0" 
tuOpenedLeft = "0"
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
debugg = True
#caseBaoDuong
caseBD = 0
checkBDok = False

statusSuCo = 0
#mang de kiem tra xem su co thuoc loai nao 0-co nguoi trong tu 1-chay trong 2-chay ngoai 3-gia sach nho co vat can
arraySuCo = ['0','0','0','0'] 
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

    def checkSuCo(self,ishuman):
        "ham kiem tra co su co hay khong truoc khi van hanh va kiem tra theo timer"
        global statusSuCo,isWaiting, tuTraiPhai
        threadLock.acquire()
        #reset mang su co
        statusSuCo = 0
        for i in range(4):
            arraySuCo[i] = '0'
            
        for dt in dataReceivedSer:
            if tuTraiPhai == 'A' or  tuTraiPhai == dt[0] : #chi check tu ben trai hoac ben phai
                if dataReceivedSer[dt].fireSenOut == 1 :
                    statusSuCo = 3 # bao chay ngoai
                    arraySuCo[2] = dt
                    msg = str(dt) + " có cháy ngoài"
                    suCo_logger.error(msg)
                if dataReceivedSer[dt].fireSenIn == 1:
                    arraySuCo[1] = dt
                    statusSuCo = 2 #== la bao chay trong
                    msg = str(dt) + " có cháy trong"
                    suCo_logger.error(msg)
                
                if dataReceivedSer[dt].numPersonIn == 1 :
                    statusSuCo = 1 # co nguoi trong tu
                    arraySuCo[0] = dt
                    msg = str(dt) + " có người trong tủ"
                    suCo_logger.error(msg)
                    break
                if dataReceivedSer[dt].infrared_1 == 1 or dataReceivedSer[dt].infrared_2 != 0 or dataReceivedSer[dt].infrared_3 != 0 or dataReceivedSer[dt].infrared_4 != 0 : 
                    statusSuCo = 4 #gia sach nho co vat can
                    arraySuCo[3] = dt 
                    msg = str(dt) + " giá sách nhô có vật cản"
                    suCo_logger.error(msg)


        if statusSuCo != 0 or (statusSuCo == 0 and isWaiting == 0): # isWaiting == 0 tuc la ko trong qua trinh van hanh
            byteSuCo = struct.pack('bb',statusSuCo,isWaiting)
            for sock in allConnection:
                allConnection[sock].send(b'\xcb\xcb'+byteSuCo)#sent waiting
        threadLock.release()
        return statusSuCo
    
    def DoneSuCo(self,isPut):
        "kiem tra khong con su co nao nua"
        global statusSuCo,isWaiting
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
        flagActive = True
        for dt in dataReceivedSer:
            if dataReceivedSer[dt].statusMotor == 2 :
                if dt[0] == 'L' :
                    tuOpenedLeft = dt
                elif dt[0] == 'R' :
                    tuOpenedRight = dt
                flagActive = False
                print("SERVER change tu active =",tuOpenedLeft)
        if flagActive :
            tuOpenedLeft = "0"
            tuOpenedRight = '0'
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

    def ConfigChieuQuayDC(self,spinLeftIsChecked):
       
        for i in range(1,numClientLeft+1):
            nameTu = "Left_"+str(i)
            if spinLeftIsChecked == True:
                dataSent2Client[nameTu].dt2Pi2Ar[1] = 0x02
            else :
                dataSent2Client[nameTu].dt2Pi2Ar[1] = 0x01
            self.sendMes2Client(nameTu,b'\xee\xee'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
        
        for i in range(1,numClientRight+1):
            nameTu = "Right_"+str(i)
            if spinLeftIsChecked == True:
                dataSent2Client[nameTu].dt2Pi2Ar[1] = 2
            else :
                dataSent2Client[nameTu].dt2Pi2Ar[1] = 1

            self.sendMes2Client(nameTu,b'\xee\xee'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
       
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
      
#tao ra 1 thread client khi co 1 client ket noi den server
class ListenClientThread(threading.Thread,DongMoTu):
    def __init__(self,idThreadIP,connection,soTu):
        threading.Thread.__init__(self)
        self.threadIP = idThreadIP
        self.connection = connection
        self.tu = soTu
        self.daemon = True

    def run(self):
        "thread nay co nhiem vu chinh la lang nghe du lieu tu client gui den server"
        sLog = self.tu + " ClientThread is running"
        print(sLog)
        global isWaiting,tuTraiPhai, haveSucoClient,tuOpenedLeft,tuOpenedRight, isFlag2906, caseBD,checkBDok
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
                    if len(data) == 2 and data[0] == 0xAA and data[1] == 0xAA:
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
                                print("haveSuCoClient = True ", self.tu)
                            elif data[29] == 0x02:
                                tuOpenedLeft = self.tu

                    #receive data setting from Client sent to server
                    elif len(data) == 2 and data[0] ==0xbb and data[1] == 0xbb :
                        data = self.connection.recv(8)
                        if len(data) == 8:
                            dataSent2Client[self.tu].setData(data)
                            #print(self.tu + " CLIENT SENT 0xBBBB--datasetting")
                    elif len(data) == 2 and data[0] == 0xef and data[1] == 0xed:
                        #dung khan cap sent all dung khan cap
                        print("client gui lenh dung khan cap")
                        isWaiting = 2

                    elif len(data) == 2 and data[0] == 0xee and data[1] == 0xee:
                        #mo tu
                        if isWaiting == 0:
                            #khi dang dong khan cap thi ko mo tu
                            print("client yeu cau mo tu ",self.tu)
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(1,self.tu)

                        elif isWaiting == 2 :
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(2,self.tu) #mo tu tong quat

                    elif len(data) == 2 and data[0] == 0xee and data[1] == 0xff:
                        #ddong tu
                        print("client yeu cau dong tu ", self.tu)
                        if isWaiting != 1 :
                            tuTraiPhai = self.tu[0]
                            dongMoTuFunction(0,0)
                    elif len(data) == 2 and data[0] == 0xcb and data[1] == 0xcb:
                        #kiem tra su co da duoc gia quyet xong
                        print("receive checkDone SuCo tu client")
                        self.DoneSuCo(True)
                    elif len(data) == 2 and data[0] == 0xbd and data[1] == 0xbd:
                        caseBD +=1
                    elif len(data) == 2 and data[0] == 0xbd and data[1] == 0xbc:
                        checkBDok = True

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
    def CheckError(self):
        global isWaiting,  haveSucoClient , isGetDataFromClient, isFlag2906,statusSuCo,tuOpenedLeft
        print("Start OpenTuThread")
        self.checkSuCo(True)
        threadLock.acquire()
        self.checkTuisOpened()
        if tuOpenedLeft == self.numTu or tuOpenedRight == self.numTu:
            #neu tu nay dang mo roi thi thoi ko phai mo nua
            threadLock.release()
            print("Tu Da Duoc Mo ", self.numTu)
            return False
        #co nguoi trong tu hoac co vat can thi ko cho dong mo tu
        if  statusSuCo == 1 :# co nguoi trong tu
            linkFile = folderMP3 + "008.mp3"
            playmp3(linkFile)
            isWaiting = 3 #co su co khi van hanh
            threadLock.release()
            return False
        elif statusSuCo == 4 :# co vat can
            linkFile = folderMP3 + "015.mp3"
            playmp3(linkFile)
            isWaiting = 3 #co su co khi van hanh
            threadLock.release()
            return False

        linkFile = folderMP3 + "004.mp3"
        playmp3(linkFile)
        #reset bien 
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
                return False
        time.sleep(self.timeSleepp)
        return True

    def run(self):
        global isWaiting
        if self.CheckError() == False :
            return
        #send open tu
        if self.openTuLeft() == False :
            return

        threadLock.acquire()
        if isWaiting == 1:# thoat do mo thanh cong ko co dung khan cap
            isWaiting = 0
            self.sentWaiting2AllClient() 
        threadLock.release()
        ss = "Tủ " + str(self.numberTu) + " Mở"
        loggerInfor.info(ss)
        
    def openTuLeft(self):
        global isWaiting, tuOpenedLeft, tuTraiPhai,tuOpenedRight
        self.numberTu = int(self.numTu.split('_')[1])
        firstName = self.numTu.split('_')[0] + '_'
        print(firstName)
        #check tu nao dang mo
        if (firstName[0]=='L' and tuOpenedLeft != "0") or (firstName[0]=='R' and tuOpenedRight != "0") :
            "co tu dang mo"
            numberTuOpened = int(tuOpenedLeft.split('_')[1])
            print("Tu open la ", tuOpenedLeft )
            if self.numberTu < numberTuOpened :
                "tu muon mo co nho hon tu dang mo ko?? neu co thi mo"
                tuDau = numberTuOpened - 1
                tuK = tuDau
                while tuK >= self.numberTu :    
                    nameTu = firstName + str(tuK)
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
                    dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x01 # mo cac tu lon hon tu can mo
                    self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                    tuK-=1
                    if isWaiting == 2 :
                        return False
                    time.sleep(self.timeMiliSecond)

                #cho cac tuDau mo xong thi  
                while tuDau >= self.numberTu:
                    nameTu = firstName + str(tuDau)
                    #cho den khi nao tuDau mo xong hoac dong xong ( phong tru truong hop ko bat duoc mo thi dong)
                    while dataReceivedSer[nameTu].statusMotor != 2 :
                        if self.stopped or isWaiting != 1:
                            return False
                    #tang tu dau len 1 tu tiep theo
                    tuDau -= 1
                    if tuDau <  self.numberTu :
                        break
                    time.sleep(self.timeMiliSecond)
                return True

            else :
                "tu muon mo co nho hon tu dang mo ko?? neu co thi mo neu lon hon thi dong "
                tuDau = numberTuOpened
                tuK = tuDau

                while tuK < self.numberTu :    
                    nameTu = firstName + str(tuK)
                    dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
                    dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02 #dong cac tu nho hon tu can mo
                    self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                    tuK+=1
                    if isWaiting == 2 : 
                        return False
                    time.sleep(self.timeMiliSecond)

                #cho cac tu dong
                while tuDau < self.numberTu:
                    nameTu = firstName + str(tuDau) 
                    #cho den khi nao tuDau dong xong status == 4 
                    while dataReceivedSer[nameTu].statusMotor != 4 :
                        if self.stopped or isWaiting != 1:
                            return False
                    #tang tu dau len 1 tu tiep theo
                    tuDau += 1
                    if tuDau >=  self.numberTu :
                        break
                    time.sleep(self.timeMiliSecond)
                return True
        else:
            "ko co tu nao dang mo tat ca cac tu deu dong"
            if firstName[0]=='L' :
                tuK = numClientLeft
            else :
                tuK = numClientRight
            tuDau = tuK
            while tuK >= self.numberTu :    
                nameTu = firstName + str(tuK)
                dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x01 # mo cac tu lon hon tu can mo
                self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                tuK-=1
                if isWaiting == 2 : 
                    return False
                time.sleep(self.timeMiliSecond)

            #cho cac tuDau mo xong thi  
            while tuDau >= self.numberTu:
                nameTu = firstName + str(tuDau) 
                #cho den khi nao tuDau mo xong hoac dong xong ( phong tru truong hop ko bat duoc mo thi dong)
                while dataReceivedSer[nameTu].statusMotor != 2 :
                    if self.stopped or isWaiting != 1:
                        return False
                #tang tu dau len 1 tu tiep theo
                tuDau -= 1
                if tuDau <  self.numberTu :
                    break
            return True

class MoTuTongQuat(threading.Thread,DongMoTu):
    def __init__(self,numTu,isCheckingError):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.daemon = True
        self.numTu = numTu
        self.isCheckedError = isCheckingError
        
    def checkError(self):
        global isWaiting,  haveSucoClient , isGetDataFromClient, isFlag2906,statusSuCo
        print("---OPEN START---bat dau thuc hien luong mo tu tong quat")
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

        linkFile = folderMP3 + "004.mp3"
        playmp3(linkFile)
        
        return True

    def run(self):
        global isWaiting,  haveSucoClient , isGetDataFromClient, isFlag2906,statusSuCo
        if self.isCheckedError :
            if self.checkError() == False : 
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
        
        threadLock.acquire()
        if isWaiting == 1:# thoat do mo thanh cong ko co dung khan cap
            isWaiting = 0
            self.sentWaiting2AllClient() 
        threadLock.release()

        ss = "Tủ " + str(self.numberTu) + " Mở"
        loggerInfor.info(ss)
        print("ss")
        
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
            print("MO tu tong quat tuTraiPhai = ", tuTraiPhai)
            return False
        tuKOpen = tuDauOpen
        flagLoop = True
        #gui du lieu den cac tu 
        while flagLoop:
            flagLoop = False
            #Dong cac tu nho hon tu can mo
            if tuKClose < self.numberTu :
                flagLoop = True
                nameTu = firstName + str(tuKClose)
                dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02 #dong cac tu nho hon tu can mo
                self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                tuKClose +=1
                

            if tuKOpen >= self.numberTu :
                flagLoop = True
                nameTu = firstName + str(tuKOpen)
                dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00 # khong kiem tra cam bien
                dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x01 # mo cac tu lon hon tu can mo
                self.sendMes2Client(nameTu,b'\xbb\xbb' + bytes(dataSent2Client[nameTu].dt2Pi2Ar))
                tuKOpen -=1
            if isWaiting == 2 and self.isCheckedError :
                return False
            time.sleep(self.timeMiliSecond)
        #cho cac tuDau dong mo xong thi gui lenh tiep
        flagLoop = True
        flagDoneClose = False
        flagDoneOpen = False
        while flagLoop:
            nameTuOpen = firstName + str(tuDauOpen) 
            nameTuClose = firstName + str(tuDauClose) 
            flagLoop = False
            #cho den khi nao tuDau mo xong hoac dong xong ( phong tru truong hop ko bat duoc mo thi dong)
            while ( flagDoneOpen or dataReceivedSer[nameTuOpen].statusMotor != 2 ) and (flagDoneClose or dataReceivedSer[nameTuClose].statusMotor != 4 ):
                if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                    return False

            if flagDoneClose == False and  dataReceivedSer[nameTuClose].statusMotor == 4 :
                tuDauClose += 1
                if tuDauClose >=  self.numberTu :
                    flagDoneClose = True
                else:
                    flagLoop = True
                    
            if flagDoneOpen == False and  dataReceivedSer[nameTuOpen].statusMotor == 2:
                tuDauOpen -= 1
                if tuDauOpen <  self.numberTu :
                    flagDoneOpen = True
                else:
                    flagLoop = True
            time.sleep(self.timeMiliSecond)
        return True

#thread dung de dong tu version 2
class CloseTuThreadVer2(threading.Thread,DongMoTu):
    def __init__(self, isCheckError):
        DongMoTu.__init__(self)
        threading.Thread.__init__(self)
        self.daemon=True
        #bien kiem tra xem co can check su co de dong tu khong
        self.isCheckedError = isCheckError
        
    def CheckError(self):
        global isWaiting,haveSucoClient,tuOpenedLeft, isGetDataFromClient, isFlag2906,statusSuCo
        print("Start Dong TU")
        self.checkSuCo(True)
        threadLock.acquire()
        isWaiting = 3 #set co su co co nguoi trong tu va yeu cau dong mo tu
        threadLock.release()

        if statusSuCo == 1 :# co nguoi trong tu
            linkFile = folderMP3 + "008.mp3"
            playmp3(linkFile)
            return False
        elif  statusSuCo == 4 :# co nguoi trong tu
            linkFile = folderMP3 + "015.mp3"
            playmp3(linkFile)
            return False
        linkFile = folderMP3 + "005.mp3"
        playmp3(linkFile)
        return True

    def closeTuLeft(self):
        global numClientLeft, isWaiting, dataReceivedSer, tuTraiPhai
        tuKLeft = 1
        tuDauLeft = 1
        tuKRight = 1
        tuDauRight = 1
        flagDongTu = True
        print("close tu start")
        #gui lenh dong khong kiem tra cam bien cho cac tu chua dong
        #gui lenh dong tu ben trai 
        while tuKLeft <= numClientLeft and (tuTraiPhai == 'A' or tuTraiPhai =='L') :  
            nameTu = "Left_" + str(tuKLeft) 
            #neu tu dang dong va flagDongTu == True thi bo qua ( tu da duoc dong roi khong can gui tin hieu dong tu nua )
            if dataReceivedSer[nameTu].statusMotor == 4 and flagDongTu:
                print(" Tu left_" , tuDauLeft , " da Dong ")
                tuKLeft += 1
                tuDauLeft += 1
                continue
            flagDongTu = False
            dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
            dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00           
            self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
            tuKLeft+=1
            if isWaiting == 2 and self.isCheckedError : #neu waiting==2(dung khan cap) trong truong hop co kiem tra su co
                return False
            time.sleep(self.timeMiliSecond)
        #gui lenh dong tu ben phai 
        flagDongTu= True
        while tuKRight <= numClientRight and (tuTraiPhai == 'A' or tuTraiPhai =='R') :  
            nameTu = "Right_" + str(tuKRight) 
            #neu tu dang dong va flagDongTu == True thi bo qua ( tu da duoc dong roi khong can gui tin hieu dong tu nua )
            if dataReceivedSer[nameTu].statusMotor == 4 and flagDongTu:
                print(" Tu Right_" , tuDauRight , " da Dong ")
                tuKRight += 1
                tuDauRight += 1
                continue
            flagDongTu = False
            dataSent2Client[nameTu].dt2Pi2Ar[2] = 0x02
            dataSent2Client[nameTu].dt2Pi2Ar[5] = 0x00           
            self.sendMes2Client(nameTu,b'\xbb\xbb'+bytes(dataSent2Client[nameTu].dt2Pi2Ar))
            tuKRight+=1
            if isWaiting == 2 and self.isCheckedError : #neu waiting==2(dung khan cap) trong truong hop co kiem tra su co
                return False
            time.sleep(self.timeMiliSecond)

        #waiting cac tu dong xong
        while tuDauLeft <= numClientLeft or tuDauRight <= numClientRight:
            nameTuLeft = "Left_" + str(tuDauLeft)
            nameTuRight = "Right_" + str(tuDauRight)
            while True :
                if self.stopped or ( isWaiting != 1 and self.isCheckedError):
                    return False
                if tuDauLeft <= numClientLeft and dataReceivedSer[nameTuLeft].statusMotor == 4 :#tu da dong kiem tra tu tiep theo
                    tuDauLeft += 1
                    break
                if tuDauRight <= numClientRight and dataReceivedSer[nameTuRight].statusMotor == 4 :
                    tuDauRight += 1
                    break
            time.sleep(self.timeMiliSecond)
        return True

    def run(self) : 
        global isWaiting,haveSucoClient,tuOpenedLeft, isGetDataFromClient, isFlag2906,statusSuCo, tuTraiPhai
        if self.isCheckedError : # neu co kiem tra dieu kien
            if self.CheckError() == False : #neu dieu kien khong thoa man
                return 
            threadLock.acquire()
            isGetDataFromClient = False
            #send wating form
            isFlag2906 = False
            isWaiting = 1
            tuOpenedLeft = "0"
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
        if  self.closeTuLeft() == False : #chua dong tu xong
            return
        if self.isCheckedError :
            self.doneExecute("Dong Tu")

    def doneExecute(self, ss):    
        global  isWaiting
        threadLock.acquire()
        if isWaiting == 1:# thoat do mo thanh cong ko co dung khan cap
            isWaiting = 0
            self.sentWaiting2AllClient() 
        threadLock.release()
        loggerInfor.info(ss)


def dongMoTuFunction(inCase,numTu) :
    global threadDongMoTu
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
            threadDongMoTu = MoTuTongQuat(numTu,True)
            threadDongMoTu.start()
        elif inCase == 3:
            threadDongMoTu = MoTuTongQuat(numTu,False)
            threadDongMoTu.start()

def saveNhietDoDoAm():
    for tu in dataReceivedSer:
        s = tu + " "+str(dataReceivedSer[tu].tempIn )+" " +str(dataReceivedSer[tu].humiIn )+" "+str(dataReceivedSer[tu].tempOut )+ " "+str(dataReceivedSer[tu].humiOut ) 
        temp_logger.info(s)

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
