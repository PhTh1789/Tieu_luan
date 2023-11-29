def back_step(func) :
    while True:
        option = input("Quay lại giao diện chính\n(0) Không\n(1) Có\n")
        if (option == "0") :
            break
        elif (option == "1") :
            return func()
        print("Lựa chọn không phù hợp")