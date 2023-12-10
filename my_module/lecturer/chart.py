import matplotlib.pyplot as plt 
import pandas as pd
from menu import *

# Đường dẫn tới folder score
score_folder_path = r"D:\PYTHON\Tieu_luan\score"
#### MAIN + CHỌN MÔN --------------------------------------------------------------------------------------------
def pick_class():
    # chọn môn
    xlsx_path,subject_list, option = get_coree(score_folder_path)
    # gán biến tên môn
    subject = subject_list[option]
    # gọi ra tên của tất cả các lớp học có trong file
    class_sheet=pd.ExcelFile(xlsx_path).sheet_names
    while True:
        try:
            #### CHỌN Đối tượng
            print("Hãy chọn lớp muốn vẽ đồ thị: ")
            for i in range(0,len(class_sheet)):
                 print((f"({i}) {class_sheet[i]}"))
            print(f"({len(class_sheet)}) So sánh các lớp")
            num_class = int(input("-->"))
            #### 1 Đối tượng
            if num_class in range(0,len(class_sheet)):
                # gán biến tên lớp
                class_=class_sheet[num_class]
                # Chọn học kỳ và gán biến tên học kỳ
                semester = pick_semester()
                ### 2 học kỳ
                if semester == "Cả hai":
                    data_sem1 , data_sem2 , colum_name1 , colum_name2 = colum_data2(xlsx_path,semester,class_)
                    chosse = int(input("Chọn kiểu biểu đồ: \
                                       \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                       \n(2) Histogram - Biểu đồ tần suất \
                                       \n(3) Pie chart - Biểu đồ tròn \
                                       \nHoặc nhập ký tự bất kỳ khác để quay lại\
                                       \n-  ->"))
                    if chosse == 1:
                        scatter_chart2(data_sem1,data_sem2,colum_name1,colum_name2,semester,class_,subject)
                        break

                    # histogram
                    elif chosse == 2:
                        hist_chart2(data_sem1 , data_sem2 , colum_name1 , colum_name2,class_,subject)
                        break

                    # Pie chart 
                    elif chosse == 3:
                        range_1, binss1, range_2 , binss2 = range_data2(data_sem1 , data_sem2)
                        pie_chart2(range_1, binss1, range_2 , colum_name1 , colum_name2, binss2 ,class_ ,subject )
                        break

                    else:
                        print("Hãy nhập đúng giá trị phù hợp")
                ### 1 học kỳ
                else:
                    # lấy cột điểm
                    data_score = colum_data1(xlsx_path,semester,class_)
                    # sort key và value
                    sort_list,value_list = count_score(data_score)
                    # chọn kiểu biểu đồ
                    chosse = int(input("Chọn kiểu biểu đồ: \
                                       \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                       \n(2) Histogram - Biểu đồ tần suất \
                                       \n(3) Pie chart - Biểu đồ tròn \
                                       \nHoặc nhập ký tự bất kỳ khác để quay lại\
                                       \n-  ->"))
                    if chosse == 1:
                        scatter_chart1(sort_list,value_list,semester,class_,subject)
                        break
                    elif chosse == 2:
                        hist_chart1(data_score,semester,class_,subject)
                        break
                    elif chosse == 3:
                        range_, bins = range_data1(data_score)
                        # print("range_",range_)
                        # print("binss",binss)
                        pie_chart1(range_,bins ,semester ,class_ ,subject)
                        break
            #### 2 Đối tượng
            elif num_class == len(class_sheet):
                print(f"Chọn lớp muốn so sánh - {len(class_sheet)})")
            #     chosse = int(input("Chọn kiểu biểu đồ: \
            #                        \n(1) Pie chart - Biểu đồ tròn \
            #                        \n(2) Scatter chart - Biểu đồ thể hiện sự phân bố \n(3) Histogram - Biểu đồ tần suất \nHoặc nhập bất kỳ số nào khác để quay lại \n-->" ))
            #     if chosse == 1:
            #         print("pie_chart ")
            #         breakS
            #     elif chosse == 2:
            #         break
            #     elif chosse == 3:
            #         print("histogram ")
            #         break
            # Trường hợp là số nhưng ngoài giá trị
            else:
                print("Hãy nhập đúng giá trị phù hợp ")

        # Trường hợp sai định dạng
        except ValueError :
                print("Lỗi: Chỉ nhập giá trị là số")
pick_class()