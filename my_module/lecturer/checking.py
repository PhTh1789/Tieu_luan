from my_module.features import loading_mess


def lecture_checking(data, lecture_col_name : str,password_col_name : str) :
    while True :
        lecture_name = input("Họ và tên: ")
        password_input = input("Mật khẩu: ")
        for name, password in zip(data[lecture_col_name], data[password_col_name]) :
            if lecture_name == str(name) and password_input == str(password) :
                print("Đăng nhập thành công\n")
                return lecture_name
        print("Tài khoản hoặc mật khẩu không chính xác")

        loading_mess(3, 1)