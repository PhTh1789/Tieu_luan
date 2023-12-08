import pandas as pd
from datetime import datetime


def get_report(lecturer_id,score, lecturer_data):
    data = lecturer_data #gán lại cho gọn
    subject = data[data["Mã giảng viên"] == str(lecturer_id)]
    subject = subject.reset_index(drop = True)
    subject = subject["Bộ môn"][0]
    read_file = pd.read_excel(score + f"\\{subject}\\report.xlsx")

    print("Môn {0}:".format(subject))
    print(read_file.tail(30) if len(read_file) != 0 else "Dữ liệu rỗng!")
    #Dùng tail để hiện thông tin mới nhất, nếu chỉ dùng print(read_file) sẽ hiện như cc khi số lượng dòng quá nhiều
    print(f"Xem chi tiết tại:  {score}\\{subject}\\report.xlsx")    

    while True:
        option = input("\nTính năng:\n(0) Dùng bộ lọc\n(1) Quay lại menu Tính năng\n-> ")
        if (option == "0"):
           
           while True:
            condition = input('Nhập điều kiện để đưa vào hàm "pandas.DataFrame.loc[]".\nVí dụ: read_file.MSSV == "Ân danh" -> ')
            #"Gio" dạng object -> Khong loc theo "Gio"
            try:
                print(read_file.loc[eval(condition)] if len(read_file.loc[eval(condition)]) != 0 else "Dữ liệu rỗng!")
                #eval() : Biến chuỗi thành dạng biểu thức.
                break
            except:
                print("Nhập sai cú pháp!")
                break

        elif (option == "1") :
            print('\n')
            break           
        else:
           print("Lỗi: Giá trị nhập không phù hợp")

## CHỌN HỌC KỲ
def pick_semester():
    while True:
            semester = input("Hãy chọn cột điểm: \n(0) Giữa kỳ \n(1) Cuối kỳ \n(2) Cả hai \n-->" )
            if semester == "0":
                semester = "Giữa kỳ"
                break
            elif semester == "1":
                semester = "Cuối kỳ"
                break
            elif semester == "2" :
                semester = "Cả hai"
                break
            else:
                print("Hãy chọn đúng định dạng")
    return semester

