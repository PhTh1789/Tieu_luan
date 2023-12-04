import pandas as pd
# import openpyxl
from my_module.student import student_checking, get_core, get_core0, get_core1
from my_module.lecturer import lecture_checking
from my_module.features import back_step

lecture_data = pd.read_excel(r'D:\PYTHON\Tieu_luan\account\lecturer.xlsx')
student_data = pd.read_excel(r'D:\PYTHON\Tieu_luan\account\student.xlsx')

#Chọn giao diện
while True :
    define = input("Bạn là sinh viên (0) hay giảng viên (1):\n-> ")
    if define == "0" :
        print('\n')
        mssv = student_checking(student_data, "MSSV", "Mật khẩu")
        break
    elif define == "1" :
        print('\n')
        lecture_name = lecture_checking(lecture_data, "Giảng viên", "Mật khẩu")
        break
    
    print("Lỗi: Giá trị nhập khác 0 và 1")

def student() :
    while True:
        print("Tính năng:")
        option = input("(0) Xem điểm\n(1) Phản hồi\n(2) Tài liệu\n-> ")
        if (option == "0"):
            print('\n')
            get_core0(get_core(mssv, r"D:\PYTHON\Tieu_luan\score")) #chạy get_core0 với các biến get_core trả về
            back_step(student)
            break

        elif (option == "1") :
            print('\n')
            get_core1(get_core(mssv, r"D:\PYTHON\Tieu_luan\score"))
            back_step(student)
            break            
        
        elif (option == "2") :
            print('\n')
            pass

        print("Lỗi: Giá trị nhập không phù hợp")

def lecture() :
    while True:
        print("Tính năng:")
        option = input("(0) Lập đồ thị\n(1) Xem phản hồi\n(2) Tài liệu\n-> ")
        if (option == "0") :
            print('\n')
            print("option 0")
            back_step(lecture)
            break

        elif (option == "1") :
            print('\n')
            print("option 1")
            break
        
        elif (option == "2") :
            print('\n')
            print("option 2")
            break

        print("Lỗi: Giá trị nhập không phù hợp")


match define :
    case "0" :
        student()
    case "1" :
        lecture()