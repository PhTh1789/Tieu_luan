from my_module.lecturer.menu import *
from my_module.lecturer.back2 import *
from my_module.features.back import back_step
# from menu import *
# from back2 import back_step
#### MAIN--------------------------------------------------------------------------------------------
def get_chart():
### Chọn Môn
    try:
        xlsx_path,subject, class_sheet,option= pick_subject()
        if option == "thoat":
            return
        else:
        ### CHỌN Đối tượng
            while True:
                try:
                    num_class = pick_class (class_sheet)
                ### 1 Đối tượng
                    if num_class in range(len(class_sheet)):
                        one_object(num_class = num_class,
                                   class_sheet = class_sheet,
                                   subject = subject,
                                   xlsx_path = xlsx_path)
                        break
                ### 2 Đối tượng--------------------------------------------------------------------------------------------
                    elif num_class == len(class_sheet):
                         two_object(class_sheet = class_sheet,
                                    xlsx_path = xlsx_path,
                                    subject = subject)
                         break
                ### Quay lại
                    elif num_class == (len(class_sheet) + 1):
                        back_step(name_function = get_chart, mess = " Bạn muốn quay lại ? ")
                        break
                    else:
                        print("Chỉ nhập số trong khoảng cho trước")
            ### Trường hợp sai định dạng
                except ValueError :
                        print("Lỗi: Nhập sai định dạng")
    except:
        return