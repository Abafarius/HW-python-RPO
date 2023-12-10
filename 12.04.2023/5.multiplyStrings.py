length_user = input("Enter length  of string: ")

try:
    length = int(length_user)
except ValueError:
    print("Error!")
    exit()

givenChars = "C1 C2 " * length
print(givenChars)

"""VN: задание не выполнено. Вам надо спросить у пользователя два символа: c1 и c2, а также длину строки.
Например, пользователь ввёл символы 'S' и 'N', и длину 5. Ваша программа должна вывести 'SNSNS'
"""