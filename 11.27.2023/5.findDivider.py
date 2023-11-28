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


