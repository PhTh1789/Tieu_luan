from my_module.features import loading_mess


def lecture_checking(data, lecture_col_name : str,password_col_name : str) :
    while True :
        lecture_id = input("Mã giảng viên: ")
        password_input = input("Mật khẩu: ")
        for id, password in zip(data[lecture_col_name], data[password_col_name]) :
            if lecture_id == str(id) and password_input == str(password) :
                print("Đăng nhập thành công\n")
                return lecture_id
        print("Tài khoản hoặc mật khẩu không chính xác")

        loading_mess(3, 1)