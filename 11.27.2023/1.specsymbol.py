ud = input("Enter a number from 0-9:")

try:
    numU = int(ud)
except ValueError:
    print("Value error just occured! You must type single integer number as: 0,1,2,3,4,5,6,7,8,9.")
else:
    match numU:
        case 0:
            print(")")
        case 1:
            print("!")
        case 2:
            print("@")
        case 3:
            print("#")
        case 4:
            print("$")
        case 5:
            print("%")
        case 6:
            print("^")
        case 7:
            print("&")
        case 8:
            print("*")
        case 9:
            print("(")            
        case _:
            print("no symbol for such number.")

