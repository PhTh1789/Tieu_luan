import matplotlib.pyplot as plt 
import pandas as pd
import os
# from my_module.features import back_step

# Đường dẫn tới folder score
score_folder_path = r"D:\PYTHON\Tieu_luan\score"

# HÀM CHỌN MÔN
def get_coree( score_folder_path) :
    # Lấy danh sách các folder có trong đường dẫn
    subject_list = os.listdir(score_folder_path)
    print("Chọn môn: ")
    # In danh sách tên các folder 
    for index, subject in zip(range(0, len(subject_list)), subject_list) :
        print(f"({index})", subject)
    # input chọn môn theo số
    while True :
        option = input("-> ")
        #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
        if any(option in str(idx) for idx in range(0, len(subject_list))) :
            break
        print("Lựa chọn không phù hợp")
    # đường dẫn tới file excel sau khi chọn môn
    xlsx_path = score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx"
    # Lấy ra tên tất cả các sheet 
    # list môn học, lựa chọn là số, dữ liệu cột đã đọc
    return  xlsx_path,subject_list, option 
# HÀM LẤY DỮ LIỆU CỘT
def colum_data(colum_name):
        # gán biến của get_scoree vào
        xlsx_path,subject_list, option= get_coree(score_folder_path)
        # Đọc dữ liệu từ file Excel
        data_excel = pd.read_excel(xlsx_path)
        # Đọc dữ liệu của cột colum_name
        colum_data = data_excel[colum_name].tolist()
        # print (colum_data)
        return colum_data
def pick_class():
    while True:
        xlsx_path,subject_list, option = get_coree(score_folder_path)
        class_sheet=pd.ExcelFile(xlsx_path).sheet_names
        try: 
            num_objects = int(input(f"Hãy chọn lớp muốn vẽ đồ thị: \n(1) {class_sheet[0]}   \n(2) {class_sheet[1]} \n-->"))
            if num_objects == 1:
                chose = int(input("Chọn: \n(1) Để vẽ bar chart \nHoặc nhập bất kỳ số nào khác để quay lại\n-->"))
                if chose == 1:
                    print("bar_chart ")
                    break
            elif num_objects == 2:
                chose = int(input("Chọn kiểu biểu đồ: \n(1) Pie chart - Biểu đồ tròn \n(2) Scatter chart - Biểu đồ thể hiện sự phân bố \n(3) Histogram - Biểu đồ tần suất \nHoặc nhập bất kỳ số nào khác để quay lại \n-->" ))
                if chose == 1:
                    print("pie_chart ")
                    break
                elif chose == 2:
                    print("scatter_chart ")
                    break
                elif chose == 3:
                    print("histogram ")
                    break
            # Trường hợp là số nhưng ngoài giá trị
            else:
                print("Xin hãy nhập đúng giá trị phù hợp ")

        # Trường hợp sai định dạng
        except ValueError :
                print("Lỗi: Chỉ nhập giá trị là số")
pick_class()