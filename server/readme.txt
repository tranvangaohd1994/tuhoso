new180703:
    thêm mới chức năng điều khiển điều hòa trên tủ Master, client ko thay đổi gì
    
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

    10 0a : server gui lenh client play loa
    1d 1d : thong gio
    fa fa : server gui cai dat thoi gian cho client

    
20181023:
    lam hien thi do thi nhiet do va do am len do thi logTemp
    

DoneTask 1009:
    them bot tu 


    Task 09-21 :
        dong bo thoi gian cho server va client
        form bao duong chinh lai phan cam bien dem nguoi bao ok , va loa bao den chieu sang 
        form hoc dieu hoc chinh set gia tri khoi tao cho tbInput, them self.btHoc = None cho moi nut dieu khien

Chế độ bảo dưỡng :
    +Chỉ được kích hoạt và Kết thúc khi thao tác trên Master.
    +Trong quá trình bảo dưỡng Master ko care bất kì cảnh báo or sự cố nào
        (trong timer nếu đang bd return luôn)

Task 0914 : 
    0. cai dạt thoi gian tu dong mo thong gio
    1.  Phần loa báo cho bảo dưỡng còn không đúng (File âm thanh sai), nhiều khi kiểm tra xong còn không báo loa(Như kiểm tra cảm biến đếm người xong không báo hoàn thành thao tác)
    2. Nhiệt độ có thể xem dưới dạng đồ thị, phần log có thể xem được trực tiếp trên tủ Master mà không cần thoát app
    Kiểm tra bản log có kèm thời gian các thông tin tối giản hơn: (Lỗi cập nhập liên tục) (Lưu file sự cố và file lưu hoạt động thường để riêng)
        + Nhiệt độ độ ấm 10 phút/ lần
        + Thời gian đóng, mở, dừng tủ có kèm tên tủ
        ví dụ: Tủ 1 mở : 10:22:33s ngày 25/07/2018
        + Thời gian sự cố:
        Ví dụ: Sự cố người trong tủ: 10:23:55s ngày 25//2018
        + Các thông tin lưu đều có thể xem trên tủ Master và có biểu đồ nhiệt độ theo thời gian
    
    4. Phần chờ cảm biến vân tay quá chậm 
    5. Xây dựng giao diện thêm bớt các cột trên Master. Việc thêm bới cột bằng phần mềm chỉ thao tác được với tủ ngòai cùng, Setup IP bằng phần cứng. 
    6. Xây dựng hệ thống với tủ bên phải (Lên phương án vì sắp triển khai rồi)	
    7. Khi 1 tủ dừng do bản thân nó, các tủ khác vẫn dừng rất  chậm. Một số trường hợp không mở được tủ hoặc thoát màn hình chờ khi chưa hoàn thành thao tác (Ví dụ như tủ 1 mở xong mở tủ 2 thì không được)
    
    9. Khi hệ thống đang vận hành (Quá trình đóng hoặc mở), yêu cầu màn hình đều sáng
    (Có cách nào can thiệp vào độ sáng màn hình vào thời gian sáng không)
  
   
    13. Xây dựng thuật toán tự động tính toán nhiệt độ độ ẩm trong và ngoài giá và đưa ra cảnh báo đồng thời khởi động các hệ thống điều hòa điều ẩm
    Dễ dàng liên kết được các bộ giá với nhau
    - Có thể nhập dữ liệu, tìm kiếm dữ liệu trên SQL
    - Phân quyền bảo mật với các nội dung tìm kiếm, mượn trả
    - Khóa giá từ xa liên kết với hệ thống qua Ethernet
    - Tự động hoặc đặt giờ thông gió từ xa
    - Có thể tính toán nhiệt độ độ ẩm trong và ngoài giá và đưa ra cảnh báo tới phần mềm PC đồng thời khởi động các hệ thống điều hòa điều ẩm

DoneTask0914:
    10. Test module thời gian thực update thoi gian thu tu server-->client client tu xet thoi gian cho chinh minh

    8. Cảnh báo cháy: Cháy trong tủ nào thì tủ đó mở ra, Cháy ngoài tủ thì đóng toàn bộ hệ thống (Chỉ loa cảnh báo cháy không cần loa cho các thao tác đóng mở hoàn thành mặc dù nó đang đóng hoặc đang mở)
    11. Xây dựng thuật toán điều khiển cho thông gió  trên Master (Mục 7, Byte số 1,6 , Byte số 6 là khoảng cách giữ các tủ với khoảng cách tối đa là 80cm, ví dụ 2 tủ khoảng cách là 40, 4 tủ khoảng cách sẽ là 20)
    12. Xem thuật toán đóng mở tủ mới, code để thử nghiệm luôn
    3. Update lại màn hình cho màn hình mới
        1-welcome
        2-SV_Login
        3-SV_ChonTuCaiDat
        4-setChieuQuayDC
        5-mainDisplay
        6-formTimKiem
        7-fKetQuaTraCuu
        8-SV_CanhBao
        9-formWaiting
        10-SV_ChonTuCaiDatV2
        11-SV_CaiDatNangCao
        12-BaoDuongServer
        13-setDieuKienVanHanh
        14-setLucChongKet
        15-setKCMotu
        16-setTocDoDC
        17-setKCGiamToc
        18-setThongGio
        19-setThemTu
        20-setPassword
        21-svCaiDatPhuTro




sudo hwclock --set --date "2018-09-17 23:40:20+0700"


import os
from subprocess import call

call('sudo hwclock --set --date "2018-09-17 23:40:20+0700"',shell=True)
call('sudo hwclock -r',shell=True)
call('sudo hwclock -s',shell=True)

import time
from time import strftime
cnt=0
while cnt<20:
    cnt+=1
    _date = strftime("%H:%M:%S  %A,%d/%m/%Y")
    print(_date)
    time.sleep(1)

#os.system('sudo hwclock --set --date "2018-09-17 23:40:20+0700"')
#os.system('sudo hwclock -r')
#os.system('sudo hwclock -s')


