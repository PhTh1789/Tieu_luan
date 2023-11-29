import os
import pandas as pd

def get_core(mssv, score_folder_path) :
    subject_list = os.listdir(score_folder_path)
    print("Chọn môn: ")
    for index, subject in zip(range(0, len(subject_list)), subject_list) :
        #Cắt chuỗi bỏ phần định dạng sau dấu chấm
        subject_name = subject[:subject.index(".")]
        print(f"({index})", subject_name)

    while True :
        option = input("-> ")
        #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
        if any(option in str(idx) for idx in range(0, len(subject_list))) :
            break
        print("Lựa chọn không phù hợp")

    data = pd.read_excel(score_folder_path + f"\\{subject_list[int(option)]}")
    #Tham số trong isin() phải là iterable
    result = data.loc[data["MSSV"].isin([int(mssv),])]
    
    print("Giữa kỳ: {0}\nCuối kỳ: {1}".format(result["Giữa kỳ"][0], result["Cuối kỳ"][0]))