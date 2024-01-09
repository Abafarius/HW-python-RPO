num1 = 0
num2 = 0

user_input1 = input("Enter number 1:")


try:
    num1 = int(user_input1)
except ValueError:
    print("Value Error has just occured. Enter an integer number")
    exit()


user_input2 = input("Enter number 2:")


try:
    num2 = int(user_input2)
except ValueError:
    print("Value Error has just occured. Enter an integer number")
    exit()

res = 1
counter = 0
#Euclide's Algorithm
if num1>num2:
    if num2 == 0:
        print("Second number can't be zero!")
    else:
        while (res != 0):
            res = num1 % num2
            num1 = num2
            if res == 0:
                break
            num2 = res

if num1<num2:
    if num1 == 0:
        print("Second number can't be zero!")
    else:
        while (res != 0):
            res = num2 % num1
            num2 = num1
            if res == 0:
                break
            num1 = res



print("The most big divider: ", num2)






