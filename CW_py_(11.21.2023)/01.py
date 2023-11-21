user_in = input("Enter number:")

try:

    num = int(user_in)

except ValueError:
    print("Enter valid number")
else:
    if num > 0:
        print("You entered number bigger than 0")
    elif num < 0:
        print("You entered number lower than 0")
    else:
        print("You entered number 0")

