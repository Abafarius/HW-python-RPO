num1 = 0
num2 = 0

user_input1 = input("Enter number 1:")


try:
    num1 = int(user_input1)
except ValueError:
    print("Value Error has just occured. Enter an integer number")


user_input2 = input("Enter number 2:")


try:
    num2 = int(user_input2)
except ValueError:
    print("Value Error has just occured. Enter an integer number")

res = 1
counter = 0
#Euclide's Algorythm
if num1>num2:
    while (res != 0):
        res = num1 % num2
        num1 = num2
        num2 = res
        counter += 1
        print(res, counter)






