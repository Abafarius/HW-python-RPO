user_x = input("Enter x (must be integer):")
user_y = input("Enter y (must be integer):")

try:
    x = int(user_x)
except ValueError:
    print("Enter valid x number!")
else:
    try:
        y = int(user_y)
    except ValueError:
        print("Enter valid y number!")
    else:
        if x > 0 and y > 0:
            print("1st quarter")
        elif x < 0 and y > 0:
            print("2nd quarter")
        elif x < 0 and y < 0:
            print("3rd quarter")
        elif x == 0 and y == 0:
            print("you are on 0") 
        elif x == 0:
            print("You are on axis y")
        elif y == 0:
            print("You are on axis x")

        else:
            print("4th quarter")