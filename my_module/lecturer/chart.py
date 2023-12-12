import pandas as pd
from menu import *
from back2 import *

#### MAIN + CHỌN MÔN --------------------------------------------------------------------------------------------
def get_chart():
    # Đường dẫn tới folder score
    score_folder_path = r"D:\PYTHON\Tieu_luan\score"
    # chọn môn
    xlsx_path,subject_list, option = get_coree(score_folder_path)
    # gán biến tên môn
    subject = subject_list[option]
    # gọi ra tên của tất cả các lớp học có trong file
    class_sheet=pd.ExcelFile(xlsx_path).sheet_names
    while True:
        try:
    #### CHỌN Đối tượng
            num_class = pick_class (class_sheet)
        ### 1 Đối tượng
            if num_class in range(len(class_sheet)):
                # gán biến tên lớp
                class_=class_sheet[num_class]
                # Chọn học kỳ và gán biến tên học kỳ
                semester = pick_semester()
            ## 2 học kỳ
                if semester == "Cả hai":
                # gán biến lần lượt: data học kỳ số 1, data học kỳ số 2, tên học kỳ số 1, tên học kỳ số 2 được lấy ra từ hàm colum
                    data_sem1 , data_sem2 , colum_name1 , colum_name2 = colum_data2_1c(xlsx_path,semester,class_)
                    chosse = int(input("Chọn kiểu biểu đồ: \
                                       \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                       \n(2) Histogram - Biểu đồ tần suất \
                                       \n(3) Pie chart - Biểu đồ tròn \
                                       \nHoặc nhập ký tự bất kỳ khác để quay lại\
                                       \n--> "))
                # Scatter chart 
                    if chosse == 1:
                        scatter_chart1(data_sem1,data_sem2,subject,class_,colum_name1,colum_name2)
                        break

                # histogram
                # chỉ có biến 2 học kỳ, biến class_
                    elif chosse == 2:
                        hist_chart2(data_hist1 = data_sem1,
                                    data_hist2 = data_sem2,
                                    subject = subject,
                                    colum_name1 = colum_name1,
                                    colum_name2 = colum_name2,
                                    class_ = class_)
                        break
            
                # Pie chart 
                    elif chosse == 3:
                        range_1, binss1, range_2 , binss2 = range_data2(data_sem1 , data_sem2)
                        pie_chart2(range_1, binss1, range_2 , colum_name1 , colum_name2, binss2 ,class_ ,subject )
                        break

                    else:
                        print("Hãy nhập đúng giá trị phù hợp")
            ### 1 học kỳ
                elif semester == "Cuối kỳ" or semester =="Giữa kỳ":
                    # lấy cột điểm
                    data_score = colum_data1_1c(xlsx_path,semester,class_)
                    # chọn kiểu biểu đồ
                    chosse = int(input("Chọn kiểu biểu đồ: \
                                    \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                    \n(2) Histogram - Biểu đồ tần suất \
                                    \n(3) Pie chart - Biểu đồ tròn \
                                    \nHoặc nhập ký tự bất kỳ khác để quay lại\
                                    \n-  ->"))
                ## scatter     
                    if chosse == 1:
                    # sort key và value
                        sort_list,value_list = count_score(data_score)
                        scatter_chart1(sort_list,value_list,subject,class_,semester = semester)
                        break
                ## histogram
                    elif chosse == 2:
                        hist_chart1(data_score,semester,class_,subject)
                        break
                ## Pie
                    elif chosse == 3:
                        range_, bins = range_data1(data_score)
                        pie_chart1(range_,bins ,semester ,class_ ,subject)
                        break
                    else:
                        print("Lỗi: nhập giá trị ngoài khoản cho phép")
                # elif semester == "3" :
                #     back_step2(name_function = pick_class(class_sheet), mess = "Quay lại ?")        
        ### 2 Đối tượng--------------------------------------------------------------------------------------------
            elif num_class == len(class_sheet):
                num_class1, num_class2 = pick_class2(class_sheet = class_sheet)
                while True:
                    # try:
                        if (num_class1 and num_class2) in range(len(class_sheet)):
                            # gán tên lớp vào class_1, class_2
                            class_1 = class_sheet[num_class1]
                            class_2 = class_sheet[num_class2]
                            print(class_1,class_2)
                            semester = pick_semester()
                        ## 2 học kỳ
                            if semester == "Cả hai":
                                data_mid_sem_1, data_mid_sem_2, data_end_sem_1, data_end_sem_2, \
                                colum_name1, colum_name2 = colum_data2_2c(xlsx_path, semester, class_1, class_2)
                                chosse = int(input("Ở lựa chọn này chỉ hỗ trợ vẽ 1 biểu đồ \
                                                \n Chọn:\
                                                \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố\
                                                \n--> "))
                            # Scater 
                                if chosse == 1:
                                    scatter_chart2(data_mid_sem_1 , data_mid_sem_2 ,data_end_sem_1 ,data_end_sem_2, subject,
                                                   class_1 = class_1, class_2 = class_2, colum_name1 = colum_name1, colum_name2 = colum_name2)
                                    break
                                # elif chosse == 2:
                                #     back_step2 ( name_function = pick_semester, mess="Quay lại ?")
                                else:
                                    print("Hãy nhập đúng giá trị phù hợp")
                        # 1 học kỳ
                            # elif semester == "3":
                            #     back_step2(name_function= pick_class2, mess="Quay lại ?")
                            else:
                                data_score1,data_score2 = colum_data1_2c(xlsx_path,semester,class_1,class_2) 
                                chosse = int(input("Chọn kiểu biểu đồ: \
                                                \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                                \n(2) Histogram - Biểu đồ tần suất \
                                                \n(3) Pie chart - Biểu đồ tròn \
                                                \nHoặc nhập ký tự bất kỳ khác để quay lại\
                                                \n--> "))
                            # Scater 
                                if chosse == 1:
                                    sort_list1, value_list1 = count_score(data_score1)
                                    sort_list2, value_list2 = count_score(data_score2)
                                    scatter_chart2(sort_list1,sort_list2, value_list1 , value_list2,
                                                    subject = subject,class_1 = class_1 , class_2 = class_2 , semester = semester)
                                    break
                            # Histogram
                                elif chosse == 2:
                                    hist_chart2(data_hist1 = data_score1 ,
                                                data_hist2 = data_score2,
                                                subject = subject,
                                                class_1 = class_1,
                                                class_2 = class_2,
                                                semester = semester)
                                    break
                            # Pie chart 
                                elif chosse == 3:
                                    range_1, binss1, range_2 , binss2 = range_data2(data_range_1 = data_score1,
                                                                                    data_range_2 = data_score2 )
                                    pie_chart2( range_1, binss1, range_2 , binss2,
                                               subject = subject, class_1 = class_1,
                                               class_2 = class_2,
                                               semester = semester)
                                    break      
                                else:
                                    print("Hãy nhập đúng giá trị phù hợp")
                        else:
                            print("Lỗi: nhập giá trị ngoài khoản cho phép")

                    # except:
                        print("Lỗi: Nhập sai định dạng")
                break            
            elif num_class == (len(class_sheet) + 1):
                back_step2(name_function = get_chart, mess="Quay lại")
            else:
                print("Lỗi: Nhập sai định dạng")
    #### Trường hợp sai định dạng
        except ValueError :
                print("Lỗi: Nhập sai định dạng")
get_chart()