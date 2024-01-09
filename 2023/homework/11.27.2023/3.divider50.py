num1 = 0
counter = 0
user_input1 = input("Enter number:")


try:
    num1 = float(user_input1)
except ValueError:
    print("Value Error has just occured. Enter an integer number")
    exit()


while num1 > 50:
    num1 /= 2
    counter += 1
print("Result of dividing: ", num1, "\nTimes you divided: ", counter)

