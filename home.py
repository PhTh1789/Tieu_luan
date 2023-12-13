import pandas as pd
# import openpyxl
from my_module.student import student_checking, get_core, get_core0, get_core1
from my_module.lecturer import lecturer_checking, get_report, get_chart
from my_module.features import back_step, up_book, loading_mess

lecturer_data_path = r'D:\PYTHON\Tieu_luan\account\lecturer.xlsx'
student_data_path = r'D:\PYTHON\Tieu_luan\account\student.xlsx'
score_data = r"D:\PYTHON\Tieu_luan\score"

#Chọn giao diện
while True :
    define = input("Bạn là\n(0) Sinh viên\n(1) Giảng viên\n-> ")
    if define == "0" :
        print('\n')
        mssv = student_checking(student_data_path, "MSSV", "Mật khẩu")
        if (mssv == "datlaimatkhau") :
            print('\n')
            mssv = student_checking(student_data_path, "MSSV", "Mật khẩu")
        break
    elif define == "1" :
        print('\n')
        lecturer_id = lecturer_checking(lecturer_data_path, "Mã giảng viên", "Mật khẩu")
        if (lecturer_id == "datlaimatkhau") :
            print('\n')
            lecturer_id = lecturer_checking(lecturer_data_path, "Mã giảng viên", "Mật khẩu")
        break
    
    print("Lỗi: Giá trị nhập khác 0 và 1")

def student() :
    while True:
        print(f"\nTài khoản: {mssv}\nTính năng:")
        option = input("(0) Xem điểm\n(1) Phản hồi\n(2) Tài liệu\n(3) Thoát\n-> ")
        if (option == "0"):
            print('\n')
            get_core0(get_core(mssv, score_data)) #chạy get_core0 với các biến get_core trả về
            back_step(name_function=student, mess="Quay lại")
            break

        elif (option == "1") :
            print('\n')
            get_core1(get_core(mssv, score_data))
            back_step(name_function=student, mess="Quay lại")
            break            
        
        elif (option == "2") :
            print('\nTruy cập đường dẫn dưới đây:\n-> https://drive.google.com/drive/u/0/folders/1AP1E0aOiem_1WkJriombjLfZyaLuiq9b')
            print('\n')
            back_step(name_function=student, mess="Quay lại")
            break

        elif (option == "3") :
            print('\nChương trình kết thúc')
            break

        print("Lỗi: Giá trị nhập không phù hợp")

def lecturer() :
    while True:
        print(f"\nTài khoản: {lecturer_id}\nTính năng:")
        option = input("(0) Lập đồ thị\n(1) Xem phản hồi\n(2) Tài liệu\n(3) Thoát\n -> ")
        if (option == "0") :
            print('\n')
            get_chart( )
            back_step(name_function=lecturer, mess="Quay lại")
            break
        
        # Nhánh xem phản hồi
        elif (option == "1") :
            print('\n') 
            get_report(lecturer_id, score_data, lecturer_data_path)
            lecturer()
            back_step(name_function=lecturer, mess="Quay lại")
            break
        
        # Nhánh up xem tài liệu
        elif (option == "2") :
            print('\n')
            #Sử dụng tài liệu file client_secrets.json và mycreds.txt để xác thực và cấp quyền cho tải file
            up_book()
            back_step(name_function=lecturer, mess="Quay lại")
            break
        
        elif (option == "3") :
            print('\nChương trình kết thúc')
            break

        print("Lỗi: Giá trị nhập không phù hợp")


match define :
    case "0" :
        student()
    case "1" :
        lecturer()