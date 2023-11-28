import pandas as pd
from my_module.student import check, get_core
# from my_module.student import check, get_core
# from my_module.features import loading_mess

lecture_data = pd.read_excel(r'D:\Code\Python\Tiểu luận - NMLT\account\lecturer.xlsx')
student_data = pd.read_excel(r'D:\Code\Python\Tiểu luận - NMLT\account\student.xlsx')

def student() :
    mssv = check(student_data, "MSSV", "Mật khẩu")
    get_core(mssv, r"D:\Code\Python\Tiểu luận - NMLT\score")

def lecture() :
    print("something")


def login() :
    #Chọn giao diện
    while True :
        define = input("Bạn là sinh viên (0) hay là giáo viên (1): ")
        if define == "0" :
            return student()
        elif define == "1" :
            return lecture()
        
        print("Chỉ nhập 0 hoặc 1\n--+--")
        
    
login()