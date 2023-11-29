import pandas as pd
from my_module.student import check, get_core
from my_module.features import back_step
# from my_module.student import check, get_core
# from my_module.features import loading_mess

lecture_data = pd.read_excel(r'D:\Code\Python\Tiểu luận - NMLT\account\lecturer.xlsx')
student_data = pd.read_excel(r'D:\Code\Python\Tiểu luận - NMLT\account\student.xlsx')

#Chọn giao diện
while True :
    define = input("Bạn là sinh viên (0) hay là giáo viên (1): ")
    if define == "0" :
        mssv = check(student_data, "MSSV", "Mật khẩu")
        break
    elif define == "1" :
        break
    
    print("Chỉ nhập 0 hoặc 1\n--+--")
def student() :
    while True:
        print("Tính năng:")
        option = input("(0) Xem điểm\n(1) Phản hồi\n(2) Tài liệu\n-> ")
        if (option == "0") :
            get_core(mssv, r"D:\Code\Python\Tiểu luận - NMLT\score")
            back_step(student)
            break

        elif (option == "1") :
            pass
        
        elif (option == "2") :
            pass

        print("Lựa chọn không phù hợp")

def lecture() :
    print("something")


match define :
    case "0" :
        student()
    case "1" :
        lecture()