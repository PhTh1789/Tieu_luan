import pandas as pd
from my_module.student import student_checking, get_core
from my_module.lecturer import lecture_checking
from my_module.features import back_step
# from my_module.student import check, get_core
# from my_module.features import loading_mess

lecture_data = pd.read_excel(r'C:\Users\Admin\Desktop\python\TL\TLGiang\account\lecturer.xlsx')
student_data = pd.read_excel(r'C:\Users\Admin\Desktop\python\TL\TLGiang\account\student.xlsx')

#Chọn giao diện
while True :
    define = input("Bạn là sinh viên (0) hay giảng viên (1):\n-> ")
    if define == "0" :
        mssv = student_checking(student_data, "MSSV", "Mật khẩu")
        break
    elif define == "1" :
        lecture_name = lecture_checking(lecture_data, "Giảng viên", "Mật khẩu")
        break
    
    print("Lỗi: Giá trị nhập khác 0 và 1")

def student() :
    while True:
        print("Tính năng:")
        option = input("(0) Xem điểm\n(1) Phản hồi\n(2) Tài liệu\n-> ")
        if (option == "0") :
            get_core(mssv, r"C:\Users\Admin\Desktop\python\TL\TLGiang\score")
            back_step(student)
            break

        elif (option == "1") :
            
            pass
        
        elif (option == "2") :
            pass

        print("Lỗi: Giá trị nhập không phù hợp")

def lecture() :
    while True:
        print("Tính năng:")
        option = input("(0) Lập đồ thị\n(1) Xem phản hồi\n(2) Tài liệu\n-> ")
        if (option == "0") :
            print("option 0")
            back_step(lecture)
            break

        elif (option == "1") :
            print("option 1")
            break
        
        elif (option == "2") :
            print("option 2")
            break

        print("Lỗi: Giá trị nhập không phù hợp")


match define :
    case "0" :
        student()
    case "1" :
        lecture()