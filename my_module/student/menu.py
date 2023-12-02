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
        #Cắt chuỗi bỏ phần định dạng sau dấu chấm
        subject_name = subject
        print(f"({index})", subject_name)

    while True :
        option = input("-> ")
        #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
        if any(option in str(idx) for idx in range(0, len(subject_list))) :
            break
        print("Lựa chọn không phù hợp")
    return mssv, score_folder_path, subject_list, option

# dùng cho option = 0
def get_core0(get):
    mssv, score_folder_path, subject_list, option = get #lấy từ hàm get_core trả về
    data = pd.read_excel(score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx")
    result = data[data["MSSV"] == int(mssv)]
    #Tiến hành reset index vì lấy phần từ trong cột sẽ chọn theo index
    #Khi không có drop thì dataframe sẽ thêm một cột là index cũ trước reset
    result = result.reset_index(drop = True)

    print("Giữa kỳ: {0}\nCuối kỳ: {1}".format(result["Giữa kỳ"][0], result["Cuối kỳ"][0]))

# dùng cho option = 1
def get_core1(get):
    mssv, score_folder_path, subject_list, option = get

    link = score_folder_path + f"\\{subject_list[int(option)]}" + f"\\report.xlsx" # sử dụng nhiều lần nên gán biến
    data = pd.read_excel(link)
    stt = int(np.nan_to_num(data["STT"].max())) # lấy stt mới dựa trên stt cuối cùng (là stt lớn nhất) của file
    date_now = datetime.now().strftime('%H:%M %d-%b-%y') # ngày dạng hh:mm dd/mmm/yyyy

    # chọn ẩn danh
    while True:
        private = input("Bạn có muốn ẩn danh?\n(0) Không\n(1) Có\n-> ")
        if (private == "0"):
            break
        elif (private == "1"):
            mssv = "Ẩn danh"
            break
        print("Lựa chọn không phù hợp")

    #review lời nhắn và gửi
    while True:
        loi_nhan = input("Lời nhắn: ")
        review = input("Bạn có chắc muốn gửi lời nhắn này?\n(0) Thay doi loi nhan\n(1) Gui\n(Huy) Thoat\n-> ")
        if (review == "0"):
            pass
        elif (review == "1"):
            wb = openpyxl.load_workbook(link) #mở file
            sheet = wb['Sheet1'] #chọn Sheet
            # Thêm hàng mới 
            sheet.append([stt + 1, date_now, mssv, loi_nhan])
            wb.save(link) #lưu lại trên file đang thao tác
            print("Gửi thành công!", end = "")
            loading_mess(3, 1, "")
            break
        elif (review == "Huy"):
            break
        else:
            print("Lựa chọn không phù hợp")


