### tại vì deo sài cái back kia đc nên tạo cái này bù qua
def back_step2(*args,name_function0, name_function1, mess) :
    #Quay lại với lựa chọn
    while True:
        try:
            option = input(f"{mess}:\n(0) Không\n(1) Có\n-> ")
            if (option == "0") :
                print('\n')
                return name_function0(*args)
            elif (option == "1") :
                print('\n')
                return name_function1(*args)
        except:
            print("Lựa chọn không phù hợp")