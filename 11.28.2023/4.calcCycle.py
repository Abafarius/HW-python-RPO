user_decision = ""
divide = 0
while user_decision !=  "no":

    user_in1 = input("Enter 1st number:")
    user_in2 = input("Enter 2nd number:")
    user_in3 = input("Enter operation with number (+,-,*,/,**):")

    try:
        num1 = int(user_in1)
    except ValueError:
        print("Enter valid number 1")
    try:
        num2 = int(user_in2)
    except ValueError: 
            print("Enter valid number 2")

    match user_in3:
        case "+":
                add = num1+num2
                print("The result of adding:", add)
        case "-":
                diff = num1 - num2
                print("The difference is:", diff)
        case "*":
                multiply = num1 * num2
                print("The result is:", multiply)
        case "/":
            try:
                divide = num1 / num2
            except ZeroDivisionError:
                print("No zero division in our community!")
            print("The result is:", divide)  
        case _:
                print("There is no such operation!")       

    user_in4 = input("Press any key to continue or 'no'\n")
    user_decision = user_in4.lower()