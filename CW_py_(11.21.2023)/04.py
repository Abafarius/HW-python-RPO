user_in = input("Enter integer number:")

try:
    num = int(user_in)
except ValueError:
    print("Enter valid Number!")
else:
    if num % 2:
        print("Your number is odd")
    else: 
        print("YOur number is even")
        