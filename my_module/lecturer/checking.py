from my_module.features import loading_mess


def lecturer_checking(data, lecturer_col_name : str,password_col_name : str) :
    while True :
        lecturer_id = input("Mã giảng viên: ")
        password_input = input("Mật khẩu: ")
        for id, password in zip(data[lecturer_col_name], data[password_col_name]) :
            if lecturer_id == str(id) and password_input == str(password) :
                print("Đăng nhập thành công\n")
                return lecturer_id
        print("Tài khoản hoặc mật khẩu không chính xác")

        loading_mess(3, 1)