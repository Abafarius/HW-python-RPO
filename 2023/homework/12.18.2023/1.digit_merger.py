def get_digit_merger(num1,num2,num3):
    merging = num1+num2+num3
    result = int(merging)
    return result

data1 = input("Enter integer number1: ")
try:
    digit1  = int(data1)
except ValueError:
    print("Value error! Enter integer number!")
    exit()

data2 = input("Enter integer number2: ")
try:
    digit2  = int(data2)
except ValueError:
    print("Value error! Enter integer number!")
    exit()

data3 = input("Enter integer number3: ")
try:
    digit3  = int(data3)
except ValueError:
    print("Value error! Enter integer number!")
    exit()

num1 = str(digit1)
num2 = str(digit2)
num3 = str(digit3)

res = get_digit_merger(num1,num2,num3)
print(res)
