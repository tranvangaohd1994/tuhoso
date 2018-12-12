new181211:
    +chỉnh sửa lại form viết tiếng việt tự code ko cần cài đặt unicode hay virtualkeyboard
    + xem lại log nhiệt độ sửa lỗi ít data mà vẫn fill toàn bộ trường
    + khong de thong gio 1 phut khi nao nguoi dung dong moi dong

Header giao tiep giua client va server 

Client - server:
    Dong mo tu :
        ee ee : mo tu
        ee ff : dong tu
        ef ed : dung khan cap
    Nhan data:
        aa aa : nhan 30byte data;
        bb bb : data setting
    Su co:
    
server 2 client:
    4f 4b : active after login
    78 71 : server logout
    dd aa : request data from client
    bb bb : nhan 8 byte cai dat tham so gui cho AR
    ee ee : nhan 8 byte cai dat va luu tru
    ef ef : server sent isWaiting = 1 gui 06 xuong cho AR (chuan bi van hanh)
    ef ee : van hanh done isWaiting = 0 
    ef ed : server yeu cau dung khan cap
    ac ac : exit app 
    cb cb : canh bao server gui statusSuCo va ca canh bao
    cb cd : kiem tra su co thanh cong
    
    bd bd : gui che do bao duong
    dc dc : Khóa or mở khóa động cơ
    df dd : server gui bat den cho client
    df df : server gui lenh tat den cho client

    10 0a : server gui lenh client play loa
    1d 1d : thong gio
    fa fa : server gui cai dat thoi gian cho client

    da da : server gui du lieu nhiet do va do am ben ngoai ve cho client

server_1 so bien:{


    statusVanHanh : # 0-mainDisplay 1-waitingForm 2-svDieuKhienDieuHoa 3-BaoDuongServer
        0 : hoat dong binh thuong ko form nao hien

        0x34 : thong bao bat frm Dieu Khien dieu hoa
        0x36 : thong bao da bat dieu khien dieu hoa
        
        0x30(48) : bat dieu hoa
        0x31 : tat dieu hoa
        0x32 : bat quat gio dieu hoa
        0x33 :  tat quat gio dieu hoa
        16-31 : nhiet do tu 16-31

        0x35 : thoat frmDieuHoa



        #form bao duong
        40 : thong bao bat frm bao duong
        41 : thong bao da bat form bao duong
        42 : ket thuc frm bao duong
}

update 20181201{
    + update form tim kiem dul lieu form het qua du lieu
    + masterPC tham phan nhan du lieu
}