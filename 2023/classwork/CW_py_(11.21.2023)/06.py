user_in1 = input("Enter 1st number:")
user_in2 = input("Enter 2nd number:")
user_in3 = input("Enter operation with number (+,-,*,/,**):")

try:
    num1 = int(user_in1)
except ValueError:
    print("Enter valid number 1")
else:
    try:
        num2 = int(user_in2)
    except ValueError: 
        print("Enter valid number 2")
    else:
        if user_in3 == "+":
            add = num1+num2
            print("The result of adding:", add)
        elif user_in3 == "-":
            diff = num1 - num2
            print("The difference is:", diff)
        elif user_in3 == "*":
            multiply = num1 * num2
            print("The result is:", multiply)
        elif user_in3 == "/":
            divide = num1 * num2
            print("The result is:", divide)
        elif user_in3 == "**":
            power = num1 ** num2
            print("The result is:", power)
        else:
            print("There is no such operation!")





