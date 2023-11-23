ud = input("Enter three-digit number:")
try:
    td = int(ud)
except ValueError:
    print("Value error just occured! You must type 3 digit integer number as: 123,456,555")
else:
    if 100 <= td <= 999:

        digit1 = td // 100
        digit2 = (td // 10) % 10
        digit3 = td % 10


        if digit1 == digit2 or digit2 == digit3 or digit1 == digit3:
            print("There are same digits in your number")
        else:
            print("There are no same digits in your number")
    else:
        print("Please, enter correct three-digit number.")