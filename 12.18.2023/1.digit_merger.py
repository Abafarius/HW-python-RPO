def get_digit_merger(num1,num2,num3):
    if not type(num1) is int and type(num2) is int and type(num3) is int:
        print("argument must be integer")
    else:
        string_num1 = str(num1)
        string_num2 = str(num2)
        string_num3 = str(num3)
        pre_result = string_num1 + string_num2 + string_num3
        print("type of pre_result: ", type(pre_result))
        try:
            result = int(pre_result)
        except ValueError:
            print("Enter integer number!")
            exit()
        print("type of result: ", type(result))
        print("The result is: ", result)
    return result
data1 = input("Enter integer number1: ")
data2 = input("Enter integer number2: ")
data3 = input("Enter integer number3: ")


try:
    get_digit_merger(data1,data2,data3)
except TypeError:
    print("There must be 3 arguments!")
    exit()