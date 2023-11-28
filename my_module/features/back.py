def back_step(func) :
    option = input("Quay lại \n(0) Không\n(1) Có\n")
    match option :
        case "0" :
            print("END")
        case "1" :
            func()