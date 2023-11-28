num1 = 0
num2 = 0
counter = 0
sum = 0
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



if num1<num2:
    while num1 <= num2:
        counter = num1
        sum += counter
        num1 += 1
    print("The sum of numbers in your given range: ",sum)
else:
    print("1st number must be bigger!")
