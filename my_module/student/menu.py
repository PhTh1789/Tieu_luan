import os
import pandas as pd
import openpyxl
import numpy as np
from datetime import datetime
from my_module.features import loading_mess

# tách ra để sử dụng nhiều lần không cần phải code lại
def get_core(mssv, score_folder_path) :
    subject_list = os.listdir(score_folder_path)
    print("Chọn môn: ")
    for index, subject in zip(range(0, len(subject_list)), subject_list) :
        print(f"({index})", subject)

    while True :
        option = input("-> ")
        #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
        if any(option in str(idx) for idx in range(0, len(subject_list))) :
            break
        print("Lựa chọn không phù hợp")
    return mssv, score_folder_path, subject_list, option

#CHỨC NĂNG XEM ĐIỂM
def get_core0(get):
    mssv, score_folder_path, subject_list, option = get #lấy từ hàm get_core trả về
    data = pd.read_excel(score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx")
    result = data[data["MSSV"] == int(mssv)]
    #Tiến hành reset index vì lấy phần từ trong cột sẽ chọn theo index
    #Khi không có drop thì dataframe sẽ thêm một cột là index cũ trước reset
    result = result.reset_index(drop = True)

    print("Giữa kỳ: {0}\nCuối kỳ: {1}\n".format(result["Giữa kỳ"][0], result["Cuối kỳ"][0]))

#CHỨC NĂNG PHẢN HỒI
def get_core1(get):
    mssv, score_folder_path, subject_list, option = get
    #Lấy đường dẫn đến file phản hồi của môn đã chọn
    link = score_folder_path + f"\\{subject_list[int(option)]}" + f"\\report.xlsx"
    data = pd.read_excel(link)
    # lấy stt mới dựa trên stt cuối cùng (là stt lớn nhất) của file
    stt = int(np.nan_to_num(data["STT"].max()))
    # ngày dạng hh:mm dd/mmm/yyyy
    date_now = datetime.now().strftime('%H:%M %d-%b-%y')
    print('\n')

    # chọn ẩn danh
    while True:
        private = input("Bạn có muốn ẩn danh?\n(0) Không\n(1) Có\n-> ")
        if (private == "0"):
            break
        elif (private == "1"):
            mssv = "Ẩn danh"
            break
        print("Lựa chọn không phù hợp")
    print('\n')

    #review lời nhắn và gửi
    while True:
        loi_nhan = input("Lời nhắn: ")
        review = input("Bạn có chắc muốn gửi lời nhắn này?\n(0) Gửi\n(1) Chỉnh sửa\n(2) Thoát\n-> ")
        if (review == "0"):
            wb = openpyxl.load_workbook(link) #mở file
            sheet = wb['Sheet1'] #chọn Sheet
            # Thêm hàng mới 
            sheet.append([stt + 1, date_now, mssv, loi_nhan])
            wb.save(link) #lưu lại trên file đang thao tác
            print("Gửi thành công!", end = "")
            loading_mess(3, 1, "")
            print('\n')
            break
        elif (review == "1"):
            continue
        elif (review == "2"):
            print('\n')
            break
        else:
            print("Lựa chọn không phù hợp")


