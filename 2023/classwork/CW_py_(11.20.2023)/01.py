import math
user_input1 = input("Enter integer number:")
user_input2 = input("Enter integer number:")
try:
    a = int(user_input1)
    b = int(user_input2)
except ValueError:
    print("You entered wrong value, please, enter strictly integer number")
else:
    diff = a-b
    try:
        result = math.sqrt(diff)
    except ValueError:
        print("First num must be bigger")
    else:
        print(result)



