# Asking for three digited number
number_user = input("Введите трехзначное число: ")

#Translating from string to integer
number = int(number_user)

# calculating second digit of number
second_digit = (number // 10) % 10

# Printing result
print("Second digit of number:", second_digit)