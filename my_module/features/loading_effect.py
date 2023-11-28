from time import sleep

# Hàm với hai đối số count : số dấu chấm; step : khoảng thời gian hiển thị giữa các chấm
def loading_mess(count : int, step : int, mess = "Đang tải") :
    print(mess , end="", flush=True)
    for item in range(count) :
        sleep(step)
        if item == count - 1 :
            print(".")
            break
        print(".", end="", flush=True)