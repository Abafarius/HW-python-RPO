def get_digit_merger(num1,num2,num3):
    if not type(num1) is int and type(num2) is int and type(num3) is int:
        print("argument must be integer")
        #VN: функция не должна ничего печатать и заниматься проверкой аргументов, если указано, что они num
    else:
        string_num1 = str(num1)
        string_num2 = str(num2)
        string_num3 = str(num3)
        pre_result = string_num1 + string_num2 + string_num3
        print("type of pre_result: ", type(pre_result))
        #VN: ^^^^^^ делайте функции без побочных эффектов
        try:
            result = int(pre_result)
            #VN: если все num правильного типа, то исключений, вроде бы, не должно возникнуть
        except ValueError:
            print("Enter integer number!")
            exit()
            #VN: ^^^^^ делайте функции без побочных эффектов! Функция не должна решать, завершать ли программу!
        print("type of result: ", type(result))
        print("The result is: ", result)
        #VN:  снова побочные эффекты - функция не должна ничего печатать, если это не её прямое назначение!
    return result
data1 = input("Enter integer number1: ")
data2 = input("Enter integer number2: ")
data3 = input("Enter integer number3: ")


try:
    get_digit_merger(data1,data2,data3)
except TypeError:
    print("There must be 3 arguments!")
    exit()