
import logging

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
loggerInfor = setup_logger('Infor_logger', '/home/gao/Desktop/Infor.log')
dt=[13,14,15,12]

def saveNhietDoDoAm():
    for tu in range(1,4):
        nameTu = "Left_"+str(tu)
        #tempIn HumiIn tempout HumiOut
        s = nameTu +" "+str(dt[0])+" " +str(dt[1])+" "+str(dt[2])+ " "+str(dt[3]) + " "
        loggerInfor.info(s)

saveNhietDoDoAm()