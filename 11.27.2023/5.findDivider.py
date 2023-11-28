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


counter = 0
#Euclide's Algorythm
if num2<num1:
    after_divide = num2 % num1
    while (after_divide != 0):
        num1%=after_divide
        after_divide = num1
        counter += 1
print(after_divide, counter)




