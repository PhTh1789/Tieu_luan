import matplotlib.pyplot as plt 
import pandas as pd
import os
# from my_module.features import back_step

# Đường dẫn tới folder score
score_folder_path = r"D:\PYTHON\Tieu_luan\score"

xlsx_global_path = 0

# HÀM CHỌN MÔN
def get_coree( score_folder_path) :
    subject_list = os.listdir(score_folder_path)
    # Lấy danh sách các folder có trong đường dẫn
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
    global xlsx_global_path
    xlsx_global_path = xlsx_path
    return  xlsx_path,subject_list, option
    # Chọn cột điểm muốn xem
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
    
# HÀM LẤY DỮ LIỆU CỘT
def colum_data(colum_name):
        # gán biến của get_scoree vào
        semester = pick_semester()
        colum_name = semester
        colum_name1 = 0
        # if semester == "Cả Hai":
        #     colum_name = "Giữa kỳ"
        #     colum_name1 = "Cuối kỳ"
        #     data = data_excel[colum_name].tolist()
        #     data1 = data_excel[colum_name1].tolist()
        #     print ("data_1",data)
        #     print("data1",data1)
        # Đọc dữ liệu từ file Excel
        semester == "Giữa kỳ" or semester == "Cuối kỳ"
        data_excel = pd.read_excel(xlsx_global_path)
        # Đọc dữ liệu của cột colum_name
        data = data_excel[colum_name].tolist()
        return data

# HÀM ĐẾM SỐ ĐIỂM
def count_score(data_score):
    data_dict = {}
    value_list= []
    # Tạo danh sách các cặp (phần tử, số lần xuất hiện)
    for element in data_score:
        data_dict[element] = data_dict.get(element, 0) + 1
    # sort theo điểm từ bé tới lớn
    sort_list = sorted(data_dict)
    for i in sort_list: 
        value_list.append(data_dict[i])
    return sort_list,value_list
# HÀM CHART
def scatter_chart():
    sort_list,value_list = count_score(colum_data(any))
    x = sort_list
    y = value_list
    plt.style.use ('seaborn-v0_8-whitegrid')
    # plt.legend();
    plt.scatter(x,y,s= 15, c = "blue",label = "điểm");
    plt.plot(x,y);
    plt.title("Biểu đồ thể hiện sự phân bố điểm của lớp ",)
    plt.xlabel("Điểm")
    plt.ylabel("Count")
    plt.show();

def pick_class():
    get_coree(score_folder_path)
    class_sheet=pd.ExcelFile(xlsx_global_path).sheet_names
    while True:
        try:
            print("Hãy chọn lớp muốn vẽ đồ thị: ")
            for i in range(0,len(class_sheet)):
                 print((f"({i}) {class_sheet[i]}"))
            print(f"{len(class_sheet)+1} Cả hai")
            num_objects = int(input("-->"))
            #num_objects = int(input(f"Hãy chọn lớp muốn vẽ đồ thị: \n(1) {class_sheet[0]}   \n(2) {class_sheet[1]} \n(3) So sánh 2 lớp \n-->"))
            if num_objects in range(0,len(class_sheet)):
                chose = int(input("Chọn kiểu biểu đồ: \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \n(3) Histogram - Biểu đồ tần suất \nHoặc nhập bất kỳ số nào khác để quay lại\nHoặc nhập bất kỳ số nào khác để quay lại\n-->"))
                if chose == 1:
                    scatter_chart()
                    break
            elif num_objects == "Cả hai":
                chose = int(input("Chọn kiểu biểu đồ: \n(1) Pie chart - Biểu đồ tròn \n(2) Scatter chart - Biểu đồ thể hiện sự phân bố \n(3) Histogram - Biểu đồ tần suất \nHoặc nhập bất kỳ số nào khác để quay lại \n-->" ))
                if chose == 1:
                    print("pie_chart ")
                    break
                elif chose == 2:
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