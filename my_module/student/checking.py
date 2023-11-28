from my_module.features import loading_mess


def check(data, mssv_col_name : str,password_col_name : str) :
    while True :
        mssv_input = input("MSSV: ")
        password_input = input("Mật khẩu: ")
        for mssv, password in zip(data[mssv_col_name], data[password_col_name]) :
            if mssv_input == str(mssv) and password_input == str(password) :
                print("Đăng nhập thành công")
                return mssv_input
        print("Tài khoản hoặc mật khẩu không chính xác")

        loading_mess(3, 1)