from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
import os

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
def get_coree( score_folder_path) :
    subject_list = os.listdir(score_folder_path)
    # Lấy danh sách các folder có trong đường dẫn
    print("Chọn môn: ")
    # In danh sách tên các folder 
    for index, subject in zip(range(0, len(subject_list)), subject_list) :
        print(f"({index})", subject)
    # input chọn môn theo số
    while True :
        try:
            option = int(input("-> "))
            #Nếu lựa chọn nằm trong index của subject_list thì được xem là phù hợp
            if option in range(0, len(subject_list)) :
                break
            else:
                print("Lựa chọn không phù hợp")
        except:
            print("Lỗi: Sai định dạng \nHãy nhập lại", end="")
    # đường dẫn tới file excel sau khi chọn môn
    xlsx_path = score_folder_path + f"\\{subject_list[int(option)]}" + f"\\{subject_list[int(option)]}.xlsx"
    # trả về đường dẫn file excel, list môn học, lựa chọn
    return  xlsx_path,subject_list, option

## CHỌN HỌC KỲ--------------------------------------------------------------------------------------------
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

# LẤY DỮ LIỆU 1 CỘT--------------------------------------------------------------------------------------------
def colum_data1(xlsx_path,colum_name,class_):
        if colum_name == "Giữa kỳ" or colum_name == "Cuối kỳ":
            data_excel = pd.read_excel(xlsx_path,class_)
            data_score = data_excel[colum_name].tolist()
        return data_score

# LẤY DỮ LIỆU 2 CỘT--------------------------------------------------------------------------------------------
def colum_data2(xlsx_path,colum_name,class_):
        # gán biến của get_scoree vào
        if colum_name == "Cả hai":
              colum_name1 = "Giữa kỳ"
              colum_name2 = "Cuối kỳ"
              data_excel = pd.read_excel(xlsx_path,class_)
              data_sem1 = data_excel[colum_name1].tolist()
              data_sem2 = data_excel[colum_name2].tolist()

        #Đọc dữ liệu của cột colum_name ( Giữa kỳ / Cuối kỳ )
        return data_sem1 , data_sem2 , colum_name1 , colum_name2

## Đếm khoảng điểm cho 1 học kỳ
def range_data1(data_score): 
    # đếm số phần tử thõa mãn khoảng 5 khoảng cách đều từ 0 - 10 ( 0 - 2.5 - 5 - 7.5 - 10)
    range_ , bins = np.histogram(data_score,np.linspace(0,10,5))
    return range_, bins
## Đếm khoảng điểm cho 2 học kỳ 
def range_data2(data_sem1 , data_sem2): 
    # đếm số phần tử thõa mãn khoảng 5 khoảng cách đều từ 0 - 10 ( 0 - 2.5 - 5 - 7.5 - 10)
    range_1 , binss1 = np.histogram(data_sem1,np.linspace(0,10,5))
    range_2 , binss2 = np.histogram(data_sem2,np.linspace(0,10,5))
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

##### -----------------------------CHART---------------------------------------------------------------

# Scatter chart cho 1 kỳ--------------------------------------------------------------------------------------------
def scatter_chart1(sort_list,value_list,semester,class_,subject):
    # sort_list,value_list = count_score(colum_data())
    x = sort_list
    y = value_list
    colors = np.random.rand(len(x))
    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    chart= ax.scatter(x,y,s= 15,c= colors, cmap  = 'viridis');
    #ax.plot(x,y);
    ax.set(title = f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_} ",\
           xlabel = "Điểm",\
            ylabel = "Count",\
            # xticks = (x),\
          )
    fig.colorbar(chart);
    plt.show();

# Scatter chart cho 2 đối tượng --------------------------------------------------------------------------------------------
def scatter_chart2(data_sem1,data_sem2,colum_name1,colum_name2,semester,class_,subject):
    x = data_sem1
    y = data_sem2
    colors = np.random.rand(len(x))
    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    chart = ax.scatter(x,y,s= 15, c = colors, cmap  = 'viridis');
    # ax.plot(x,y);
    ax.set(title = f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_}",\
           xlabel = f"{colum_name1}",\
            ylabel = f"{colum_name2}"\
            )
    fig.colorbar(chart);
    plt.show();
    
# BAR CHART--------------------------------------------------------------------------------------------
# def bar_chart(sort_list,value_list,semester,class_,subject):
#     x = sort_list
#     y = value_list
#     plt.style.use ('seaborn-v0_8-whitegrid')
#     # plt.legend();
#     fig, ax = plt.subplots()
#     ax.bar(x,y,width= 0.4,align = "center")
#     ax.set(title = f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_}",\
#             xlabel = "Điểm",\
#             ylabel = "Count")
#     plt.show()
    
## Hist chart--------------------------------------------------------------------------------------------
def hist_chart1(data_score,semester,class_,subject):
    plt.style.use ('seaborn-v0_8-whitegrid')
    # plt.legend();
    fig, ax = plt.subplots()
    ax.hist(data_score, color = "#00C9A7" ,edgecolor = "white")
    ax.set(title = f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_} ",\
            xlabel = "Điểm",\
            ylabel = "Count")
    # for i in range(len(x)):
    #     ax.text(i, y[i], str(y[i]), ha='center', va='bottom')
    plt.show();

## Hist chart 2 lớp | 2 kỳ--------------------------------------------------------------------------------------------
def hist_chart2(data_sem1 , data_sem2 , colum_name1 , colum_name2,class_,subject):
    plt.style.use ('seaborn-v0_8-whitegrid')
    # plt.legend();
    fig, (ax1,ax2) = plt.subplots(1,2, figsize = (20,10))
    ax1.hist(data_sem1, color = "#00C9A7" ,edgecolor = "white")
    ax1.set(title = f"{colum_name1}",\
            xlabel = "Điểm",\
            ylabel = "Count")
    ax2.hist(data_sem2, color = "#00C9A7" ,edgecolor = "white")
    ax2.set(title = f"{colum_name2}",\
            xlabel = "Điểm",\
            ylabel = "Count")
    fig.suptitle(f"Biểu đồ so sánh điểm {colum_name1} và {colum_name2}\
                \nmôn {subject}\
                \nlớp {class_} ",\
                ha = 'center', va = 'top',\
                fontsize = 20, fontweight = 'bold',\
                color = "blue")
    plt.show();

## pie chart 1 đối tượng
def pie_chart1(range_,bins ,semester ,class_ ,subject ):
    # sort_list,value_list = count_score(colum_data())
    labels = []
    size = [valu for valu in range_ if valu !=0]
    colors = ["#ee4035", "#7bc043 ", "#0392cf", "#f37736" , "#fdf498"]
    for i in range(len(range_)):
        if range_[i] != 0:
            labels.append(f"{bins[i]} - {bins[i+1]}")

    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots()
    ax.pie(size,labels = labels,colors = colors,autopct='%1.1f%%',counterclock=True);
    ax.set(title = f"Biểu đồ thể hiện sự phân bố điểm {semester} môn {subject} của lớp {class_} ")
    plt.show();

## pie chart 2 đối tượng
def pie_chart2(range_1, binss1, range_2 , colum_name1 , colum_name2, binss2 ,class_ ,subject ):
    # sort_list,value_list = count_score(colum_data())
    labels1 = []
    size1 = [valu for valu in range_1 if valu !=0]

    labels2 = []
    size2 = [valu for valu in range_2 if valu !=0]
    
    colors = [ "#ee4035", "#7bc043", "#0392cf", "#f37736" , "#fdf498"]

    for i in range(len(range_1)):
        if range_1[i] != 0:
            labels1.append(f"{binss1[i]} - {binss1[i+1]}")

    for i in range(len(range_2)):
        if range_2[i] != 0:
            labels2.append(f"{binss2[i]} - {binss2[i+1]}")
    
    labels = list(set(labels1 + labels2))
    print(labels1, labels2 , labels)

    plt.style.use ('seaborn-v0_8-whitegrid')
    fig, (ax1,ax2) = plt.subplots(ncols = 2)
    ax1.pie(size1, colors = colors, autopct='%1.1f%%', counterclock=False, startangle=90);
    ax1.set_title(colum_name1, va = 'bottom',
                   fontsize = 14, fontweight= 'bold',
                     color='gray', pad = 5) 

    ax2.pie(size2, colors = colors, autopct='%1.1f%%', counterclock=False, startangle=90);
    ax2.set_title( colum_name2, va = 'bottom',
                   fontsize = 14, fontweight= 'bold',
                     color='gray', pad = 5)

    fig.suptitle(f"Biểu đồ so sánh điểm {colum_name1} và {colum_name2}",
                 va = 'bottom',
                fontsize = 20, fontweight = 'bold',
                color = "green")
    fig.suptitle(f" Môn: {subject}\nLớp: {class_}",
                x=0.1, y=0.9,
                fontsize = 20, fontweight = 'bold',
                color = "green")
    
    fig.legend(labels,
                title = "Khoảng điểm",
                loc = "center right",
                frameon=True
                )
    plt.show();

