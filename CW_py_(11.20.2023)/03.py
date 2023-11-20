user_input1 = input("Enter 1st num:")
user_input2 = input("Enter 2nd num:")

try :
    num1 = float(user_input1)
    num2 = float(user_input2)
except ValueError:
    print("Enter valid number")
else:
    try :
        division = num1/num2
    except ZeroDivisionError:
        print("2nd number can't be zero")
    else: 
        print("The result of division:", division)