import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import os
from datetime import datetime
from my_module.lecturer.back2 import *
# from back2 import back_step2


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

## CHỌN MÔN-----------------------------------------------------------------------------------------------
def pick_subject() :
    score_folder_path = r"D:\PYTHON\Tieu_luan\score"
    subject_list = os.listdir(score_folder_path)
    # input chọn môn theo số
    while True :
        try:
    # Lấy danh sách các folder có trong đường dẫn
            print("Chọn môn: ")
            # In danh sách tên các folder 
            for index, subject in zip(range(0, len(subject_list)), subject_list) :
                print(f"({index})", subject)
            print(f"({len(subject_list)}) Quay lại")
            option = int(input("-> "))
            #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
            if option in range(len(subject_list)) :
                # đường dẫn tới file excel sau khi chọn môn
                xlsx_path = score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx"
                # gán biến tên môn
                subject = subject_list[option]
                # gọi ra tên của tất cả các lớp học có trong file
                class_sheet=pd.ExcelFile(xlsx_path).sheet_names
                break
            elif option == len(subject_list):
                return
            else:
                print("Lựa chọn không phù hợp")
        except:
            print("Lỗi: Sai định dạng \nHãy nhập lại", end="")
    
    
    # trả về đường dẫn file excel, list môn học, lựa chọn
    return  xlsx_path,subject, class_sheet,option

## CHỌN LỚP
def pick_class(class_sheet):
    print("Hãy chọn lớp muốn vẽ đồ thị: ")
    for i in range(0,len(class_sheet)):
         print((f"({i}) {class_sheet[i]}"))
    print(f"({len(class_sheet)}) So sánh 2 lớp")
    print(f"({len(class_sheet) + 1 }) quay lại")
    num_class = int(input("-->"))
    return num_class
## Chọn lớp để so sánh
def pick_class2(class_sheet):
    while True:
        try:
            print("Hãy chọn 2 lớp muốn so sánh:")
            for i in range(len(class_sheet)):
                print((f"({i}) {class_sheet[i]}"))
            num_class1, num_class2 = map(int,input( "Nhập số tương ứng với lớp và cách nhau bằng 1 khoảng trắng :").split(" "))
            if (num_class1 and num_class2) in range(len(class_sheet)):
                break
            else:
                print("Lỗi: nhập giá trị ngoài khoảng cho phép")
        except:
            print("Lỗi: Nhập sai định dạng")
    return num_class1, num_class2


## CHỌN HỌC KỲ---------s-----------------------------------------------------------------------------------
def pick_semester(mess = "quay lại"):
    while True:
            semester = input(f"Hãy chọn cột điểm: \
                             \n(0) Giữa kỳ \
                             \n(1) Cuối kỳ \
                             \n(2) Cả hai \
                             \n(3) {mess} \
                             \n-->" )
            if semester == "0":
                semester = "Giữa kỳ"
                break
            elif semester == "1":
                semester = "Cuối kỳ"
                break
            elif semester == "2" :
                semester = "Cả hai"
                break
            elif semester == "3":
                break
            else:
                print("Hãy nhập đúng giá trị đã cho (0),(1),(2),(3)")
    return semester

## LẤY DỮ LIỆU 1 colum--------------------------------------------------------------------------------------------
    # 1 sheet 1 colum
def colum_data1_1c(xlsx_path,colum_name,class_):
    data_excel = pd.read_excel(xlsx_path,class_)
    data_score = data_excel[colum_name].tolist()
    return data_score
    # 2 sheet 1 colum
def colum_data1_2c(xlsx_path,colum_name,class_1,class_2):
    data_excel1 = pd.read_excel(xlsx_path,class_1)
    data_excel2 = pd.read_excel(xlsx_path,class_2)
    data_score1 = data_excel1[colum_name].tolist()
    data_score2 = data_excel2[colum_name].tolist()
    return data_score1,data_score2

## LẤY DỮ LIỆU 2 colums--------------------------------------------------------------------------------------------
    # 1 sheet 2 colums
def colum_data2_1c(xlsx_path,colum_name,class_):
        if colum_name == "Cả hai":
            colum_name1 = "Giữa kỳ"
            colum_name2 = "Cuối kỳ"
            data_excel = pd.read_excel(xlsx_path,class_)
            data_mid_sem_1 = data_excel[colum_name1].tolist()
            data_end_sem_1 = data_excel[colum_name2].tolist()
        return data_mid_sem_1 , data_end_sem_1 , colum_name1 , colum_name2

    # 2 sheet 2 colums
def colum_data2_2c(xlsx_path,colum_name,class_1,class_2):
        if colum_name == "Cả hai":
            colum_name1 = "Giữa kỳ"
            colum_name2 = "Cuối kỳ"

            data_excel1 = pd.read_excel(xlsx_path,class_1)
            data_excel2 = pd.read_excel(xlsx_path,class_2)

            data_mid_sem_1 = data_excel1[colum_name1].tolist()
            data_mid_sem_2 = data_excel2[colum_name1].tolist()

            data_end_sem_1 = data_excel1[colum_name2].tolist()
            data_end_sem_2 = data_excel2[colum_name2].tolist()
        return data_mid_sem_1 , data_mid_sem_2 ,data_end_sem_1 ,data_end_sem_2,colum_name1 , colum_name2

## Đếm khoảng điểm cho 1 học kỳ
def range_data1(data_score): 
    # đếm số phần tử thõa mãn khoảng 5 khoảng cách đều từ 0 - 10 ( 0 - 2.5 - 5 - 7.5 - 10)
    range_ , bins = np.histogram(data_score,np.linspace(0,10,5))
    return range_, bins
## Đếm khoảng điểm cho 2 học kỳ 
def range_data2(data_range_1 , data_range_2): 
    # đếm số phần tử thõa mãn khoảng 5 khoảng cách đều từ 0 - 10 ( 0 - 2.5 - 5 - 7.5 - 10)
    range_1 , binss1 = np.histogram(data_range_1,np.linspace(0,10,5))
    range_2 , binss2 = np.histogram(data_range_2,np.linspace(0,10,5))
    return range_1, binss1, range_2 , binss2

# HÀM ĐẾM SỐ ĐIỂM CỦA HỌC KỲ --------------------------------------------------------------------------------------------
def count_score(data_score):
    # dữ liệu lấy từ colum data trả về dạng dictionary
    data_dict = {}
    # list rỗng để có thể thâm các value của data_dict 
    value_list= []
    # Tạo danh sách các cặp (phần tử, số lần xuất hiện)
    for element in data_score:
        data_dict[element] = data_dict.get(element, 0) + 1
    # sort theo điểm từ bé tới lớn và trả vào sort_list
    sort_list = sorted(data_dict)
    # lấy value của từng key trong data dict
    for i in sort_list: 
        value_list.append(data_dict[i])
    return sort_list,value_list

##### -----------------------------CHART-----------------------------------------------------------------------------------------------------------------------------------------------------------

# Scatter chart cho 1 đối tượng--------------------------------------------------------------------------------------------
def scatter_chart1(x_data , y_data , subject , class_  , colum_name1 = any , colum_name2 = any, semester = any ):
    x = x_data
    y = y_data
    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    
    #ax.plot(x,y);
    if (colum_name1 and colum_name2 ) == any:

        size = []
        for i in range(len(y)) :
            size.append(y[i]*20)
        colors = x
        ax.set_xlabel ("Điểm", fontsize = 14, fontweight = "bold", color = "gray" ) 
        ax.set_ylabel ("Count", fontsize = 14, fontweight = "bold", color = "gray")
        ax.set_title(f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_} ",
                      fontsize = 20, fontweight = "bold", color = "#7F4CD3", pad = 20 )
        
        chart= ax.scatter(x,y,s= size,alpha = 0.7, c= colors, cmap  = 'viridis');
        fig.colorbar(chart);
    elif semester  == any:

        colors = []
        for i in range(len(x)):
            colors.append((x[i]*0.3+y[i]*0.7))

        size = []
        for i in range(len(x)):
            size.append((x[i]+y[i]))

        ax.set_xlabel ( f"{colum_name1}", fontsize = 14,
                        fontweight = "bold", color = "gray" ) 
        ax.set_ylabel ( f"{colum_name2}", fontsize = 14,
                       fontweight = "bold", color = "gray")
        ax.set_title(f"Biểu đồ thể hiện sự phân bố điểm môn {subject} của lớp {class_}",
                      fontsize = 20, fontweight = "bold", color = "#7F4CD3", pad = 20)

        chart= ax.scatter(x,y,s= size,alpha = 0.7, c= colors, cmap  = 'viridis');
        fig.colorbar(chart).set_label( "Điểm tổng kết môn",fontsize = 14,fontweight = "bold", color = "gray");
    
    plt.show();

## scatter 2 đối tượng
def scatter_chart2(data_x_1 , data_x_2 ,data_y_1 ,data_y_2, subject,class_1 , class_2 ,
                    colum_name1 = any, colum_name2 = any, semester = any):
    x1 , y1 = data_x_1, data_y_1
    x2 , y2 = data_x_2, data_y_2
    print (x1)
    print (y1)
    
    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, (ax1,ax2) = plt.subplots(ncols = 2)
## 1 Học kỳ 
    if (colum_name1 and colum_name2 ) == any :

        size1 = []
        for i in range(len(y1)) :
            size1.append(y1[i]*20)
        colors1 = x1 

        size2 = []
        for i in range(len(y2)) :
            size2.append(y2[i]*20)
        colors2 = x2

        ax1.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax1.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
        ax1.set_title(f"Lớp {class_1}", fontsize = 16,
                       fontweight = "bold" )
        
        ax2.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax2.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
        ax2.set_title(f"Lớp {class_2}", fontsize = 16, 
                      fontweight = "bold" )

        fig.suptitle(f"So sánh sự phân tán điểm {semester} môn {subject} của 2 lớp",
                      ha = 'center', va = "top",
                    fontsize = 20, fontweight = 'bold',
                    color = "#7F4CD3"
                    )

        chart1 = ax1.scatter(x1,y1,s= size1, c = colors1, alpha = 0.7, cmap  = 'viridis');
        chart2 = ax2.scatter(x2,y2,s= size2, c = colors2, alpha = 0.7, cmap  = 'viridis');

        fig.colorbar(chart1 and chart2)
## 2 học kỳ
    elif semester == any:
        colors1 = []
        for i in range(len(x1)):
            colors1.append((x1[i]*0.3+y1[i]*0.7))
        colors2 = []
        for i in range(len(x2)):
            colors2.append((x2[i]*0.3+y2[i]*0.7))

        size1 = []
        for i in range(len(x1)):
            size1.append((x1[i]+y1[i]))
        size2 = []
        for i in range(len(x2)):
            size2.append((x2[i]+y2[i]))
    # label 1
        ax1.set_xlabel ( f"{colum_name1}", fontsize = 12,
                        fontweight = "bold", color = "gray" ) 
        ax1.set_ylabel ( f"{colum_name2}", fontsize = 12,
                       fontweight = "bold", color = "gray")
    # title 1
        ax1.set_title(f"Lớp {class_1}", fontsize = 16, 
                      fontweight = "bold" )
    # label 2 
        ax2.set_xlabel ( f"{colum_name1}", fontsize = 12,
                        fontweight = "bold", color = "gray" ) 
        ax2.set_ylabel ( f"{colum_name2}", fontsize = 12,
                       fontweight = "bold", color = "gray")
    # title 2
        ax2.set_title(f"Lớp {class_2}", fontsize = 16,
                       fontweight = "bold" )
    # suptitle tổng
        fig.suptitle(f"So sánh sự phân tán điểm môn {subject}", 
                    ha = 'center', va = "top",
                    fontsize = 20, fontweight = 'bold',
                    color = "#7F4CD3"
                    )
    # chart
        chart1 = ax1.scatter(x1,y1,s= size1, c = colors1, alpha = 0.7, cmap  = 'viridis');
        chart2 = ax2.scatter(x2,y2,s= size2, c = colors2, alpha = 0.7, cmap  = 'viridis');
    # colorbar
        fig.colorbar(chart1 and chart2).set_label( " Điểm trung bình 2 kỳ", 
                                                  fontsize = 14, fontweight = "bold", color = "gray" )
    
    plt.show();
        
## Hist chart--------------------------------------------------------------------------------------------
def hist_chart1(data_hist,semester,class_,subject):
    plt.style.use ('seaborn-v0_8-whitegrid')
    # plt.legend();
    fig, ax = plt.subplots()
    ax.hist(data_hist, color = "#00C9A7" ,edgecolor = "white")

    ax.set_title(f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_} ",
                      fontsize = 20, fontweight = "bold", color = "#7F4CD3", pad = 20 )
    ax.set_xlabel ("Điểm", fontsize = 14, fontweight = "bold", color = "gray" ) 
    ax.set_ylabel ("Count", fontsize = 14, fontweight = "bold", color = "gray")
    
        
    plt.show();

## Hist chart 2 lớp | 2 kỳ--------------------------------------------------------------------------------------------
def hist_chart2(data_hist1 , data_hist2 ,subject, colum_name1 = any , colum_name2 = any,class_1 = any ,class_2 = any, class_ = any, semester = any):
    plt.style.use ('seaborn-v0_8-whitegrid')
    # plt.legend();
    fig, (ax1,ax2) = plt.subplots(1,2, figsize = (20,10))
    ax1.hist(data_hist1, color = "#00C9A7" ,edgecolor = "white")
    ax2.hist(data_hist2, color = "#00C9A7" ,edgecolor = "white")
## Trường hợp cho 2 lớp
    if ( class_ and colum_name1 and colum_name2) == any:
        fig.suptitle(f"Biểu đồ so sánh điểm {semester} môn {subject} của 2 lớp ",
                    ha = 'center', va = 'top',
                    fontsize = 20, fontweight = 'bold',
                    color = "#007BFF")
    
        ax1.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax1.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
        ax1.set_title(f"Lớp {class_1}", fontsize = 16,
                       fontweight = "bold" )
        
        ax2.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax2.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
        ax2.set_title(f"Lớp {class_2}", fontsize = 16, 
                      fontweight = "bold" )
## Trường hợp cho 2 học kỳ
    elif (semester and class_1  and class_2 ) == any:
        fig.suptitle(f"Biểu đồ so sánh điểm {colum_name1} và {colum_name2} môn {subject} của lớp {class_}  ",
                    ha = 'center', va = 'top',
                    fontsize = 20, fontweight = 'bold',
                    color = "#007BFF")
        ax1.set(title = f"{colum_name1}",
            xlabel = "Điểm",
            ylabel = "Count")
        ax2.set(title = f"{colum_name2}",
            xlabel = "Điểm",
            ylabel = "Count")
        
        # label 1
        ax1.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax1.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
    # title 1
        ax1.set_title(f"{colum_name1}", fontsize = 16, 
                      fontweight = "bold" )
    # label 2 
        ax2.set_xlabel ("Điểm", fontsize = 14, 
                        fontweight = "bold", color = "gray" ) 
        ax2.set_ylabel ("Số lần xuất hiện", fontsize = 14, 
                        fontweight = "bold", color = "gray")
    # title 2
        ax2.set_title(f"{colum_name2}", fontsize = 16,
                       fontweight = "bold" )
    plt.show();

## pie chart 1 đối tượng
def pie_chart1(range_, bins, semester , class_ , subject ):
    labels = []
    size = [valu for valu in range_ if valu !=0]
    colors = ["#ee4035", "#7bc043", "#0392cf", "#f37736" , "#fdf498"]
    for i in range(len(range_)):
        if range_[i] != 0:
            labels.append(f"{bins[i]} - {bins[i+1]}")

    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    ax.pie(size,colors = colors,autopct='%1.1f%%',counterclock=True);
    ax.set_title(f"Điểm {semester} môn {subject} của lớp {class_} ",
            fontsize = 20, fontweight = "bold", color = "green", pad = 5 )
    fig.legend(labels,
                title = "Khoảng điểm",
                loc = "center right",
                frameon=True
                )
    plt.show();

## pie chart 2 đối tượng
def pie_chart2(range_1, binss1, range_2 , binss2 ,subject , 
               colum_name1 = any , colum_name2 = any , class_ = any, class_1 = any, class_2 = any, semester = any ):
    # sort_list,value_list = count_score(colum_data())
    labels_1 = []
    size1 = [valu for valu in range_1 if valu !=0]

    labels_2 = []
    size2 = [valu for valu in range_2 if valu !=0]
    
    colors = [ "#ee4035", "#7bc043", "#0392cf", "#f37736" , "#fdf498"]

    for i in range(len(range_1)):
        if range_1[i] != 0:
            labels_1.append(f"{binss1[i]} - {binss1[i+1]}")

    for i in range(len(range_2)):
        if range_2[i] != 0:
            labels_2.append(f"{binss2[i]} - {binss2[i+1]}")
    # gộp các phần tử của label_1 và labels_2 thành 1 labels tổng và loại bỏ các phần tử trùng
    labels = list(set(labels_1 + labels_2))
    
    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, (ax1,ax2) = plt.subplots(ncols = 2)
    ax1.pie(size1, colors = colors, autopct='%1.1f%%', counterclock=False, startangle=90);

    ax2.pie(size2, colors = colors, autopct='%1.1f%%', counterclock=False, startangle=90);

## Trường hợp cho 2 lớp
    if ( class_ and colum_name1 and colum_name2) == any:

        ax1.set_title(class_1, va = 'bottom',
                   fontsize = 14, fontweight= 'bold',
                     color='gray', pad = 5)
        
        ax2.set_title( class_2, va = 'bottom',
                       fontsize = 14, fontweight= 'bold',
                         color='gray', pad = 5)
    
        fig.suptitle(f"Biểu đồ so sánh điểm {semester} của 2 lớp",
                    ha = 'center', va = "top",
                    fontsize = 20, fontweight = 'bold',
                    color = "green"
                    )
        
        fig.legend(labels,
                    title = "Khoảng điểm",
                    loc = "center right",
                    frameon = True
                    )
## Trường hợp cho 2 học kỳ
    elif (semester and class_1  and class_2 ) == any:
        ax1.set_title(colum_name1, va = 'bottom',
                   fontsize = 14, fontweight= 'bold',
                     color='gray', pad = 5) 
        ax2.set_title( colum_name2, va = 'bottom',
                       fontsize = 14, fontweight= 'bold',
                         color='gray', pad = 5)
        fig.suptitle(f" Môn: {subject}\nLớp: {class_}",
                    ha = 'center',va = "top",
                    fontsize = 20, fontweight = 'bold',
                    color = "green")
        fig.legend(labels,
                    title = "Khoảng điểm",
                    loc = "center right",
                    frameon = True
                    )
    plt.show();

def one_object(num_class,class_sheet,subject,xlsx_path):
    ## gán biến tên lớp
        class_=class_sheet[num_class]
    ## Chọn học kỳ và gán biến tên học kỳ
        semester = pick_semester(mess = "Nhập lại")
    ## 2 học kỳ
        if semester == "Cả hai":
        # gán biến lần lượt: data học kỳ số 1, data học kỳ số 2, tên học kỳ số 1, tên học kỳ số 2 được lấy ra từ hàm colum
            data_sem1 , data_sem2 , colum_name1 , colum_name2 = colum_data2_1c(xlsx_path,semester,class_)
            while True:
                choose = input("Chọn kiểu biểu đồ: \
                                   \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                                   \n(2) Histogram - Biểu đồ tần suất \
                                   \n(3) Pie chart - Biểu đồ tròn \
                                   \n(4) Quay lại\
                                   \n--> ")
            # Scatter chart 
                if choose == "1":
                    scatter_chart1(data_sem1,data_sem2,subject,class_,colum_name1,colum_name2)
                    break
            # histogram
                elif choose == "2":
                    hist_chart2(data_hist1 = data_sem1,
                                data_hist2 = data_sem2,
                                subject = subject,
                                colum_name1 = colum_name1,
                                colum_name2 = colum_name2,
                                class_ = class_)
                    break
            # Pie chart 
                elif choose == "3":
                    range_1, binss1, range_2 , binss2 = range_data2(data_sem1 , data_sem2)
                    pie_chart2(range_1, binss1, range_2 , binss2 ,subject , 
                               colum_name1 , colum_name2,class_ )
                    break
                elif choose == "4":
                    one_object(num_class,class_sheet,subject,xlsx_path)
                    break
                else:
                    print("Hãy nhập đúng giá trị phù hợp")
    ## 1 học kỳ
        elif semester == "Cuối kỳ" or semester =="Giữa kỳ":
            # lấy cột điểm
            data_score = colum_data1_1c(xlsx_path,semester,class_)
                # chọn kiểu biểu đồ
            while True:
                choose = input("Chọn kiểu biểu đồ: \
                               \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                               \n(2) Histogram - Biểu đồ tần suất \
                               \n(3) Pie chart - Biểu đồ tròn \
                               \n(4) Quay lại\
                               \n--> ")
            ## scatter     
                if choose == "1":
                # sort key và value
                    sort_list,value_list = count_score(data_score)
                    scatter_chart1(sort_list,value_list,subject,class_,semester = semester)
                    break
            ## histogram
                elif choose == "2":
                    hist_chart1(data_score,semester,class_,subject)
                    break
            ## Pie
                elif choose == "3":
                    range_, bins = range_data1(data_score)
                    pie_chart1(range_,bins ,semester ,class_ ,subject)
                    break
                elif choose == "4":
                    one_object(num_class,class_sheet,subject,xlsx_path)
                    break
                else:
                    print("Hãy nhập đúng giá trị phù hợp")
    ## Quay lại
        elif semester == "3":
            one_object(num_class,class_sheet,subject,xlsx_path)
def two_object(class_sheet,xlsx_path,subject):
# chọn 2 đối tượng muốn vẽ
    num_class1, num_class2 = pick_class2(class_sheet = class_sheet)
# gán tên lớp vào class_1, class_2
    class_1 = class_sheet[num_class1]
    class_2 = class_sheet[num_class2]
    print(class_1,class_2)
    semester = pick_semester()
## 2 học kỳ
    if semester == "Cả hai":
        data_mid_sem_1, data_mid_sem_2, data_end_sem_1, data_end_sem_2, \
        colum_name1, colum_name2 = colum_data2_2c(xlsx_path, semester, class_1, class_2)
        while True:
            choose = input("Ở lựa chọn này chúng tôi chỉ hỗ trợ vẽ 1 biểu đồ \
                            \n Chọn:\
                            \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố\
                            \n(2) Quay lại phần chọn lớp\
                            \n--> ")
        # Scater 
            if choose == "1":
                scatter_chart2(data_mid_sem_1 , data_mid_sem_2 ,data_end_sem_1 ,data_end_sem_2, subject,
                               class_1 = class_1, class_2 = class_2, colum_name1 = colum_name1, colum_name2 = colum_name2)
                break
        # Quay lại
            elif choose == "2":
                two_object(class_sheet,xlsx_path,subject)
                break
            else:
                print("Hãy nhập đúng giá trị phù hợp")
## 1 học kỳ
    elif semester == "Cuối kỳ" or semester =="Giữa kỳ":
    # Lấy data của 2 lớp
        data_score1,data_score2 = colum_data1_2c(xlsx_path,semester,class_1,class_2) 
        while True:
            choose = input("Chọn kiểu biểu đồ: \
                            \n(1) Scatter chart - Biểu đồ thể hiện sự phân bố \
                            \n(2) Histogram - Biểu đồ tần suất \
                            \n(3) Pie chart - Biểu đồ tròn \
                            \n(4) Quay lại\
                            \n--> ")
        # Scater 
            if choose == "1":
                sort_list1, value_list1 = count_score(data_score1)
                sort_list2, value_list2 = count_score(data_score2)
                scatter_chart2(sort_list1,sort_list2, value_list1 , value_list2,
                                subject = subject,class_1 = class_1 , class_2 = class_2 , semester = semester)
                break
        # Histogram
            elif choose == "2":
                hist_chart2(data_hist1 = data_score1 ,
                            data_hist2 = data_score2,
                            subject = subject,
                            class_1 = class_1,
                            class_2 = class_2,
                            semester = semester)
                break
        # Pie chart 
            elif choose == "3":
            # gán dữ liệu gồm 2 list số liệu và 2 list khoảng lấy số liệu
                range_1, binss1, range_2 , binss2 = range_data2(data_range_1 = data_score1,
                                                                data_range_2 = data_score2 )
                pie_chart2( range_1, binss1, range_2 , binss2,
                           subject = subject, class_1 = class_1,
                           class_2 = class_2,
                           semester = semester)      
                break
        # Quay lại
            elif choose == "4":
                two_object(class_sheet,xlsx_path,subject)
                break
            else:
                print("Hãy nhập đúng giá trị phù hợp")
## Quay lại
    elif semester == "3":
        two_object(class_sheet,xlsx_path,subject)
