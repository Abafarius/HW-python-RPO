length_user = input("Enter length  of string: ")


try:
    length = int(length_user)
except ValueError:
    print("Error!")
    exit()

user_symbol1 = input("Enter a symbol: ")
user_symbol2 = input("Enter a symbol: ")

result_string = ""

for i in range(length):
    if i % 2 == 0:
        result_string += user_symbol1
    else:
        result_string += user_symbol2

print(result_string)

"""VN: задание не выполнено. Вам надо спросить у пользователя два символа: c1 и c2, а также длину строки.
Например, пользователь ввёл символы 'S' и 'N', и длину 5. Ваша программа должна вывести 'SNSNS'
"""

#AB: Теперь должно работать =D


