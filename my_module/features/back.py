def back_step(func) :
    while True:
        option = input("Thoát chương trình\n(0) Không\n(1) Có\n-> ")
        if (option == "0") :
            return func()
        elif (option == "1") :
            break
        print("Lựa chọn không phù hợp")
    print("Chương trình kết thúc")