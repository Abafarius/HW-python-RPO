ud = input("Enter a number from 0-9:")

try:
    numU = int(ud)
except ValueError:
    print("Value error just occured! You must type single integer number as: 0,1,2,3,4,5,6,7,8,9.")
else:
    if numU == 0:
        print(")")
    elif numU == 1:
        print("!")
    elif numU == 2:
        print("@")
    elif numU == 3:
        print("#")
    elif numU == 4:
        print("$")
    elif numU == 5:
        print("%")
    elif numU == 6:
        print("^")
    elif numU == 7:
        print("&")
    elif numU == 8:
        print("*")
    elif numU == 9:
        print("(")
    else:
        print("no symbol for such number.")