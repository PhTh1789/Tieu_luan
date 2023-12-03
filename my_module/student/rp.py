import os
import pandas as pd

subject_list = os.listdir(r"C:\Users\Admin\Desktop\python\TL\TLGiang\score")
print(subject_list)
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

score_folder_path = r"C:\Users\Admin\Desktop\python\TL\TLGiang\score"
data = pd.read_excel(score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx")
print((score_folder_path + f"\\{subject_list[int(option)]}"))
result = data[data["MSSV"] == int(22166101)]
#Tiến hành reset index vì lấy phần từ trong cột sẽ chọn theo index
#Khi không có drop thì dataframe sẽ thêm một cột là index cũ trước reset
result = result.reset_index(drop = True)
print("Giữa kỳ: {0}\nCuối kỳ: {1}".format(result["Giữa kỳ"][0], result["Cuối kỳ"][0]))