# Asking for three digited number
number_user = input("Enter a three-digit number: ")

def_num = 137

#Translating from string to integer
try:
    number = int(number_user)
except ValueError:
    print("Wrong value. Default number 137 is active")
    number = def_num
# calculating second digit of number
second_digit = (number // 10) % 10

# Printing result
print("Second digit of number:", second_digit)